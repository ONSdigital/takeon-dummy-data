from .. import response_factory 

data_location = "/home/ryan/question_data.json"
data = response_factory.ContributorResponse(data_location, 1234, 1235, 202012).build_contributor()

def test_data_builds_correctly():
    
    test_outputs = {'form_id': '001',
                     'period': 202012,
                     'reference': 1235,
                     'responses': {'Q146': {'response': 442, 'should_fail': True},
                     'Q201': {'response': 1663, "should_fail": False},
                     'Q202': {'response': 9387},
                     'Q203': {'response': 2775},
                     'Q204': {'response': 2477, 'should_fail': False}},
                     'survey': '001'}


    assert data["responses"] == test_outputs["responses"]

def test_contributor_builds_correctly():
    test_outputs = {'form_id': '001',
                    'period': '202012',
                    'reference': '1234',
                    'responses': [{'question_code': '642', 'response': 4667},
                    {'question_code': '124', 'response': 8966},
                    {'question_code': '432', 'response': 385}],
                    'should_fail': "Overridden",
                    'survey': '001'}

    contributor = data
    assert str(contributor["form_id"]) == str(test_outputs["form_id"])
    assert str(contributor["period"]) == str(test_outputs["period"])
    assert str(contributor["reference"]) == str(test_outputs["reference"])
    assert str(contributor["survey"]) == str(test_outputs["survey"])
