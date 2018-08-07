# Use the 'calendar' module to draw calendars to the console
# https://docs.python.org/3.6/library/calendar.html
#
# Use the sys module to look for command line arguments in the `argv` list
# variable.
#
# If the user specifies two command line arguments, month and year, then draw
# the calendar for that month.

# Stretch goal: if the user doesn't specify anything on the command line, show
# the calendar for the current month. See the 'datetime' module.

# Hint: this should be about 15 lines of code. No loops are required. Read the
# docs for the calendar module closely.

import sys
import calendar
import datetime
#sys.argv[0] is name of program

month = sys.argv[1]
year = sys.argv[2]
print(str( month ) + ", " + str(year))

#if month
sys.stderr.write('This is stderr text \n')
sys.stderr.flush()
print(calendar.setfirstweekday(2))

sys.stdout.write('This is stdout text \n')
print(sys.argv)