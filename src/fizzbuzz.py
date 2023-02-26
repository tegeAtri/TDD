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

################################################################################
# Variables

################################################################################
# Functions

def fizzbuzz(val) -> str:
    """calculates the fizzbuzz from val

    Args:
        val (int): input value

    Returns:
        str: string of the input value
    """
    if isinstance(val, int):
        return calc(val)
    raise ValueError

def calc(val:int) -> str:
    """_summary_

    Args:
        val (_type_): _description_

    Returns:
        _type_: _description_
    """
    res:str = ''

    if is_val_fizz(val) and is_val_buzz(val):
        res = "fizzbuzz"
    elif is_val_fizz(val):
        res = "fizz"
    elif is_val_buzz (val):
        res = "buzz"
    else:
        res = str(val)

    return res

def is_val_fizz(val:int) -> bool:
    """Check if val is a multiple of three

    Args:
        val (int): _description_
    """
    if (val % 3 == 0) and (val != 0):
        return True
    return False

def is_val_buzz(val:int) -> bool:
    """Check if val is a multiple of five

    Args:
        val (int): _description_
    """
    if (val % 5 == 0) and (val != 0):
        return True
    return False
