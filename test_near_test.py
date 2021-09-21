import pytest

@pytest.mark.parametrize("a, b, c", [
    (1, 2, 3),
    (0.1, 0.2, 0.3)
    ])
def test_add(a, b, c):
    from near_test import add
    answer = add(a, b)
    #assert answer == c # will report error b/c 0.1+0.2=0.3000004
    #b/c python stores 0.1 and 0.2 in kind of jumpy way
    assert pytest.approx(answer) == c #answer approx. equals c
    
    #pytest.approx(ans, abs=2) == c   checks if ans falls within c+-2