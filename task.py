import csv
import datetime

my_dict = {}


class Task(object):
    """Task the object for each individual task that is created."""

    def __init__(self):
        fmt = ('%m-%d-%y')
        self.first_name = input("What is your first name? ")
        self.last_name = input("What is your last name? ")
        self.task_name = input('What is the task name? ')
        self.time_spent = input('How mush time was spent? ')
        if input('Was the task done today?') == 'y':
            self.date = datetime.date.today()
            self.date = self.date.strftime(fmt)
        else:
            self.date = input('What is the task date? (MM-DD-YY) ')
        self.notes = input('Notes (hit enter to skip)? ')
        self.my_dict = {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'task_name': self.task_name,
            'time_spent': self.time_spent,
            'notes': self.notes,
            'date': self.date
            }
