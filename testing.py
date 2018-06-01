"""
CP1404/CP5632 Practical
Testing demo using assert and doctest
"""

import doctest
from car import Car


def repeat_string(s, n):
    string_list = []
    while n != 0:
        string_list.append(s)
        n -= 1
    return " ".join(string_list)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 5)
    True
    """
    return len(word) > length


def run_tests():
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    # the test below should fail
    assert repeat_string("hi", 2) == "hi hi"

    test_car = Car()
    assert test_car.odometer == 0, "Car does not set odometer correctly"

    test_car = Car(fuel=10)
    assert test_car.fuel == 10
    test_car_2 = Car()
    assert test_car_2.fuel == 0


run_tests()

doctest.testmod()


# TODO: 5. Write and test a function to format a phrase as a sentence,

def make_sentence(phrase):
    if phrase[len(phrase)-1] == ".":
        pass
    else:
        phrase += "."
    if phrase[0].isupper():
        pass
    else:
        phrase.capitalize()  # WHY IS .CAPTILIZE() NOT WORKING
    return phrase


assert make_sentence("hello") == "Hello."
assert make_sentence("It is an ex parrot.") == "It is an ex parrot."
assert make_sentence("GDAY!") == "GDAY!."