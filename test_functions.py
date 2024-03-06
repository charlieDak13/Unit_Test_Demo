import math
from io import StringIO

import pytest
import util_functions

# test the find_hypotenuse() function
# function name and module must start with 'test_'


def test_find_hypotenuse():
    assert util_functions.find_hypotenuse(3, 4) == 5
    assert util_functions.find_hypotenuse(-1, 1) == math.sqrt(2)

    # show that passing a stirng object as one of the trsiagle sides caused a type error
    with pytest.raises(TypeError) as error:
        util_functions.find_hypotenuse('joe', 4) == 0
    assert error.type == TypeError

    #

    assert util_functions.find_hypotenuse(True, 4) == math.sqrt(17)
    with pytest.raises(TypeError) as error:
        util_functions.find_hypotenuse(None, 4) == 0
    assert error.type == TypeError


# capture file descripter
def test_enter_first_name(monkeypatch, capfd):

    # test a valid string
    input_string = 'joe'
    simulate_user_input = StringIO(input_string)
    monkeypatch.setattr("sys.stdin", simulate_user_input)

    assert util_functions.enter_first_name() == "joe"

    # test that the prompt was properly printed to terminal
    out, err = capfd.readouterr()
    assert out == 'Please enter your first name: '

    # test an invalid string
    input_string = '100'
    simulate_user_input = StringIO(input_string)
    monkeypatch.setattr("sys.stdin", simulate_user_input)

    assert util_functions.enter_first_name() is None

    # test that the prompt was properly printed to terminal
    out, err = capfd.readouterr()
    assert out == 'Please enter your first name: Please enter a valid name\n'



