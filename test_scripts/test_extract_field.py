from .. import response_factory

def test_extract_field_tickbox():
    data = "monthly_neutronium.json"
    responses = response_factory.ContributorResponse(data, 0, 1, 202012)
    assert responses.extract_field_type("Q146") == "tickbox"

def test_extract_field_numeric():
    data = "monthly_neutronium.json"
    responses = response_factory.ContributorResponse(data, 0, 1, 202012)
    assert responses.extract_field_type("Q205") == "numeric"