from insert_into_db.format_data import FormatData

def test_format_data():
    contributor = {'form_id': '001',
    'period': '202012',
    'reference': '1234',
    'responses': [{'question_code': '642', 'response': 4667},
    {'question_code': '124', 'response': 8966},
    {'question_code': '432', 'response': 385}],
    'should_fail': "Overridden",
    'survey': '001'}

    contributor_output = {'form_id': '001',
    'period': '202012',
    'reference': '1234',
    'responses': [{'question_code': '642', 'response': 4667},
    {'question_code': '124', 'response': 8966},
    {'question_code': '432', 'response': 385}],
    'survey': '001'}


    formatted = FormatData(contributor, ["should_fail"]).format()
    assert formatted == contributor_output