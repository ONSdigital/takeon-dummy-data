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
        contributor =  {"reference": self.base, "period": self.period, "survey": self.survey, "form_id": self.form_id, "responses": self.build_response_data()}

        return contributor

    def should_fail(self):
        die = random.randint(1, 15)
        if die < 5:
            return True
        return False

    def build_response_data(self):
        return [{"question_code": qCode, "response": random.randint(0, 9999), "should_fail": self.should_fail()} for qCode in self.qCodes]

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


class Validations:
    def __init__(self, validation_q_codes, response_data):
        self.v_qcodes = validation_q_codes
        self.responses = response_data

    def grab_responses(self):
        # Build a dict of responses in the form question_code: response
        # return [{i["question_code"]: i["response"]} for i in self.responses["responses"] if i["question_code"] in self.v_qcodes]
        return [{i["question_code"]: i["response"]} for i in self.responses["responses"]]
    
    def assert_validation_pass(self, response_dict, validation_rules):
        for rule in validation_rule.keys():
            if rule is "QVDQ":
                return

    def assert_qvdq_pass(self, responses, validation_schema):
        derived_response = responses[0][validation_schema["derived_q_code"]]
        compound_responses = validation_schema["primary_q_codes"]
        validation_sum = 0
        
        for i in compound_responses:
            for j in responses:
                try:
                    validation_sum += j[i]
                except KeyError:
                    pass
        if validation_sum != int(derived_response) and validation_sum > int(derived_response):
            diff = int(derived_response) - validation_sum
            responses[1][compound_responses[0]] += diff
        elif validation_sum != int(derived_response) and int(derived_response) > validation_sum:
            diff = int(derived_response) - validation_sum
            responses[1][compound_responses[0]] += diff
        return responses
