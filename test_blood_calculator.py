# By convention, the module name is 'test_<ModuleName>'


#test normal HDL
# By convention, the function name is 'test_<funcName>'
def test_hdl_analysis_normal():
    from blood_calculator import hdl_analysis
    answer = hdl_analysis(65)
    expected = "Normal"
    assert answer == expected
    
# will output error if doesn't have: __name__ == "__main__": interface() 
# lines in original code, b/c test_ cannot take interface

#if want to test other HDL cases, DON'T use same function names,
#otherwise will only run the last one !!!
# b/c pytest first scans through all the functions by name, 
# and will override previous memory if it sees a same name, so only the last was run
def test_hdl_analysis_bl():
    from blood_calculator import hdl_analysis
    answer = hdl_analysis(45)
    expected = "Borderline Low"
    assert answer == expected
    
def test_hdl_analysis_low():
    from blood_calculator import hdl_analysis
    answer = hdl_analysis(15)
    expected = "Low"
    assert answer == expected
    
    
# OR, can put in one fucntion with multiple calls
# =============================================================================
# def test_hdl_analysis():
#     from blood_calculator import hdl_analysis
#     answer = hdl_analysis(65)
#     expected = "Normal"
#     assert answer == expected
#     answer = hdl_analysis(45)
#     expected = "Borderline Low"
#     assert answer == expected #if test failed here, func stops & will not run later tests
#     answer = hdl_analysis(15)
#     expected = "Low"
#     assert answer == expected
# =============================================================================

# Actually, should use a decorator:
import pytest

# the decorator started with @
# parametrize in pytest takes in two parameters: ("string", [list])
# will loop through the list, tells when the func starts and ends (runs b/f and after the function)
@pytest.mark.parametrize("HDL_value, expected", [
    (65, "Normal"),
    (45, "Borderline Low"),
    (15, "Low")])
def test_hdl_analysis(HDL_value, expected):
    from blood_calculator import hdl_analysis
    answer = hdl_analysis(HDL_value)
    assert answer == expected
    
@pytest.mark.parametrize("in_string, expected", [
    ("ab", True),
    ("abc", False),
    ("12345456", False)])
def test_check_input(in_string, expected):
    from blood_calculator import check_input
    answer = check_input(in_string)
    assert answer == expected
    
    