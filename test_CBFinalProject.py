from CBFinalProject import parse, check_inequality, check_equality, check_power, check_divisor
import pytest

# Check Parser
def test_parse():
    assert parse("#>5") == ["#", ">", "5"]
    assert parse("#<5") == ["#", "<", "5"]
    assert parse("# > 5") == ["#", ">", "5"]
    assert parse("Is #>5?") == ["#", ">", "5"]
    assert parse("   #     >    5") == ["#", ">", "5"]
    assert parse("# > 500") == ["#", ">", "500"]
    assert parse("2 | #") == ["2", "|", "#"]
    assert parse("# ^ 3") == ["#", "^", "3"]
    assert parse("") == None
    assert parse("masala_dosa") == None


# Check Evaluators
t = 400
q = 64
def test_check_inequality():
    assert check_inequality(parse("#>5"), t)
    assert not check_inequality(parse("#<5"), t)
    assert check_inequality(["#", "<", "500"], t)
    with pytest.raises(ValueError):
        check_inequality(["E", ">", "e"], t)
    assert check_inequality(["3", ">", "2"], t)
    assert not check_inequality(["500", "<", "#"], t)
    assert check_inequality(["2", "|", "#"], t) == None
    assert check_inequality(["2", "=", "#"], t) == None
    assert check_inequality(["#", "^", "2"], t) == None
    assert check_inequality(["","",""], t) == None

def test_check_equality():
    assert check_equality(["#", "=", "400"], t)
    assert not check_equality(["#", "=", "401"], t)
    assert check_equality(["400", "=", "#"], t)
    assert check_equality(["", "", ""], t) == None
    assert check_equality(["500", "<", "#"], t) == None
    assert check_equality(["#", "^", "2"], t) == None
    assert check_equality(["","",""], t) == None

def test_check_divisor():
    assert check_divisor(["2", "|", "#"], t)
    assert not check_divisor(["3", "|", "#"], t)
    assert check_divisor(["4", "|", "#"], t)
    assert check_divisor(["#", "|", "800"], t)
    assert not check_divisor(["#", "|", "700"], t)
    assert check_divisor(["2", "=", "#"], t) == None
    assert check_divisor(["500", "<", "#"], t) == None
    assert check_divisor(["#", "^", "2"], t) == None
    assert check_divisor(["","",""], t) == None

def test_check_power():
    assert check_power(["#", "^", "2"], t)
    assert not check_power(["#", "^", "3"], t)
    assert not check_power(["#", "^", "4"], t)
    assert check_power(["2", "^", "#"], q)
    assert check_power(["4", "^", "#"], q)
    assert not check_power(["3", "^", "#"], q)
    assert check_power(["2", "=", "#"], t) == None
    assert check_power(["500", "<", "#"], t) == None
    assert check_power(["2", "|", "#"], t) == None
    assert check_power(["","",""], t) == None