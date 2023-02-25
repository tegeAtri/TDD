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
import logging
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(filename)s/%(funcName)s(%(lineno)d) - %(levelname)s - %(message)s")
logging.disable(logging.DEBUG)


################################################################################
# Variables

################################################################################
# Functions

def logger_example():
    """Example logging function

    """
    logging.info('This is an info message')
    logging.debug('This is an debug message')
    logging.warning('This is a warning message')
    logging.error('This is a error message')
    logging.critical('This is a critical message')


def main():
    

################################################################################
# Scripts
if __name__ == "__main__":
    main()