from . import response_factory
from . import period_on_period as pop
from numba import jit
import json


class ValidationDungeon(response_factory.ContributorResponse):
    '''
    Force the validations to yield the truth!
    '''
    def __init__(self, form_data, start_reference, end_reference, period, seed=None): 
        super().__init__(form_data, start_reference, end_reference, period)
        self.pop = pop.PeriodOnPeriod(form_data, start_reference, end_reference, period, seed=10)
        self.pop_data = list(self.pop)

    def check_should_fail_status(self, contributor):
        for question in contributor["responses"].keys():
            print(contributor["responses"][question])
            try:
                if contributor["responses"][question]["should_fail"] in (False, "False"):
                     contributor["responses"][question]["response"] = self.assert_pass(contributor, question)["responses"][question]["response"]
            except KeyError as e:
                print("{} does not have should_fail attribute".format(question))
                continue
        return contributor

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
            if rule == "POPM":
                print("Running POPM")
                return self.make_popm_pass(contributor, question)

    def discover_validations(self, q_code):
        '''
        Now we had a question code that should fail. Great! But which validations is that qCode attached
        to? We need to traverse the validations part of our validation schema json and find the
        validations which has our question code as the primary_q_code attribute.
        '''
        validations = {q_code: []}
        for validation_name in self.validations.keys():
            for valid in self.validations[validation_name]:
                print(validation_name)
                if valid["primary_q_code"] == q_code:
                    validations[q_code].append(validation_name)
        return validations


    def make_vp_pass(self, contributor, q_code):
        primary_q_code = contributor["responses"][q_code]["response"]
        contributor["responses"][q_code]["response"] = ""
        return contributor

    def make_qvdq_pass(self, contributor, q_code):
        derived_response = contributor["responses"][q_code]["response"]
        derived_q_codes = None
        validation_dict = self.extract_validations(contributor, q_code, "QVDQ")
        validation_sum = eval(self.build_sum(contributor, "QVDQ", validation_dict))

        largest_value = self.find_largest_for_qvdq(contributor, validation_dict["derived_q_codes"])

        if validation_sum > int(derived_response):
            diff = int(derived_response) - validation_sum
            contributor["responses"][largest_value[1]]["response"] += diff
        elif int(derived_response) > validation_sum:
            diff = int(derived_response) - validation_sum
            contributor["responses"][largest_value[1]]["response"] += diff
        return contributor 

    
    def find_largest_for_qvdq(self, contributor, derived_q_codes):
        '''
        find the largest value in the derived qcode set
        '''
        derived_list = derived_q_codes
        current_largest = (contributor["responses"][derived_list[0]]["response"], derived_list[0])
        for i in derived_list[1:]:
            if int(contributor["responses"][i]["response"]) > int(current_largest[0]):
                current_largest = (contributor["responses"][i]["response"], i)
        return current_largest

    def build_sum(self, contributor, rule, validation_dict, back_data=None):
        formula = validation_dict["formula"]
        formula_atoms = formula.split(" ")
        formula_string = ""
        print(contributor)
        for i in formula_atoms:
            if i in ("+", "-", "!=", ">", "<"):
                formula_string += i
            else:
                formula_string += str(contributor["responses"][i]["response"])
        return formula_string

    def make_popm_pass(self, contributor, q_code):
        validation_dict = self.extract_validations(contributor, q_code, "POPM")
        primary = validation_dict["primary_q_code"]
        comparison = validation_dict["POPM"]["comparison_q_code"]
        # return tuple (CONTRIBUTOR_OBJECT, LIST_INDEX)
        pop_data = self.pop.b_search(contributor["reference"], self.pop_data, 0, len(self.pop_data))
        does_pass = self.build_popm_sum(contributor, primary, comparison, pop_data[0], validation_dict)
        self.pop_data[pop_data[1]]["responses"][comparison]["response"] = contributor["responses"][primary]["response"] 
        return contributor

    def build_popm_sum(self, contributor, q_code, comparison, back_data, validation_dict):
        formula_atoms = validation_dict["formula"].split(" ")
        primary_response = contributor["responses"][q_code]["response"]
        comparison = back_data["responses"][comparison]["response"]
        print("atoms: {}".format(formula_atoms))
        return "{prime} {op} {comp}".format(prime=primary_response, op=formula_atoms[1], comp=comparison)

    def output_back_data(self):
        with open("/home/ryan/Documents/pp_data.json", "w+") as file:
            file.write(json.dumps(self.pop_data, indent=4))

    def extract_validations(self, contributor, q_code, rule):
    # Extract correct validation dict from an array of validations
        for i in self.validations[rule]:
            if i["primary_q_code"] == q_code:
                return i
