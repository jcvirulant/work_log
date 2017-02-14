import csv
import datetime
import sys
from log_search import Search

# Must format all inputs --> date task name, duration, etc.

fieldnames = [
            'first_name', 'last_name', 'task_name',
            'time_spent', 'notes', 'date'
            ]


def task_info():
    fmt = ('%m-%d-%y')
    task_name = input('What is the task name? ')
    time_spent = input('How mush time was spent? ')
    if input('Was the task done today?') == 'y':
        date = datetime.date.today()
        date = date.strftime(fmt)
    else:
        date = input('What is the task date? (MM-DD-YY) ')
    notes = input('Notes (hit enter to skip)? ')
    my_list = [first_name, last_name, task_name, time_spent, notes, date]
    my_dict = {
            'first_name': first_name,
            'last_name': last_name,
            'task_name': task_name,
            'time_spent': time_spent,
            'notes': notes,
            'date': date
            }
    return my_dict


def menu():
    ask = input('Would you like to [S]earch, [N]ew task, or [Q]uit? '.lower())
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


def wtf():  # wtf = write to file
    csvfile = open("work_log.csv", 'a')
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writerow(task_info())
    csvfile.close()


print('Welcome to...\n\nTASK LOG 3000!!!!!\n\n')
my_dict = {}
first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
sf()

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
