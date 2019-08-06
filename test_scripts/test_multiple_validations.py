from .. import validation_dungeon

def test_multiple_validations():
    data = "/home/ryan/question_data.json"
    validations = validation_dungeon.ValidationDungeon(data, 0, 1, 202012)
    contributor = {'form_id': '001',
                 'period': 202012,
                 'reference': 1,
                 'responses': {'Q146': {'response': 442, "should_fail": False},
                              'Q201': {'response': 500},
                              'Q202': {'response': 388},
                              'Q203': {'response': 400},
                              'Q204': {'response': 1200, 'should_fail': False}},
                'survey': '001'}
    assert validations.check_should_fail_status(contributor)["responses"] == {'Q146': {'response': "", "should_fail": False }, 'Q201': {'response': 1212}, 'Q202': {'response': 388}, 'Q203': {'response': 400}, 'Q204': {'response': 1200, 'should_fail': False}}


