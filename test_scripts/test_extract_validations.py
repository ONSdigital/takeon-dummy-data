from .. import validation_dungeon

def test_extract_validations():
    data = "monthly_neutronium.json"
    validations = validation_dungeon.ValidationDungeon(data, 0, 1, 202012)

    contributor = {'form_id': '001',
    'period': 202012,
    'reference': 1,
    'responses': {'Q146': {'response': 442, "should_fail": False},
                 'Q201': {'response': 500},
                 'Q202': {'response': 388, "should_fail": False},
                 'Q203': {'response': 400},
                 'Q204': {'response': 1200, 'should_fail': False}},
   'survey': '001'}

    assert validations.extract_validations(contributor, "Q204", "QVDQ") == { "derived_q_codes": ["Q201", "Q202", "Q203"], "primary_q_code": "Q204", "formula": "Q201 + Q202 - Q203"}

def test_extract_validations_from_multiple():
    data = "monthly_neutronium.json"
    validations = validation_dungeon.ValidationDungeon(data, 0, 1, 202012)

    contributor = {'form_id': '001',
    'period': 202012,
    'reference': 1,
    'responses': {'Q146': {'response': 442, "should_fail": False},
                    'Q201': {'response': 500},
                    'Q202': {'response': 388, "should_fail": False},
                    'Q203': {'response': 400},
                    'Q204': {'response': 1200, 'should_fail': False}},
    'survey': '001'}

    assert validations.extract_validations(contributor, "Q205", "VP") == {"primary_q_code": "Q205", "formula": "Q205 != \"\""}
        