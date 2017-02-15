import csv
import datetime
import sys
from log_search import Search

# Must format all inputs --> date task name, duration, etc.

fieldnames = [
            'first_name', 'last_name', 'task_name',
            'time_spent', 'notes', 'date'
            ]


class Log:
    def __init__(self):
        print('Welcome to...\n\nTASK LOG 3000!!!!!\n\n')
        self.first_name = input("What is your first name? ")
        self.last_name = input("What is your last name? ")
        sf()

    def menu():
        ask = input('Would you like to [S]earch,'
                    ' [N]ew task, or [Q]uit? '.lower())
        if ask == 's':
            search = Search()
        elif ask == 'n':
            wtf()
        else:
            print('Thank you for using Task Log 3000!')
            sys.exit()

    def sf():  # sf = start_file
        try:
            csvfile = open("work_log.csv", 'x')
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
        except FileExistsError:
            pass


while True:
    menu()


# Create search based on date
# Create search based on string
# either as a regular expression or a plain text search.
# Print a report of this information to the screen
    # including the date
    # title of task
    # time spent
    # and general notes.


# Menu has a “quit” option to exit the program.
# Entries can be deleted and edited
    # letting user change the date
    # task name
    # time spent
    # notes
# Entries can be searched for and found based on a date range
# Entries are displayed one at a time with the ability to page through records
    # (previous/next/back).
