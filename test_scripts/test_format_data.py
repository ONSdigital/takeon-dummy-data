from insert_into_db.format_data import FormatData

def test_dict_one_attribute():
    test_dict = {"test_1": "Hello"}
    assert FormatData(["should_fail"]).search_dict(test_dict) == test_dict


def test_dict_sub_dict():
    test_dict = {"test_1": "Hello", "test_2":{"anAttribute": "Hello"}}
    assert FormatData(["should_fail"]).search_dict(test_dict) == test_dict

def test_format_data():
    contributor = {'form_id': '001',
    'period': 202012,
    'reference': 1235,
    'responses': {'Q146': {'response': 442, 'should_fail': True},
    'Q201': {'response': 1663, "should_fail": False},
    'Q202': {'response': 9387},
    'Q203': {'response': 2775},
    'Q204': {'response': 2477, 'should_fail': False}},
    'survey': '001'}

    contributor_output = {'form_id': '001',
    'period': 202012,
    'reference': 1235,
    'responses': {'Q146': {'response': 442},
    'Q201': {'response': 1663},
    'Q202': {'response': 9387},
    'Q203': {'response': 2775},
    'Q204': {'response': 2477}},
    'survey': '001'}


    formatted = FormatData(contributor, ["should_fail"]).format()
    assert formatted == contributor_output