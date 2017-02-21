import csv
from datetime import datetime as dt
import time
import sys

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
fmt = ('%m-%d-%y')


def delete_task():
    global index
    if input('Are you sure you want to delete this task? Y/N').lower() == 'y':
        del my_tasks[index]
        index -= 1
    else:
        pass


def edit():
    global index
    print('What aspect of the task would you like to change? ')
    item = input(
                '[T]ask Name, '
                '[D]uration, '
                '[N]otes, '
                '[D]ate, '
                ).lower()
    if item == 't':
        aspect = 'task_name'
    elif item == 'd':
        aspect = 'time_spent'
    elif item == 'n':
        aspect = 'notes'
    else:
        aspect = 'date'
    print('You have chose to modify {}'.format(aspect))
    my_tasks[index][aspect] = input('Enter your changes: ')


def menu():
    global index
    print('Key: '
          '[S]earch, '
          '[E]dit, '
          '[D]elete, '
          'new [T]ask, '
          '[P]revious, '
          '[N]ext, '
          'or [Q]uit\n'
          )
    print('_' * 50)
    ask = input('Would you like to do? '.lower())
    if ask == 's':
        search = search_menu()
    elif ask == 'e':
        edit()
    elif ask == 'd':
        delete_task()
    elif ask == 't':
        my_tasks.append(new_task())
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
        quit()
    else:
        print('Invalid request')
        menu()


def new_task():
    first_name = input("What is your first name? ")
    last_name = input("What is your last name? ")
    task_name = input('What is the task name? ')
    time_spent = input('How mush time was spent? ')
    if input('Was the task done today?') == 'y':
        date = dt.today()
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


def quit():
    csvfile = open("work_log.csv", 'w')
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for item in my_tasks:
        writer.writerow(item)
    csvfile.close()
    sys.exit()


def search_menu():
    menu_select = input('Search by [D]ate, Date [R]ange,'
                        ' or by [T]ask name? ').lower()
    if menu_select == 'd':
        search('date')
    elif menu_select == 'r':
        search_range()
    else:
        search('task_name')


def search(fieldname):
    global index
    search = input('What {} would you like to search?'.format(fieldname))
    for task in my_tasks:
        if search in task[str(fieldname)]:
            index = my_tasks.index(task)
            print_task()
    menu()


def search_range():
    global index
    date1 = dt.strptime(input('From: '), fmt)
    date2 = dt.strptime(input('To: '), fmt)
    for task in my_tasks:
        if date1 <= dt.strptime(task[str('date')], fmt) <= date2:
            index = my_tasks.index(task)
            print_task()
    menu()


def sf():  # sf = start_file
    try:
        csvfile = open("work_log.csv", 'x')
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        print('Please create a new task to start!')
        my_tasks.append(new_task())
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


print('Welcome to...\n\nTASK LOG 3000!!!!!\n\n')
sf()
index = 0

while True:
    print_task()
    menu()


# create regex search

# Entries can be searched for and found based on a date range
