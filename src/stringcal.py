#!/usr/bin/env python
""" String Calculator kata of Test Driven Development.

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
import re

################################################################################
# Variables

################################################################################
# Functions

def stringcal(numstring) -> int:
    """calculates an integer sum out of the string arguments

    Args:
        numstring (str): string with two comma seperated numbers

    Returns:
        int: sum of the string input
    """
    if isinstance(numstring, str):
        if re.search(r'\D$',numstring) is None:
            return convert_and_calculate_values(numstring)
    raise ValueError

def convert_and_calculate_values(numstr: str) ->int:
    """_summary_

    Args:
        numstr (str): _description_

    Returns:
        int: _description_
    """
    delimiter, numstr = define_separator(numstr)
    summands = numstr.split(delimiter)
    res: int = 0
    res = convert_and_sumup(summands)

    return res

def define_separator(numberstring) -> str:
    """_summary_

    Args:
        numberstring (_type_): _description_

    Returns:
        str: _description_
    """
    separator: str = '\n'
    if numberstring.startswith('//'):
        mat = re.search(r'(?<=//)[\s|\S]+(?=\n)',numberstring)
        if mat is not None:
            separator = mat.group()
            p = re.compile(r'//[\s|\S]+\n')
            numberstring = p.sub('',numberstring)
            print("string. ", numberstring)

    return separator, numberstring

def convert_and_sumup(summands) -> int:
    """_summary_

    Args:
        summands (_type_): _description_

    Returns:
        int: _description_
    """
    result: int = 0
    for _, value in enumerate(summands):
        result += look_for_separators(value)

    return result

def look_for_separators(value):
    """_summary_

    Args:
        value (_type_): _description_
    """
    result: int = 0
    match = re.search(r'\D',value)
    if match is not None:
        result = sum_different_separator_sum(value, match)
    else:
        result = int(value)

    return result

def sum_different_separator_sum(value, match):
    """_summary_

    Args:
        value (_type_): _description_
        match (_type_): _description_

    Returns:
        _type_: _description_
    """
    result: int = 0
    if match.group() == ',':
        subsum = value.split(',')
        for _, val in enumerate(subsum):
            result += int(val)

    return result
