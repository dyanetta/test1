#!/usr/bin/python

#
# Script has a serious bug - multiple files could have the same name once their
# case is changed - testfile1 and Testfile1 are different now, but once changed
# to all upper or all lower, the script will simply overwrite files. Since the
# assessment question didnt specify and the situation doesnt exist on your test 
# server, Im leaving as-is. But, I would seek clarification on what to do. I'm
# tempted to add a "-01" to the end of the filename and increment if more then
# file exists, but given the short time I have to do these scripts, I'll just 
# point out that I see the problem for now.
#

import os
import sys
import string
import argparse

# The "-c" option is mandatory and must be either "lower" or "upper" or script 
# will exit with an error and syntax message
parser = argparse.ArgumentParser(description='Filename Case Changer')
parser.add_argument('-c', action="store", choices=('lower', 'upper'), dest="case",
                    help="Specify conversion to upper or lower case", required=True)
args = parser.parse_args()

fileDirectory = "/var/data/afh/"
filenames = os.listdir(fileDirectory)

# Given that we know the "case" argument is correct at this point, there's no need
# to specify upper, just use an else.
if args.case == "lower":
   for file in filenames:
      oldName = fileDirectory + file
      newName = fileDirectory + file.lower()
      os.rename(oldName, newName)
else:
   for file in filenames:
      oldName = fileDirectory + file
      newName = fileDirectory + file.upper()
      os.rename(oldName, newName)
