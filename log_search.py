import re
import csv
import time


class Search:
    fmt = ('%m-%d-%y')

    def __init__(self):
        self.row_num = 0
        self.print_task(self.row_num)
        self.menu()

    def search_menu(self):
        menu_select = input('Search by [D]ate, date [R]ange'
                            ' or Search by [T]ask name? ').lower()
        elif menu_select == 'd':
            self.rff('date')
        elif menu_select == 'r':
            pass
        else:
            self.rff('task_name')

        def date_search(self):



    # def rff(self, fieldname):  # rff = read from file
    #     count = 0
    #     csvfile = open('work_log.csv', 'r')
    #     search = input('What {} would you like to search?'.format(fieldname))
    #     reader = csv.DictReader(csvfile)
    #     for row in reader:
    #         if search in row[str(fieldname)]:
    #             count += 1
    #             print(
    #                 '\n\nFirst Name: ' + row['first_name'] + '\n'
    #                 'Last Name: ' + row['last_name'] + '\n'
    #                 'Task: ' + row['task_name'] + '\n'
    #                 'Duration: ' + row['time_spent'] + '\n'
    #                 'Notes: ' + row['notes'] + '\n'
    #                 'Date: ' + row['date'] + '\n'
    #                 )
    #             print('_' * 50)
    #     if count == 0:
    #         print('No results found')
    #     if input('\n\nSearch again? Y/n').lower() == 'y':
    #         Search()

    def print_task(self, num):
        count = 0
        csvfile = open('work_log.csv', 'r')
        reader = csv.DictReader(csvfile)
        for row in reader:
            if count == num:
                print(
                    '\n\nFirst Name: ' + row['first_name'] + '\n'
                    'Last Name: ' + row['last_name'] + '\n'
                    'Task: ' + row['task_name'] + '\n'
                    'Duration: ' + row['time_spent'] + '\n'
                    'Notes: ' + row['notes'] + '\n'
                    'Date: ' + row['date'] + '\n'
                    )
                print('_' * 50)
                count += 1
            else:
                count += 1

    def delete_task(self):
        pass

    def edit_task(self):
        pass
