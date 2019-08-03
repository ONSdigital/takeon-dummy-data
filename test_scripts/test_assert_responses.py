from .. import dummy_data

data = dummy_data.Response("202012", "999", "001", ["Q204", "Q201", "Q202", "Q203", "Q146"],"12345678",0).build_contributor()

def test_assert_qvdq_larger_sum():
    # 4 randomly generated integers in the range [0, 9999] will almost certainly fail
    # We need to assert that some pass validation. We do this here, if should_fail is True,
    # we pass (as again it will likely fail). However if should_fail is False, we need to force
    # the responses to sum to Q204.
    # In this test we look at the case where the sum of the Qcodes is GREATER THAN the derived sum

    validations = dummy_data.Validations(["Q204", "Q201", "Q146"], data)
    # responses = validations.grab_responses()
    responses = [{"Q204": 1200}, {"Q201": 400}, {"Q202": 412}, {"Q203": 400}]
    # Notice that 300 + 312 + 300 = 1212 != 1200
    print(responses)
    validation_schema = [{ "primary_q_codes": ["Q201", "Q202", "Q203"], "derived_q_code": "Q204", "formula": "Q201 + Q202 - Q203"}]
    asserted_valids = validations.assert_qvdq_pass(responses, validation_schema[0])
    assert asserted_valids == [{"Q204": 1200}, {"Q201": 388}, {"Q202": 412}, {"Q203": 400}]

def test_assert_qvdq_smaller_sum():
    
    # 4 randomly generated integers in the range [0, 9999] will almost certainly fail
    # We need to assert that some pass validation. We do this here, if should_fail is True,
    # we pass (as again it will likely fail). However if should_fail is False, we need to force
    # the responses to sum to Q204.
    # In this test we look at the case where the sum of the Qcodes is LESS THAN the derived sum

    validations = dummy_data.Validations(["Q204", "Q201", "Q146"], data)
    # responses = validations.grab_responses()
    responses = [{"Q204": 1200}, {"Q201": 400}, {"Q202": 388}, {"Q203": 400}]
    # Notice that 400 + 388 + 400 = 1188 != 1200
    print(responses)
    validation_schema = [{ "primary_q_codes": ["Q201", "Q202", "Q203"], "derived_q_code": "Q204", "formula": "Q201 + Q202 - Q203"}]
    asserted_valids = validations.assert_qvdq_pass(responses, validation_schema[0])
    assert asserted_valids == [{"Q204": 1200}, {"Q201": 400}, {"Q202": 388}, {"Q203": 400}]
