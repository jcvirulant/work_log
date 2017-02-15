import re
import csv


class Search:
    fmt = ('%m-%d-%y')

    def __init__(self):
        if input('Search by [D]ate or [T]ask name? ').lower() == 'd':
            self.rff('date')
        else:
            self.rff('task_name')

    def rff(self, fieldname):  # rff = read from file
        count = 0
        csvfile = open('work_log.csv', 'r')
        search = input('What {} would you like to search?'.format(fieldname))
        reader = csv.DictReader(csvfile)
        for row in reader:
            if search in row[str(fieldname)]:
                count += 1
                print(
                    '\n\nFirst Name: ' + row['first_name'] + '\n'
                    'Last Name: ' + row['last_name'] + '\n'
                    'Task: ' + row['task_name'] + '\n'
                    'Duration: ' + row['time_spent'] + '\n'
                    'Notes: ' + row['notes'] + '\n'
                    'Date: ' + row['date'] + '\n'
                    )
                print('_' * 50)
        if count == 0:
            print('No results found')
        if input('\n\nSearch again? Y/n').lower() == 'y':
            Search()
