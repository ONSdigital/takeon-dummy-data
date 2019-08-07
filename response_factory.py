import json
import random

class ContributorResponse:
    def __init__(self, form_data, start_reference, end_reference, period):
        self.form_data = form_data
        self.form = json.loads(self.load_json(form_data))
        self.start_ref = start_reference
        self.end_ref = end_reference
        self.period = period
        self.survey_name = self.form["survey_name"]
        self.survey = self.form["survey_code"]
        self.form_id = self.form["form_id"]
        self.question_codes = self.form["question_codes"]
        self.v_q_codes = self.form["validation_question_codes"]
        self.validations = self.form["validations"]
        random.seed(20)

    @staticmethod
    def load_json(data_location):
        with open(data_location, "r") as file:
            return file.read()

    def build_contributor(self):
        return  {"reference": self.start_ref, "period": self.period, "survey": self.survey, "form_id": self.form_id, "responses": self.build_response_data()}

    def build_response_data(self):
        responses = {}
        for question in self.question_codes:
            if question in self.v_q_codes:
                responses[question] = {"response": random.randint(0, 9999), "should_fail": True if random.randint(0,15) > 10 else False}
            else:
                responses[question] = {"response": random.randint(0, 9999)}
        return responses

    def __iter__(self):
        return self

    def __next__(self):
        while self.start_ref < self.end_ref:
            self.start_ref += 1
            return self.build_contributor()
        else:
            raise StopIteration

    def __len__(self):
        return self.end_ref - self.start_ref
