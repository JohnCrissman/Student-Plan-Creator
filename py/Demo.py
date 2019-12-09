from py.Backtracking import Backtracking
from py.CSP import CSP
from py.Student import Student
from py.CoursesOffered import CoursesOffered
from py.Display import Display


def main():
    #    this main should use the classs created to generate the student's plan
    #
    print('hello from main')
    student = Student("fall_2008.txt")

    courses_offered = CoursesOffered(student)

    csp = CSP(courses_offered)

    bt = Backtracking(csp)
    bt.backtracking_algorithm_first_n_solution(3)
    solutions = bt.all_solutions
    print('********************************************')
    d = Display(solutions)


if __name__ == '__main__':
    main()
