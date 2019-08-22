from .. import validation_dungeon

data = "monthly_neutronium.json"

def test_build_sum():
    validations = validation_dungeon.ValidationDungeon(data, 1000, 1001, 202012)
    contributor = {'form_id': '001',
                 'period': 202012,
                 'reference': 1,
                 'responses': {'Q146': {'response': 442 },
                              'Q201': {'response': 500},
                              'Q202': {'response': 388},
                              'Q203': {'response': 400},
                              'Q204': {'response': 1200, 'should_fail': False}},
                'survey': '001'}

    valids = validations.extract_validations(contributor, "Q204", "QVDQ")

    assert validations.build_sum(contributor, "QVDQ", valids) == "500 + 388 - 400 "

def test_build_popm_sum():
    validations = validation_dungeon.ValidationDungeon(data, 1000, 1001, 202012)
    contributor = {'form_id': '001',
                 'period': 202012,
                 'reference': 1,
                 'responses': {'Q146': {'response': 442 },
                              'Q201': {'response': 500},
                              'Q202': {'response': 388},
                              'Q203': {'response': 400},
                              'Q204': {'response': 1200, 'should_fail': False}},
                'survey': '001'}
    back_data = {'form_id': '001',
                 'period': 202012,
                 'reference': 1,
                 'responses': {'Q146': {'response': 442 },
                              'Q201': {'response': 500},
                              'Q202': {'response': 388},
                              'Q203': {'response': 400},
                              'Q204': {'response': 412, 'should_fail': False}},
                'survey': '001'}

    valids = validations.extract_validations(contributor, "Q201", "POPM")
    print(valids)

    assert validations.build_sum(contributor, "POPM", valids, back_data=back_data, comparison="Q204" ) == "500 != 412 "

def test_build_popzc_sum():
    validations = validation_dungeon.ValidationDungeon(data, 1000, 1001, 202012)
    contributor = {'form_id': '001',
                 'period': 202012,
                 'reference': 1,
                 'responses': {'Q146': {'response': 442 },
                              'Q201': {'response': 500},
                              'Q202': {'response': 388},
                              'Q203': {'response': 400, 'should_fail': False},
                              'Q204': {'response': 1200, 'should_fail': False}},
                'survey': '001'}
    back_data = {'form_id': '001',
                 'period': 202012,
                 'reference': 1,
                 'responses': {'Q146': {'response': 442 },
                              'Q201': {'response': 500},
                              'Q202': {'response': 388},
                              'Q203': {'response': 400},
                              'Q204': {'response': 412, 'should_fail': False},
                              'Q205': {'response': 145}},
                'survey': '001'}

    valids = validations.extract_validations(contributor, "Q203", "POPZC")
    assert validations.build_sum(contributor, "POPZC", valids, back_data=back_data, comparison="Q205", threshold=11 ) == "400 != 145 and ( 400 != 0 or 145 != 0 ) and 400 - 145 > 11 "