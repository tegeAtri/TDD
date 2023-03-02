#!/usr/bin/env python
""" Test file for the String Calculator kata of Test Driven Development.

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
__date__ = "2023/02/26"
__deprecated__ = False
__email__ =  "patrik.tegetmeier@web.de"
__license__ = "GPLv3"
__maintainer__ = "developer"
__status__ = "Production"
__version__ = "0.0.1"


################################################################################
# Imports
import pytest
from src.stringcal import stringcal

def test_given_input_string_is_empty_stringcal_will_return_zero():
    """_summary_
    """
    val: int
    val = stringcal('')
    assert val == 0

@pytest.mark.parametrize("test_input,expected", [('1', 1), ('0', 0), ('4', 4), ('12', 12)])
def test_given_input_string_is_value_stringcal_will_return_value(test_input,expected):
    """_summary_
    """
    val: int
    val = stringcal(test_input)
    assert val == expected

@pytest.mark.parametrize("test_input,expected", [('0,0', 0), ('1,1', 2), ('3,2', 5), ('10,12', 22)])
def test_given_input_string_has_two_stings_stringcal_will_return_the_sum_of_both(test_input,expected):
    """_summary_
    """
    val: int
    val = stringcal(test_input)
    assert val == expected

@pytest.mark.parametrize("test_input,expected", [('0,0,0', 0), ('1,1,1,1', 4), ('3,2,2,3,1,1', 12), ('10,9,8,7,6,5,4,3,2,1', 55)])
def test_given_input_string_has_multiple_stings_stringcal_will_return_the_sum_of_all(test_input,expected):
    """_summary_
    """
    val: int
    val = stringcal(test_input)
    assert val == expected

@pytest.mark.parametrize("test_input,expected", [('0\n0\n0', 0), ('1\n1\n1\n1', 4), ('3\n2\n2\n3\n1\n1', 12), ('10\n9\n8\n7\n6\n5\n4\n3\n2\n1', 55)])
def test_given_input_string_has_multiple_stings_with_diff_sep_stringcal_will_return_the_sum_of_all(test_input,expected):
    """_summary_
    """
    val: int
    val = stringcal(test_input)
    assert val == expected

@pytest.mark.parametrize("test_input,expected", [('1,2\n3', 6), ('1\n2,3', 6)])
def test_given_input_string_has_diff_delimiter_included_stringcal_will_return_sum_for_valid_delimter(test_input,expected):
    """_summary_
    """
    val: int
    val = stringcal(test_input)
    assert val == expected

def test_given_input_string_has_delimiter_at_the_end_stringcal_will_return_error():
    """_summary_
    """
    with pytest.raises(ValueError):
        assert stringcal('1,2,')
