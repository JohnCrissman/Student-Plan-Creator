from py.Backtracking import Backtracking
from py.CSP import CSP
from py.Student import Student
from py.CoursesOffered import CoursesOffered
from py.Display import Display


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
    #    this main should use the classs created to generate the student's plan
    file = input('Please enter the name of the file to read: ')
    try:
        student = Student(file)
        # load the courses offered starting on the semester the student desires to start
        courses_offered = CoursesOffered(student)
        # create the CSP with the courses offered
        csp = CSP(courses_offered)

        # create a backtracking object
        bt = Backtracking(csp)
        bt.backtracking_algorithm_all_solutions()
        all_solutions = bt.all_solutions
        size = len(all_solutions)
        # solutions = []
        print('********************************************')
        if size > 0:
            solutions = [all_solutions[0], all_solutions[int(size / 2)], all_solutions[size - 1]]
            # print(solutions[0])
            # print(solutions[1])
            # print(solutions[2])
            d = Display(solutions, student)
        else:
            print('Ohh! :( \nThere is no solution for the specified file.')

    except FileNotFoundError:
        handle_file_not_found(file)

    print("\n\n\t-- Thank you for using our app.")
    print("\t-- Artificial Brain! :)")


if __name__ == '__main__':
    main()
