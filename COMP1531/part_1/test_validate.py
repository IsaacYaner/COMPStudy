from validate import UserInputError,validate_user_name
import pytest

def test_validate_correct_input():
    input = "apple345"
    assert validate_user_name(input) == True

def test_validate_empty_user_name():
    input = ""
    with pytest.raises(UserInputError) as info:
        validate_user_name(input) 
    assert 'user input error' in str(info.value)
'''
'''
def test_validate_space():
    input = "appl 345"
    with pytest.raises(UserInputError) as info:
        validate_user_name(input) 
    assert 'user input error' in str(info.value)

def test_validate_incorrect_length():
    input = "really_a_very_longpassword"
    with pytest.raises(UserInputError) as info:
        validate_user_name(input) 
    assert 'user input error' in str(info.value)
