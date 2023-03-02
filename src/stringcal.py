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
            return calc(numstring)
    raise ValueError

def calc(numstr: str) ->int:
    """_summary_

    Args:
        numstr (str): _description_

    Returns:
        int: _description_
    """
    summands = numstr.split("\n")
    res: int = 0
    res = sumup(summands)

    return res

def sumup(summands) -> int:
    """_summary_

    Args:
        summands (_type_): _description_

    Returns:
        int: _description_
    """
    result: int = 0
    for _, value in enumerate(summands):
        match = re.search(r'\D',value)
        if match is not None:
            if match.group() == ',':
                subsum = value.split(',')
                for _, val in enumerate(subsum):
                    result += int(val)
        else:
            result += int(value)
    
    return result

