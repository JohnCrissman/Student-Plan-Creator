import csv


class Display:

    def __init__(self, solutions, student):
        self.filepath = student.filepath.replace(student.filename, 'sol_'+student.filename).replace('.txt', '.csv')
        self.semester = student.semester
        self.year = student.year
        self.solutions = solutions
        self.list_of_semesters = ["FALL", "SPRING", "SUMMER"]

        with open(self.filepath, 'w') as writer:
            self.writer = csv.writer(writer)
            for sol in self.solutions:
                self.generate_output_csv(sol)
                self.generate_output_console(sol)
            print('Your solutions are stored in the resource folder under the')
            print('following name: sol_'+student.filename.replace('.txt', '.csv'))

    def generate_output_console(self, solution):
        temp_list = []
        dash = '-' * 55
        val1 = ','.join(self.list_of_semesters[:1])
        val2 = ','.join(self.list_of_semesters[1:2])
        val3 = ','.join(self.list_of_semesters[2:3])
        year = self.year
        semester = self.semester
        print(dash)
        print("{:<22} {:<10}".format('Semesters', 'Classes'))
        print(dash)

        for keys, values in sorted(solution.items()):
            temp_list.append(values)

        if semester == val1:
            print(val1 + "/" + year + '   : {:>5}'.format("") + '{}'.format(temp_list[:3]))
            x = int(year) + 1
            year = str(x)
            print(val2 + "/" + year + ' : {:>5}'.format("") + '{}'.format(temp_list[3:6]))
            print(val3 + "/" + year + ' : {:>5}'.format("") + '{}'.format(temp_list[6:9]))
            print(val1 + "/" + year + '   : {:>5}'.format("") + '{}'.format(temp_list[9:12]))

        if semester == val2:
            print(val2 + "/" + year + ' : {:>5}'.format("") + '{}'.format(temp_list[:3]))
            print(val3 + "/" + year + ' : {:>5}'.format("") + '{}'.format(temp_list[3:6]))
            print(val1 + "/" + year + '   : {:>5}'.format("") + '{}'.format(temp_list[6:9]))
            x = int(year) + 1
            year = str(x)
            print(val2 + "/" + year + ' : {:>5}'.format("") + '{}'.format(temp_list[9:12]))

        if semester == val3:
            print(val3 + "/" + year + ' : {:>5}'.format("") + '{}'.format(temp_list[:3]))
            print(val1 + "/" + year + '   : {:>5}'.format("")  + '{}'.format(temp_list[3:6]))
            x = int(year) + 1
            year = str(x)
            print(val2 + "/" + year + ' : {:>5}'.format("") + '{}'.format(temp_list[6:9]))
            print(val3 + "/" + year + ' : {:>5}'.format("") + '{}'.format(temp_list[9:12]))
        print('\n')

    def generate_output_csv(self, solution):
        temp_list =[]
        dash = '-' * 50
        val1 = ','.join(self.list_of_semesters[:1])
        val2 = ','.join(self.list_of_semesters[1:2])
        val3 = ','.join(self.list_of_semesters[2:3])
        year = self.year
        semester = self.semester

        self.writer.writerow([dash])
        self.writer.writerow(["{:<20} {:<5}".format('Semesters', 'Classes')])
        self.writer.writerow([dash])
        for keys, values in sorted(solution.items()):
            temp_list.append(values)

        if semester == val1:
            self.writer.writerow([val1 + "/" + year + '   : {:>5}'.format("") + '{}'.format(temp_list[:3])])
            x = int(year) + 1
            year = str(x)
            self.writer.writerow([val2 + "/" + year + ' : {:>5}'.format("") + '{}'.format(temp_list[3:6])])
            self.writer.writerow([val3 + "/" + year + ' : {:>5}'.format("") + '{}'.format(temp_list[6:9])])
            self.writer.writerow([val1 + "/" + year + '   : {:>5}'.format("") + '{}'.format(temp_list[9:12])])
        if semester == val2:
            self.writer.writerow([val2 + "/" + year + ' : {:>5}'.format("") + '{}'.format(temp_list[:3])])
            self.writer.writerow([val3 + "/" + year + ' : {:>5}'.format("") + '{}'.format(temp_list[3:6])])
            self.writer.writerow([val1 + "/" + year + '   : {:>5}'.format("") + '{}'.format(temp_list[6:9])])
            x = int(year) + 1
            year = str(x)
            self.writer.writerow([val2 + "/" + year + ' : {:>5}'.format("") + '{}'.format(temp_list[9:12])])

        if semester == val3:
            self.writer.writerow([val3 + "/" + year + ' : {:>5}'.format("") + '{}'.format(temp_list[:3])])
            self.writer.writerow([val1 + "/" + year + '   : {:>5}'.format("") + '{}'.format(temp_list[3:6])])
            x = int(year) + 1
            year = str(x)
            self.writer.writerow([val2 + "/" + year + ' : {:>5}'.format("") + '{}'.format(temp_list[6:9])])
            self.writer.writerow([val3 + "/" + year + ' : {:>5}'.format("") + '{}'.format(temp_list[9:12])])

        self.writer.writerow(['\t'])
        self.writer.writerow(['\t'])

