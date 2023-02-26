#!/usr/bin/env python
""" FizzBuzz kata of Test Driven Development.

Longer description of this module.

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.

This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
this program. If not, see <http://www.gnu.org/licenses/>.
"""

__author__ = "Patrik Tegetmeier"
__authors__ = ["One developer", "And another one", "etc"]
__contact__ = "patrik.tegetmeier@web.de"
__copyright__ = "Copyright $YEAR, $COMPANY_NAME"
__credits__ = ["One developer", "And another one", "etc"]
__date__ = "2023/02/25"
__deprecated__ = False
__email__ =  "patrik.tegetmeier@web.de"
__license__ = "GPLv3"
__maintainer__ = "developer"
__status__ = "Production"
__version__ = "0.0.1"


################################################################################
# Imports
import pytest
from src.fizzbuzz import fizzbuzz

@pytest.mark.parametrize("test_input,expected", [(0, "0"), (1, "1"), (2, "2"), (4, "4")])
def test_given_input_number_is_zero_fizzbuzz_will_return_zero(test_input, expected):
    """
        This function tests that FizzBuzz returns zero if given
        input number is zero.
    """
    val:str = fizzbuzz(test_input)
    assert val == expected

def test_given_input_number_is_three_fizzbuzz_will_return_fizz():
    """
        This function tests that FizzBuzz returns zero if given
        input number is zero.
    """
    val = fizzbuzz(3)
    assert val == "fizz"

@pytest.mark.parametrize("test_input,expected", [(3, "fizz"), (6, "fizz"), (9, "fizz"), (12, "fizz")])
def test_given_input_number_is_multiple_of_three_fizzbuzz_will_return_fizz(test_input,expected):
    """
        This function tests that FizzBuzz returns zero if given
        input number is zero.
    """
    val = fizzbuzz(test_input)
    assert val == expected

def test_given_input_as_float_fizzbuzz_will_return_with_exception():
    """
        This test checks that for a given input as float will generate
        an exception.
    """
    with pytest.raises(ValueError):
        assert fizzbuzz(3.141)

def test_given_input_as_string_fizzbuzz_will_return_with_exception():
    """
        This function tests that for a given input string will generate an exception.
    """
    with pytest.raises(ValueError):
        assert fizzbuzz("one")

def test_given_input_number_is_five_fizzbuzz_will_return_buzz():
    """
        This function tests that FizzBuzz returns zero if given
        input number is zero.
    """
    val = fizzbuzz(5)
    assert val == "buzz"

@pytest.mark.parametrize("test_input,expected", [(5, "buzz"), (10, "buzz"), (20, "buzz"), (25, "buzz")])
def test_given_input_number_is_multiple_of_five_fizzbuzz_will_return_buzz(test_input,expected):
    """
        This function tests that FizzBuzz returns zero if given
        input number is zero.
    """
    val = fizzbuzz(test_input)
    assert val == expected

def test_given_input_number_is_fifeteen_fizzbuzz_will_return_fizzbuzz():
    """
        This function tests that FizzBuzz returns fizzbuzz if given
        input number is fifteen.
    """
    val = fizzbuzz(15)
    assert val == "fizzbuzz"

@pytest.mark.parametrize("test_input,expected", [(15, "fizzbuzz"), (30, "fizzbuzz"), (45, "fizzbuzz"), (120, "fizzbuzz")])
def test_given_input_number_is_multiple_of_five_and_three_fizzbuzz_will_return_fizzbuzz(test_input,expected):
    """
        This function tests that FizzBuzz returns fizzbuzz if given
        input number is a multiple of three and five.
    """
    val = fizzbuzz(test_input)
    assert val == expected
