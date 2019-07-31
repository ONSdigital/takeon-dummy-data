import random

class Response:
    def __init__(self, period, survey, form_id, form_qCodes, base_ref, max_ref): 
        self.period = period
        self.survey = survey
        self.form_id = form_id
        self.qCodes = form_qCodes
        self.base = base_ref
        self.max = max_ref
        random.seed(65324)

    def build_contributor(self):
        return {"reference": self.base, "period": self.period, "survey": self.survey, "form_id": self.form_id, "responses": self.build_response_data(), "should_fail": self.should_fail()}

    def should_fail(self):
        if random.randint(1, 10) < 4:
            return True
        return False

    def build_response_data(self):
        return [{"question_code": qCode, "response": random.randint(1, 9999)} for qCode in self.qCodes]

    def __iter__(self):
        return self

    def __next__(self):
        if self.base < self.max:
            self.base += 1 
            return self.build_contributor()
        else:
            raise StopIteration

    def __len__(self):
        return self.max - self.base

    def __add__(self, addition):
        self.period += addition

    def __sub__(self, sub):
        self.period -= sub

class Validations:
    def __init__(self, validation_q_codes, response_data):
        self.v_qcodes = validation_q_codes
        self.responses = response_data

    def grab_responses(self): 
        return [i["response"] for i in self.responses["responses"] if i["question_code"] in self.v_qcodes]
