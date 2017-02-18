import csv
import datetime
import time
import sys
from task import Task
from log_search import Search

# Must format all inputs --> date task name, duration, etc.

fieldnames = [
            'first_name',
            'last_name',
            'task_name',
            'time_spent',
            'notes',
            'date'
            ]
my_tasks = []
index = 0


def menu():
    global index
    print('Key: '
          '[S]earch, '
          'new [T]ask, '
          '[P]revious, '
          '[N]ext, '
          'or [Q]uit\n'
          )
    print('_' * 50)
    ask = input('Would you like to do? '.lower())
    if ask == 's':
        search = Search()
    elif ask == 't':
        my_tasks.append(new_task())
        print(my_tasks[-1])
        wtf(my_tasks[-1])
    elif ask == 'p':
        if index == 0:
            index = len(my_tasks) - 1
        else:
            index -= 1
    elif ask == 'n':
        if index == len(my_tasks) - 1:
            index = 0
        else:
            index += 1
    elif ask == 'q':
        print('Thank you for using Task Log 3000!')
        sys.exit()
    else:
        print('Invalid request')
        menu()


def sf():  # sf = start_file
    try:
        csvfile = open("work_log.csv", 'x')
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
    except FileExistsError:
        csvfile = open("work_log.csv", 'r')
        reader = csv.DictReader(csvfile)
        for row in reader:
            my_tasks.append(row)


def wtf(task):  # wtf = write to file
    csvfile = open("work_log.csv", 'a')
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writerow(task)
    csvfile.close()


def new_task():
    fmt = ('%m-%d-%y')
    first_name = input("What is your first name? ")
    last_name = input("What is your last name? ")
    task_name = input('What is the task name? ')
    time_spent = input('How mush time was spent? ')
    if input('Was the task done today?') == 'y':
        date = datetime.date.today()
        date = date.strftime(fmt)
    else:
        date = input('What is the task date? (MM-DD-YY) ')
    notes = input('Notes (hit enter to skip)? ')
    my_dict = {
        'first_name': first_name,
        'last_name': last_name,
        'task_name': task_name,
        'time_spent': time_spent,
        'notes': notes,
        'date': date
        }
    return my_dict


def print_task():
    print(
        '\nTask Number: ' + str(index + 1) + '\n'
        'First Name: ' + my_tasks[index]['first_name'] + '\n'
        'Last Name: ' + my_tasks[index]['last_name'] + '\n'
        'Task: ' + my_tasks[index]['task_name'] + '\n'
        'Duration: ' + my_tasks[index]['time_spent'] + '\n'
        'Notes: ' + my_tasks[index]['notes'] + '\n'
        'Date: ' + my_tasks[index]['date'] + '\n'
        )
    print('_' * 50)


print('Welcome to...\n\nTASK LOG 3000!!!!!\n\n')
sf()
index = 0

while True:
    print_task()
    menu()


# create regex search
# Entries can be deleted and edited
    # letting user change the date
    # task name
    # time spent
    # notes
# Entries can be searched for and found based on a date range
