import math


def find_hypotenuse(side1, side2):
    total = (side1 ** 2) + (side2 ** 2)
    hypotenuse = math.sqrt(total)
    return hypotenuse


def enter_first_name():
    input_name = input('Please enter your first name: ')
    if string_is_alpha(input_name):
        return input_name
    print('Please enter a valid name')
    return None


def string_is_alpha(in_string):
    for char in in_string:
        # check is ascii value is 65-90 | 97 - 122
        ascii_value = ord(char)
        if ascii_value < 65 or ascii_value > 122:
            return False
        # not 91-96 (special chars)
        elif 90 < ascii_value < 97:
            return False
    return True
