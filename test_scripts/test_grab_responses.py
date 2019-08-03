from .. import dummy_data

def test_grab_responses():
    resp = dummy_data.Response("202012", "999", "001", ["642", "124", "432"], "12345678", 0).build_contributor()
    print(resp["responses"])
    validation_q_codes = ["124", "432"]
    valids = dummy_data.Validations(validation_q_codes, resp)
    assert valids.grab_responses() == [{"642": 4667}, {"124": 385}, {"432": 3708}]


