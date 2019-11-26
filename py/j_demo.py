# do your imports here
from py.CSP import CSP
from py.Backtracking import Backtracking
from py.Student import Student
from py.CoursesOffered import CoursesOffered


def main():
    print("\n====================================================== John Test\n")
    filename = "j_info.txt"

    student = Student(filename)
    courses_offered = CoursesOffered(student)
    csp = CSP(courses_offered)

    print("here are the domains")
    print(csp.domains)
    bt = Backtracking(csp)
    bt.backtracking_algorithm()

if __name__ == '__main__':
    main()
