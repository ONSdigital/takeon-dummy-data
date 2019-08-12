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

    assert validations.build_sum(contributor, "QVDQ", valids) == "500+388-400"
