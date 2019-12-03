from py.CSP import CSP
from py.Backtracking import Backtracking
import csv


class Display:

    # TODO: read the text file

    def __init__(self, solutions, filename):
        # self.filename = filename  # n_info.txt
        # self.semester = ""
        # self.year = ""
        # self.number_of_classes = ""
        # self.list_of_classes = []
        # self.load()
        self.solutions = solutions

        with open('../resources/' + filename, 'w', newline='') as csv_file:
            self.writer = csv.writer(csv_file)
            # self.writer = self.open_csv_file('n_schedule.csv')
            for sol in self.solutions:
                # print("Naz")
                self.generate_output_csv(sol)
                self.generate_output(sol)

    def generate_output(self, solution):
        print("semester" + ":" + "class")
        for keys, values in solution.items():
            print(keys + ": " + values)
        print('\n')

    def generate_output_csv(self, solution):
        for key, value in solution.items():
           self.writer.writerow([key + ": " + value])

        self.writer.writerow(['\t'])
