Holding pattern entry mode calculator / tester
==============================================

A small script that will let you either practice your holding pattern entry modes, or tell you which entry mode to use.

This script is distributed in the hope that it will be useful but without implied or expressed warranties, including, but not limited to, any implied warranty of fitness for a particular purpose.

***************************************************************

DO NOT USE FOR REAL WORLD AVIATION. Seriously. Don't.

***************************************************************


Using on Windows
================

The release zipfile includes everything you'll need.

  1. download and extract (the rest of this mini-guide assumes you've extracted in your Downloads directory).

  2. Start a command prompt:

        Start -> Run -> cmd<enter> or, 
        on Windows 10: Start -> cmd<enter>

  3. Navigate to the extracted folder.

        cd Downloads\holding-pattern-win\

  4. Run the applicaton. The --help argument will give a basic explanation of your options (but see below for a more detailed explanation)

        python.exe main.py --help


What it does
============

Quiz mode
---------

Quiz mode will default to 5 questions:

    ~ python3 main.py quiz

But you can override that and go as many rounds as you like:

    ~ python3 main.py quiz --questions 11

It will give you a situation:

    --------------------------------------------------------------------------------
    Question 1
    --------------------------------------------------------------------------------
    Choose entry method for holding on radial 193 with right turn and arriving on course 331.
      1 DIRECT
      2 PARALLEL
      3 TEARDROP
    Your answer? 

You answer by entering the number of your choice and pressing Enter. It will then tell you whether you are correct, and what the right answer was if you made a mistake.

Calc mode
---------

For calc mode, you give it the parameters of the holding pattern and it will tell you which entry to use:

    python3 main.py calc --inbound <INBOUND COURSE> --holding-radial <HOLDING RADIAL> --turn <right or left, defaults to right>

An example:

    ~ python3 main.py calc --inbound 38 --holding-radial 10
    Use a PARALLEL entry

Choices with regards to edge cases:
-----------------------------------

When approaching on a course that is exactly on the edge for a direct entry, the script will choose a direct entry (and the quiz will expect it as well).
When approaching on a course that is exactly the reciprocal of the holding pattern radial, the script will choose a parallel entry (and the quiz will expect it as well).


Testing
=======

Set up a virtualenv and install the test dependencies (aka pytest)

    virtualenv venv
    venv/bin/pip install -r requirements.txt

Run the tests

    venv/bin/pytest test.py
