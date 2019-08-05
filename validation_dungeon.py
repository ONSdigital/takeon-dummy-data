from . import response_factory
import json

class ValidationDungeon(response_factory.ContributorResponse):
    '''
    Force the validations to yield the truth!
    '''

    def check_should_fail_status(self, contributor):
        for question in contributor["responses"].keys():
            print(contributor["responses"][question])
            try:
                if contributor["responses"][question]["should_fail"] in (False, "False"):
                    return self.assert_pass(contributor, question)
                return contributor
            except KeyError as e:
                print("{} does not have should_fail attribute".format(question))
                continue

    def assert_pass(self, contributor, question):
        '''
        We have validations that will fail almost surely, however some these will need to pass
        that is the purpose of this method
        '''
        # First discover all the validations that are associated with the question code
        validations = self.discover_validations(question)
        print("validation rule to run: {}".format(validations))
        for rule in validations[question]:
            if rule == "QVDQ":
                print("Running QVDQ")
                return self.make_qvdq_pass(contributor, question)

    def discover_validations(self, q_code):
        '''
        Now we had a question code that should fail. Great! But which validations is that qCode attached
        to? We need to traverse the validations part of our validation schema json and find the
        validations which has our question code as the primary_q_code attribute.
        '''
        validations = {q_code: []}
        for validation_name in self.validations.keys():
            print(validation_name)
            if self.validations[validation_name]["primary_q_code"] == q_code:
                validations[q_code].append(validation_name)
        return validations

    def make_qvdq_pass(self, contributor, q_code):
        derived_response = contributor["responses"][q_code]["response"]
        derived_q_codes = self.form["validations"]["QVDQ"]["derived_q_codes"]
        validation_sum = 0

        for q_code in derived_q_codes:
            validation_sum += contributor["responses"][q_code]["response"]

        if validation_sum > int(derived_response):
            diff = int(derived_response) - validation_sum
            contributor["responses"][derived_q_codes[0]]["response"] += diff
        elif int(derived_response) > validation_sum:
            diff = int(derived_response) - validation_sum
            contributor["responses"][derived_q_codes[0]]["response"] += diff
        return contributor 


        
