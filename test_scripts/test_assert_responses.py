from .. import dummy_data
from .. import validation_dungeon

data = dummy_data.Response("202012", "999", "001", ["Q204", "Q201", "Q202", "Q203", "Q146"],"12345678",0).build_contributor()

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


def test_make_qvdq_pass_smaller_sum():

    # 4 randomly generated integers in the range [0, 9999] will almost certainly fail
    # We need to assert that some pass validation. We do this here, if should_fail is True,
    # we pass (as again it will likely fail). However if should_fail is False, we need to force
    # the responses to sum to Q204.
    # In this test we look at the case where the sum of the Qcodes is LESS THAN the derived sum


    data = "/home/ryan/question_data.json"
    validations = validation_dungeon.ValidationDungeon(data, 0, 1, 202012)        
    contributor = {"responses":{"Q204": {"response": 1200}, "Q201": {"response": 388}, "Q202": {"response": 400}, "Q203": {"response": 400}}}
    # Notice that 400 + 388 + 400 = 1188 != 1200
    assert validations.make_qvdq_pass(contributor, "Q204") == {"responses":{"Q204": {"response": 1200}, "Q201": {"response": 400}, "Q202": {"response": 400}, "Q203": {"response": 400}}}

def test_discover_validations():

    # We need to discover all the validations that a particular qCode is associated with

    data = "/home/ryan/question_data.json"
    validations = validation_dungeon.ValidationDungeon(data, 0, 1, 202012)
    assert validations.discover_validations("Q204") == {"Q204": ["QVDQ"]}

def test_check_failure_status():
    data = "/home/ryan/question_data.json"
    validations = validation_dungeon.ValidationDungeon(data, 0, 1, 202012)

    contributor = {'form_id': '001',
                 'period': 202012,
                 'reference': 1,
                 'responses': {'Q146': {'response': 442 },
                              'Q201': {'response': 400},
                              'Q202': {'response': 388},
                              'Q203': {'response': 400},
                              'Q204': {'response': 1200, 'should_fail': False}},
                'survey': '001'}


    assert validations.check_should_fail_status(contributor)["responses"] == {"responses":{"Q204": {"response": 1200, "should_fail": False}, "Q201": {"response": 400}, "Q202": {"response": 400}, "Q203": {"response": 400}}}

