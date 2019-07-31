from .. import dummy_data


data = dummy_data.Response("202012", "999", "001", ["642", "124", "432"],"12345678",0).build_contributor()

def test_data_builds_correctly():
    test_outputs = [{'question_code': '642', 'response': 4668},
  {'question_code': '124', 'response': 8967},
  {'question_code': '432', 'response': 386}]

    assert data["responses"] == test_outputs

def test_contributor_builds_correctly():
    test_outputs = {'form_id': '001',
                    'period': '202012',
                    'reference': '12345678',
                    'responses': [{'question_code': '642', 'response': 4668},
                    {'question_code': '124', 'response': 8967},
                    {'question_code': '432', 'response': 386}],
                    'should_fail': False,
                    'survey': '999'} 
    contributor = data
    assert contributor["form_id"] == test_outputs["form_id"]
    assert contributor["period"] == test_outputs["period"]
    assert contributor["reference"] == test_outputs["reference"]
    assert contributor["should_fail"] == test_outputs["should_fail"]
    assert contributor["survey"] == test_outputs["survey"]
