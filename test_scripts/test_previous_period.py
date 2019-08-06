from .. import previous_periods

def test_split_period():
    data = "/home/ryan/question_data.json"
    previous = previous_periods.PreviousPeriods(data, 1000, 1001, 202011)
    assert previous.split_period() == ("2020", "11")

def test_decriment_simple():
    data = "/home/ryan/question_data.json"
    previous = previous_periods.PreviousPeriods(data, 1000, 1001, 202011)
    assert previous.decriment() == "202010"

def test_decriment_december():
    data = "/home/ryan/question_data.json"
    previous = previous_periods.PreviousPeriods(data, 1000, 1001, 202012)
    assert previous.decriment() == "202011"

def test_decriment_january():
    data = "/home/ryan/question_data.json"
    previous = previous_periods.PreviousPeriods(data, 1000, 1001, 202001)
    assert previous.decriment() == "201912"

def test_decriment_febuary():
    data = "/home/ryan/question_data.json"
    previous = previous_periods.PreviousPeriods(data, 1000, 1001, 201902)
    assert previous.decriment() == "201901"


