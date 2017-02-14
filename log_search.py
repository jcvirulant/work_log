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
        csvfile = open('work_log.csv', 'r')
        search = input('What {} would you like to search?'.format(fieldname))
        reader = csv.DictReader(csvfile)
        for row in reader:
            if search in row[str(fieldname)]:
                print(row)
        if input('Search again? Y/n').lower() == 'y':
            Search()
