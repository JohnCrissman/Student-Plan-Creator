# do your imports here
from py.CSP import CSP
from py.Backtracking import Backtracking
from py.Student import Student
from py.CoursesOffered import CoursesOffered


def main():
    print("\n====================================================== John Test\n")
    filename_fall_2019 = "fall_2019.txt"
    filename_fall_2008 = "fall_2008.txt"
    filename_spring_2019 = "spring_2019.txt"
    filename_spring_2008 = "spring_2008.txt"
    filename_summer_2019 = "summer_2019.txt"
    filename_summer_2008 = "summer_2008.txt"

    student_fall_2019 = Student(filename_fall_2019)
    student_fall_2008 = Student(filename_fall_2008)
    student_spring_2019 = Student(filename_spring_2019)
    student_spring_2008 = Student(filename_spring_2008)
    student_summer_2019 = Student(filename_summer_2019)
    student_summer_2008 = Student(filename_summer_2008)


    courses_offered_fall_2019 = CoursesOffered(student_fall_2019)
    courses_offered_fall_2008 = CoursesOffered(student_fall_2008)
    courses_offered_spring_2019 = CoursesOffered(student_spring_2019)
    courses_offered_spring_2008 = CoursesOffered(student_spring_2008)
    courses_offered_summer_2019 = CoursesOffered(student_summer_2019)
    courses_offered_summer_2008 = CoursesOffered(student_summer_2008)

    csp_fall_2019 = CSP(courses_offered_fall_2019)
    csp_fall_2008 = CSP(courses_offered_fall_2008)
    csp_spring_2019 = CSP(courses_offered_spring_2019)
    csp_spring_2008 = CSP(courses_offered_spring_2008)
    csp_summer_2019 = CSP(courses_offered_summer_2019)
    csp_summer_2008 = CSP(courses_offered_summer_2008)

    print("\nDomain for Fall 2019: \n", csp_fall_2019.domains)
    print("\nDomain for Fall 2008: \n", csp_fall_2008.domains)
    print("\nDomain for Spring 2019: \n", csp_spring_2019.domains)
    print("\nDomain for Spring 2008: \n", csp_spring_2008.domains)
    print("\nDomain for Summer 2019: \n", csp_summer_2019.domains)
    print("\nDomain for Summer 2008: \n", csp_summer_2008.domains)


    # csp = CSP(courses_offered)
    #
    # print("here are the domains")
    # print(csp.domains)
    # bt = Backtracking(csp)
    # bt.backtracking_algorithm()

if __name__ == '__main__':
    main()
