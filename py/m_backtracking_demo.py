from random import randrange
from py.Backtracking import Backtracking


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
    bt = Backtracking()

    dom = {"mari": ["CS400"],
           "valor": ["CS404"],
           "thing": ["CS331", "CS345", "CS355", "CS442", "CS460"],
           "word": ["CS401", "CS411", "CS412", "CS413"],
           "maps": ["CS335", "CS415", "CS416", "CS419"]
           }
    keys = ["mari", "valor", "thing", "word", "maps"]
    num_constraints = {'mari': 14, 'valor': 1, 'thing': 14, 'word': 7, 'maps': 3}

    # dic_legal_moves = {'mari': 2, 'valor': 2, 'thing': 2, 'word': 2, 'maps': 8}
    dic_legal_moves = {key: len(value) for key, value in dom.items()}
    print(dic_legal_moves)
    selected_variable = bt.mrv_degree_alpha(dic_legal_moves, num_constraints)
    print(selected_variable)

    # Given the assignment
    print("\n======================================================\n")
    assign = {"mari": "CS355", "valor": "CS401"}
    new_var, new_dom = bt.get_csp_updated_so_far(assign)

    # for the LCV
    affect_neighbors = {'mari': 2, 'valor': 9, 'thing': 3, 'word': 2, 'maps': 3}


if __name__ == '__main__':
    main()











# assignment0 = {"A1": 7,
#               "A2": 8,
#               "A3": 9,
#               "B1": 8,
#               "B2": 7,
#               "B3": 9,
#               "C1": None,
#               "C2": None,
#               "C3": 7
#               }
# assignment1 = {"A1": 7,
#               "A2": 7,
#               "A3": 8,
#               "B1": 8,
#               "B2": 9,
#               "B3": 7,
#               "C1": None,
#               "C2": None,
#               "C3": 9
#               }
# assignment2 = {"A1": None,
#               "A2": None,
#               "A3": None,
#               "B1": 7,
#               "B2": 8,
#               "B3": 9,
#               "C1": 7,
#               "C2": None,
#               "C3": 8
#               }
# assignment3 = {"A1": 1,
#               "A2": 2,
#               "A3": 3,
#               "B1": None,
#               "B2": None,
#               "B3": 9,
#               "C1": 2,
#               "C2": 8,
#               "C3": 1
#               }
# assignment4 = {"A1": None,
#               "A2": None,
#               "A3": None,
#               "B1": None,
#               "B2": None,
#               "B3": None,
#               "C1": None,
#               "C2": None,
#               "C3": None
#               }
# num_constraints = {"A1": 4, "A2": 4, "A3": 4,
#                    "B1": 4, "B2": 4, "B3": 4,
#                    "C1": 4, "C2": 4, "C3": 4}



# csp0 = Backtracking(assignment0, num_constraints)
# csp1 = Backtracking(assignment1, num_constraints)
# csp2 = Backtracking(assignment2, num_constraints)
# csp3 = Backtracking(assignment3, num_constraints)
# csp4 = Backtracking(assignment4, num_constraints)

# print("testing whether assignments are consistent:")
# print(csp0.isAssigConsistent(assignment0)) ## true
# print(csp1.isAssigConsistent(assignment1)) ## false
# print(csp2.isAssigConsistent(assignment2)) ## false
# print(csp3.isAssigConsistent(assignment3)) ## true
# print(csp4.isAssigConsistent(assignment4)) ## true
#
# print("\ntesting whether assignments are complete and consistent!")
# print(csp0.isAssigComplete(assignment0)) ## false
# print(csp1.isAssigComplete(assignment1)) ## false
# print(csp2.isAssigComplete(assignment2)) ## false
# print(csp3.isAssigComplete(assignment3)) ## true
# print(csp4.isAssigComplete(assignment4)) ## false

## let's work with assignment4 because there are no values assigned
# print(csp4.Backtrack(assignment3))


# dict = {"A1": [7, 8, 9],
#                 "A2": [7, 8, 9],
#                 "A3": [7],
#                 "B1": [7, 8],
#                 "B2": [7, 8],
#                 "B3": [7, 8, 9],
#                 "C1": [7],
#                 "C2": [7, 8, 9],
#                 "C3": [7, 8, 9, 2, 1]
#                 }

# dict= {'a': [9,2,3,4,5], 'b': [1,2,3,4, 5, 6], 'c': [], 'd': [1,2,3,4], 'e': [1,2]}
# dict_temp = {'a': 'hello', 'b': 'bye', 'c': '', 'd': 'aa', 'e': 'zz'}


# def sort_by_values_len(dict):
#     dict_len = {key: len(value) for key, val in dict.items()}
#     import operator
#     sorted_key_list = sorted(dict_len.items(), key=operator.itemgetter(1), reverse=False)
#     sorted_dict = [{item[0]: dict[item [0]]} for item in sorted_key_list]
#     return sorted_dict


# print (sort_by_values_len(dict))
# new_dict = sort_by_values_len(dict)
# print(new_dict)
# print("testing")
# print(assignment3["A1"] != assignment3["A2"] != assignment3["A3"] != assignment3["B2"])
# print(len(assignment3))
#
# unique_values = list()
# duplicate_values = list()
# for value in assignment3.values():
#     if value not in unique_values or value is None:
#         unique_values.append(value)
#     else:
#         duplicate_values.append(value)
#
# print("Unique values: ", unique_values)
# print("Duplicate values: ", duplicate_values)
#list_of_sorted_dict = sorted(dict, key = lambda key: len(dict[key]))

#print(list_of_sorted_dict)