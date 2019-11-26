# do your imports here
from py.CSP import CSP
from py.Backtracking import Backtracking
from py.Student import Student
from py.CoursesOffered import CoursesOffered


def main():
    # write your code here
    # test your stuff here
    print("Hi john!")
    # John test
    j = Backtracking()
    print("\n====================================================== John Test\n")
    filename = "j_info.txt"

    student = Student(filename)
    courses_offered = CoursesOffered(student)
    print(courses_offered.get_semesters())
    courses_offered.get_domain_for_variables()

    csp = CSP(courses_offered)
    print("here are the domains")
    print(csp.domains)


if __name__ == '__main__':
    main()
