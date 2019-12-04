from py.CSP import CSP
from py.Backtracking import Backtracking
from py.Student import Student
import csv


class Display:

    def __init__(self, solutions, filename):
        # self.filename = filename  # n_info.txt
        self.semester = ""
        self.year = ""
        # self.number_of_classes = ""
        # self.list_of_classes = []
        self.solutions = solutions
        self.list = []
        self.list_of_semesters = ["Fall", "Spring", "Summer"]
        #self.load()

        #with open('../resources/' + filename, 'w', newline='') as csv_file:
            #self.writer = csv.writer(csv_file)
            # 33self.writer = self.open_csv_file('n_schedule.csv')
            #for sol in self.solutions:
                # print("Naz")
                #self.generate_output_csv(sol)
                #self.generate_output(sol)

        d_path = '../resources/n_info.txt'
        d_r_path = '../resources/n_schedule.csv'
        with open(d_path, 'r') as reader, open(d_r_path, 'w') as writer:
            content = reader.readlines()
            content = [x.rstrip() for x in content]
            self.semester = content.pop(0)
            self.year = content.pop(0)
            # print(self.semester)
            # print(self.year)
            self.writer = csv.writer(writer)
            for sol in self.solutions:
                self.generate_output_csv(sol)
                self.generate_output(sol)

    def generate_output(self, solution):
        dash = '-' * 55
        val1 = ','.join(self.list_of_semesters[:1])
        val2 = ','.join(self.list_of_semesters[1:2])
        val3 = ','.join(self.list_of_semesters[2:3])
        year = self.year
        semester = self.semester
        print(dash)
        print("{:<22} {:<10}".format('Semesters', 'Classes'))
        print(dash)

        for keys, values in solution.items():
            self.list.append(values)

        if semester == val1:
            print(val1 + "/" + year + '   : {:>5}'.format("") + '{}'.format(self.list[:3]))
            x = int(year) + 1
            year = str(x)
            print(val2 + "/" + year + ' : {:>5}'.format("") + '{}'.format(self.list[3:6]))
            print(val3 + "/" + year + ' : {:>5}'.format("") + '{}'.format(self.list[6:9]))
            print(val1 + "/" + year + '   : {:>5}'.format("") + '{}'.format(self.list[9:12]))

        if semester == val2:
            print(val2 + "/" + year + ' : {:>5}'.format("") + '{}'.format(self.list[:3]))
            print(val3 + "/" + year + ' : {:>5}'.format("") + '{}'.format(self.list[3:6]))
            print(val1 + "/" + year + '   : {:>5}'.format("") + '{}'.format(self.list[6:9]))
            x = int(year) + 1
            year = str(x)
            print(val2 + "/" + year + ' : {:>5}'.format("") + '{}'.format(self.list[9:12]))

        if semester == val3:
            print(val3 + "/" + year + ' : {:>5}'.format("") + '{}'.format(self.list[:3]))
            print(val1 + "/" + year + '   : {:>5}'.format("")  + '{}'.format(self.list[3:6]))
            x = int(year) + 1
            year = str(x)
            print(val2 + "/" + year + ' : {:>5}'.format("") + '{}'.format(self.list[6:9]))
            print(val3 + "/" + year + ' : {:>5}'.format("") + '{}'.format(self.list[9:12]))


        #print(self.semester + self.year + ': {}'.format(self.list[:3]))
        #print('Semester/year: {}'.format(self.list[3:6]))
        #print('Semester/year: {}'.format(self.list[6:9]))
        #print('Semester/year: {}'.format(self.list[9:12]))
        # print(self.list[:3])
        # print(self.list[3:6])
        # print(self.list[6:9])
        # print(self.list[9:12])
        # print(['{:<1}'.format(item) for item in self.list[:3]])
        print('\n')

    def generate_output_csv(self, solution):
        dash = '-' * 50
        val1 = ','.join(self.list_of_semesters[:1])
        val2 = ','.join(self.list_of_semesters[1:2])
        val3 = ','.join(self.list_of_semesters[2:3])
        year = self.year
        semester = self.semester

        self.writer.writerow([dash])
        self.writer.writerow(["{:<20} {:<5}".format('Semesters', 'Classes')])
        self.writer.writerow([dash])
        # for key, value in solution.items():
           # self.writer.writerow([key + ": " + value])

        for keys, values in solution.items():
            self.list.append(values)

        if semester == val1:
            self.writer.writerow([val1 + "/" + year + '   : {:>5}'.format("") + '{}'.format(self.list[:3])])
            x = int(year) + 1
            year = str(x)
            self.writer.writerow([val2 + "/" + year + ' : {:>5}'.format("") + '{}'.format(self.list[3:6])])
            self.writer.writerow([val3 + "/" + year + ' : {:>5}'.format("") + '{}'.format(self.list[6:9])])
            self.writer.writerow([val1 + "/" + year + '   : {:>5}'.format("") + '{}'.format(self.list[9:12])])
        if semester == val2:
            self.writer.writerow([val2 + "/" + year + ' : {:>5}'.format("") + '{}'.format(self.list[:3])])
            self.writer.writerow([val3 + "/" + year + ' : {:>5}'.format("") + '{}'.format(self.list[3:6])])
            self.writer.writerow([val1 + "/" + year + '   : {:>5}'.format("") + '{}'.format(self.list[6:9])])
            x = int(year) + 1
            year = str(x)
            self.writer.writerow([val2 + "/" + year + ' : {:>5}'.format("") + '{}'.format(self.list[9:12])])

        if semester == val3:
            self.writer.writerow([val3 + "/" + year + ' : {:>5}'.format("") + '{}'.format(self.list[:3])])
            self.writer.writerow([val1 + "/" + year + '   : {:>5}'.format("") + '{}'.format(self.list[3:6])])
            x = int(year) + 1
            year = str(x)
            self.writer.writerow([val2 + "/" + year + ' : {:>5}'.format("") + '{}'.format(self.list[6:9])])
            self.writer.writerow([val3 + "/" + year + ' : {:>5}'.format("") + '{}'.format(self.list[9:12])])

        # self.writer.writerow(self.list[:3])
        # self.writer.writerow(self.list[3:6])
        # self.writer.writerow(self.list[6:9])
        # self.writer.writerow(self.list[9:12])
        # self.writer.writerow(['\t'])
        # self.writer.writerow(['Semester/year: {}'.format(self.list[:3])])
        # self.writer.writerow(['Semester/year: {}'.format(self.list[3:6])])
        # self.writer.writerow(['Semester/year: {}'.format(self.list[6:9])])
        # self.writer.writerow(['Semester/year: {}'.format(self.list[9:12])])
        self.writer.writerow(['\t'])
        self.writer.writerow(['\t'])

