# do your imports here
from py.CSP import CSP
from py.Backtracking import Backtracking
from py.Student import Student
from py.CoursesOffered import CoursesOffered


def main():
    # filename = "fall_2008.txt"
    # filename = "fall_2019.txt"
    filename = "spring_2008.txt"
    # filename = "spring_2019.txt"
    # filename = "summer_2019.txt"
    # filename = "summer_2008.txt"
    st = Student(filename)
    co = CoursesOffered(st)
    csp = CSP(co)
    bt = Backtracking(csp)

    print("\n====================================================== BACKTRACKING\n")
    # solution = bt.backtracking_algorithm_first_n_solution(3)
    # solution = bt.backtracking_algorithm_all_solutions()
    solution = bt.backtracking_algorithm_one_solution()
    print(solution)
    if solution is not None:
        print(solution)
        print(len(solution))
        solution
        for k, v in sorted(solution.items()):
            print(k, v)
    print("\n\nAll solutions are: ", len(bt.all_solutions))

    print(bt.all_solutions)



if __name__ == '__main__':
    main()
