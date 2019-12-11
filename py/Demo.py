from py.Backtracking import Backtracking
from py.CSP import CSP
from py.Student import Student
from py.Display import Display


class Demo:
    def __init__(self, filename):
        self.student = Student(filename)
        self.csp = CSP(self.student)
        self.solutions = []
        self.__compute_student_plans()
        self.__show_results()

    def __compute_student_plans(self):
        bt = Backtracking(self.csp)
        bt.backtracking_algorithm_all_solutions()
        print('-- end of execution and debugging messages... \n\n\n\n\n')
        self.solutions = bt.all_solutions

    def __show_results(self):
        print('******************************************************\n')
        print('-----------------       RESULTS      -----------------\n')
        print('******************************************************\n')
        size = len(self.solutions)
        if size > 0:
            print('\nWe calculated ', size, ' solutions.  You will be shown\nthree of them.\n')
            solutions = [self.solutions[0], self.solutions[int(size / 2)], self.solutions[size - 1]]
            d = Display(solutions, self.student)
        else:
            print('Ohh! :( \nThere is no solution for the specified file.')


def handle_file_not_found(file):
    print('\nNOTE: The file (' + file + ') that you specified was not found.\n')
    print('Please make sure that your file is in the resource folder. In addition,')
    print('please make sure your file has the following structure:')
    # print('')
    print('|\t_____[FALL, SUMMER, SPRING] \t\t\t<-- The semester in which you plan to start classes')
    print('|\t_____[2020, 2021, 2022]\t\t\t<-- The year in which you intend to staRt classes')
    print('|\t_____[0, 2, 4]\t\t\t<--  Number of classes that have already been taken (Not needed for the MVP)')
    print('------------------ example.txt ------------------')
    print('|\tFALL')
    print('|\t2020')
    print('|\t0')


def main():

    filename = input('Please enter the name of the file to read: ')

    try:
        demo = Demo(filename)
    except FileNotFoundError:
        handle_file_not_found(filename)

    print("\n\n\t-- Thank you for using our app.")
    print("\t-- Artificial Brain! :)")


if __name__ == '__main__':
    main()
