from .. import validation_dungeon
import os

'''
def test_assert_qvdq_larger_sum():
    # 4 randomly generated integers in the range [0, 9999] will almost certainly fail
    # We need to assert that some pass validation. We do this here, if should_fail is True,
    # we pass (as again it will likely fail). However if should_fail is False, we need to force
    # the responses to sum to Q204.
    # In this test we look at the case where the sum of the Qcodes is GREATER THAN the derived sum

    validations = dummy_data.Validations(["Q204", "Q201", "Q146"], data)
    responses = [{"Q204": 1200}, {"Q201": 400}, {"Q202": 412}, {"Q203": 400}]
    # Notice that 300 + 312 + 300 = 1212 != 1200
    print(responses)
    validation_schema = [{ "primary_q_codes": ["Q201", "Q202", "Q203"], "derived_q_code": "Q204", "formula": "Q201 + Q202 - Q203"}]
    asserted_valids = validations.assert_qvdq_pass(responses, validation_schema[0])
    assert asserted_valids == [{"Q204": 1200}, {"Q201": 388}, {"Q202": 412}, {"Q203": 400}]
'''

def test_make_qvdq_pass_smaller_sum():

    # 4 randomly generated integers in the range [0, 9999] will almost certainly fail
    # We need to assert that some pass validation. We do this here, if should_fail is True,
    # we pass (as again it will likely fail). However if should_fail is False, we need to force
    # the responses to sum to Q204.
    # In this test we look at the case where the sum of the Qcodes is LESS THAN the derived sum

    
    data = "monthly_neutronium.json"
    validations = validation_dungeon.ValidationDungeon(data, 0, 1, 202012)        
    contributor = {"responses":{"Q204": {"response": 1200}, "Q201": {"response": 388}, "Q202": {"response": 401}, "Q203": {"response": 399}}}
    # Notice that 400 + 388 + 400 = 1188 != 1200
    assert validations.make_qvdq_pass(contributor, "Q204") == {"responses":{"Q204": {"response": 1200}, "Q201": {"response": 388}, "Q202": {"response": 1211}, "Q203": {"response": 399}}}

def test_discover_validations():

    # We need to discover all the validations that a particular qCode is associated with

    data = "monthly_neutronium.json"
    validations = validation_dungeon.ValidationDungeon(data, 0, 1, 202012)
    assert validations.discover_validations("Q204") == {"Q204": ["QVDQ"]}

def test_check_failure_status():
    data = "monthly_neutronium.json"
    validations = validation_dungeon.ValidationDungeon(data, 0, 1, 202012)

    contributor = {'form_id': '001',
                 'period': 202012,
                 'reference': 1,
                 'responses': {'Q146': {'response': 442 },
                              'Q201': {'response': 500},
                              'Q202': {'response': 388},
                              'Q203': {'response': 400},
                              'Q204': {'response': 1200, 'should_fail': False}},
                'survey': '001'}


    assert validations.check_should_fail_status(contributor)["responses"] == {"Q146": {'response': 442}, "Q204": {"response": 1200, "should_fail": False}, "Q201": {"response": 1212}, "Q202": {"response": 388}, "Q203": {"response": 400}}


def test_find_largest():
    data = "monthly_neutronium.json"
    validations = validation_dungeon.ValidationDungeon(data, 0, 1, 202012)

    contributor = {'form_id': '001',
                 'period': 202012,
                 'reference': 1,
                 'responses': {'Q146': {'response': 442 },
                              'Q201': {'response': 400},
                              'Q202': {'response': 388},
                              'Q203': {'response': 500},
                              'Q204': {'response': 1200, 'should_fail': False}},
                'survey': '001'}
    
    valids = validations.extract_validations(contributor, "Q204", "QVDQ")

    assert validations.find_largest_for_qvdq(contributor, valids["derived_q_codes"]) == (500, "Q203")

def test_make_vp_pass():
    data = "monthly_neutronium.json"
    validations = validation_dungeon.ValidationDungeon(data, 0, 1, 202012)

    contributor = {'form_id': '001',
                 'period': 202012,
                 'reference': 1,
                 'responses': {'Q146': {'response': 442, "should_fail": False },
                              'Q201': {'response': 400},
                              'Q202': {'response': 388},
                              'Q203': {'response': 500},
                              'Q204': {'response': 1200, 'should_fail': False}},
                'survey': '001'}
    assert validations.make_vp_pass(contributor, "Q146")["responses"] ==  {'Q146': {'response': "", "should_fail": False },
                            'Q201': {'response': 400},
                              'Q202': {'response': 388},
                              'Q203': {'response': 500},
                              'Q204': {'response': 1200, 'should_fail': False}}

