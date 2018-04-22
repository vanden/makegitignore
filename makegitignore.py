#!/usr/bin/env python3

# makegititnore.py: python program to generate gitignore files
#
# Copyright (C) 2018 Brian van den Broek vanden@gmail.com

# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option)
# any later version.

# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for
# more details.

# You should have received a copy of the GNU General Public License along with
# this program. If not, see <https://www.gnu.org/licenses/>.


"""A simple script to create default .gitignore files with a few command
line arguments to select among various suites to include.
"""

import argparse
import os
import sys

FPATH = os.path.join(os.getcwd(), '.gitignore')

# FixMe Do it right (don't want to look up, now)
PROGNAME = "makegitignore"
__version__ = "0.2.2"
PROGREPO = "https://github.com/vanden/makegitignore"


parser = argparse.ArgumentParser(
    description='Generates a .gitignore file',
    epilog='''
If no options are specified, all of the various suites are included in the
generated .gitignore. If options are specified, only the specified suites
are included.''')

parser.add_argument('-e', '--emacs', action="store_true", default=False,
                    help='include a suite to ignore various emacs artifacts')
parser.add_argument('-l', '--latex', action="store_true", default=False,
                    help='include a suite to ignore various latex artifacts')
parser.add_argument('-p', '--python', action="store_true", default=False,
                    help='include a suite to ignore various python artifacts')

args = vars(parser.parse_args())

# Needs to come after parsing arguments, lest it be impossible to run the
# --help with a present .gitignore
#
if os.path.isfile(FPATH):
    print(f"A .gitignore exists at {FPATH} already. Exiting.")
    sys.exit()



if not any(args.values()):
    for key in args.keys():
        args[key] = True


git_ignore_content = [f"""
# This .gitignore file was initially generated by {PROGNAME} v.{__version__}.
# The repositiory for {PROGNAME} is {PROGREPO}.\n
"""]


EMACS = """## emacs Stuff
auto/
\#*\#
.\#*

"""


PYTHON = """## python stuff
*.pyc
__pycache__/

"""

LATEX = """## LaTeX Stuff
*.aux
*.log
*.out
*.pdf
*.toc

"""

FLAGS_AND_CHUNKS = [
    ('emacs', EMACS),
    ('latex', LATEX),
    ('python', PYTHON),
]

for flag, chunk in FLAGS_AND_CHUNKS:
    if args[flag]:
        git_ignore_content.append(chunk)


with open(FPATH, 'w') as ignoreFile:
    ignoreFile.write('\n'.join(git_ignore_content))
