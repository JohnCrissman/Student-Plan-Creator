from random import randrange
from py.Backtracking import Backtracking
# from py.m_CSP import CSP
from py.CSP import CSP
from py.CoursesOffered import CoursesOffered
from py.Student import Student

def dict_with_random_values(keys):
    my_dictionary = dict()
    for key in keys:
        my_dictionary[key] = randrange(10)
    print("dict: ", my_dictionary)
    return my_dictionary


def generate_new_csp(keys):
    legal_moves = dict_with_random_values(keys)
    num_constraints = dict_with_random_values(keys)
    affect_neighbors = dict_with_random_values(keys)
    return legal_moves, num_constraints, affect_neighbors


def main():
    filename = "j_info.txt"
    st = Student(filename)
    co = CoursesOffered(st)
    csp = CSP(co)
    bt = Backtracking(csp)

    # dom = {"mari": ["CS400"],
    #        # "valor": ["CS404"],
    #        # "thing": ["CS331", "CS345", "CS355", "CS442", "CS460"],
    #        "word": ["CS401", "CS411", "CS412", "CS413"],
    #        "maps": ["CS335", "CS415", "CS416", "CS419", "CS400"]
    #        }
    # keys = ["mari", "valor", "thing", "word", "maps"]
    # dic_legal_moves = {'mari': 2, 'valor': 2, 'thing': 2, 'word': 2, 'maps': 8}

    # print("\n====================================================== MRV Degree Alpha\n")
    # num_constraints = {'mari': 14, 'valor': 1, 'thing': 14, 'word': 7, 'maps': 3}
    # dic_legal_moves = {key: len(value) for key, value in csp.domains.items()}
    # print(dic_legal_moves)
    # selected_variable = bt.mrv_degree_alpha(dic_legal_moves, num_constraints)
    # print(selected_variable)

    # Given the assignment
    # print("\n====================================================== UPDATE CSP\n")
    # assign = {"thing": "CS355", "valor": "CS401"}
    # new_var, new_dom = bt.get_csp_updated_so_far(assign)

    # for the LCV
    # print("\n====================================================== LCV\n")
    # bt.order_domain_variables(selected_variable, assign, csp)

    print("\n====================================================== BACKTRACKING\n")
    solution = bt.backtracking_algorithm_first_n_solution(3)
    print(solution)
    if solution is not None:
        print(solution)
        print(len(solution))
        solution
        for k, v in sorted(solution.items()):
            print(k, v)
    print("\n\nAll solutions are: ", len(bt.all_solutions))


if __name__ == '__main__':
    main()
