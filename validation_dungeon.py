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
            if rule == "VP":
                print("Running VP")
                return self.make_vp_pass(contributor, question)

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

    def make_vp_pass(self, contributor, q_code):
        primary_q_code = contributor["responses"][q_code]["response"]
        contributor["responses"][q_code]["response"] = ""
        return contributor

    def make_qvdq_pass(self, contributor, q_code):
        derived_response = contributor["responses"][q_code]["response"]
        derived_q_codes = self.form["validations"]["QVDQ"]["derived_q_codes"]
        validation_sum = eval(self.build_sum(contributor, "QVDQ"))

        largest_value = self.find_largest_for_qvdq(contributor)

        if validation_sum > int(derived_response):
            diff = int(derived_response) - validation_sum
            contributor["responses"][largest_value[1]]["response"] += diff
        elif int(derived_response) > validation_sum:
            diff = int(derived_response) - validation_sum
            contributor["responses"][largest_value[1]]["response"] += diff
        return contributor 

    
    def find_largest_for_qvdq(self, contributor):
        '''
        find the largest value in the derived qcode set
        '''
        derived_list = self.form["validations"]["QVDQ"]["derived_q_codes"]
        current_largest = (contributor["responses"][derived_list[0]]["response"], derived_list[0])
        for i in derived_list[1:]:
            if int(contributor["responses"][i]["response"]) > int(current_largest[0]):
                current_largest = (contributor["responses"][i]["response"], i)
        return current_largest

    def build_sum(self, contributor, rule):
        formula = self.form["validations"][rule]["formula"]
        formula_atoms = formula.split(" ")
        formula_string = ""
        print(contributor)
        for i in formula_atoms:
            if i in ("+", "-", "!="):
                formula_string += i
            else:
                formula_string += str(contributor["responses"][i]["response"])
        return formula_string

        
