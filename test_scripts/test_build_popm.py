from .. import validation_dungeon

def test_build_popm():
    data = "monthly_neutronium.json"
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
    back_data = {'form_id': '001',
                 'period': 202011,
                 'reference': 1,
                 'responses': {'Q146': {'response': 442, "should_fail": False},
                              'Q201': {'response': 500},
                              'Q202': {'response': 388},
                              'Q203': {'response': 400},
                              'Q204': {'response': 1200, 'should_fail': False}},
                'survey': '001'}

    validation_dict  = validations.extract_validations(contributor, "Q201", "POPM")

    assert validations.build_popm_sum(contributor, "Q201", "Q204", back_data, validation_dict) == "500 != 1200"


