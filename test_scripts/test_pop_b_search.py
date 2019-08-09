from .. import period_on_period as pop

def test_b_search():
    popm = pop.PeriodOnPeriod("/home/ryan/question_data.json", 0, 1, 202020)
    test_match = [{"reference": i} for i in range(100)]
    assert popm.b_search(47, test_match, 0, len(test_match)) == ({"reference": 47}, 47)
