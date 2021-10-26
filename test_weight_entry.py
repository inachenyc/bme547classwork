import pytest


@pytest.mark.parametrize("input, expected", [
    ("22 lb", 10),
    ("50 kg", 50),
    ("22.1 lb", 10),
    ("35.5 kg", 36),  # do want to be rounded
    ("22 lbs", 10),
    ("22 lbS", 10),
    # ("too much", False), # test for bad input
    # ("22", False), # test for missing unit
    ("22 KG", 22),  # capitalize
    ("22 Kg", 22),
    # ("22kg", 22), # no space
    # ("64 g", False), # non-compatible units
    # ("ten kg", False),
    ("-22 lb", -10)  # negative numbers
    ])
def test_parse_weight_input(input, expected):
    from weight_entry import parse_weight_input
    answer = parse_weight_input(input)
    assert answer == expected
