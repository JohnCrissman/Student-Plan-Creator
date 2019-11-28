import unittest
from py.Backtracking import Backtracking


class CSP1:
    def __init__(self):
        self.domains = {
            'S1C1': ['CS400'], 'S1C2': ['CS404'],
            'S1C3': ['CS325', 'CS331', 'CS335', 'CS345', 'CS400', 'CS401', 'CS404', 'CS413', 'CS415', 'CS419',
                     'CS460', 'CS490'],
            'S2C1': ['CS331', 'CS355', 'CS442'], 'S2C2': ['CS411', 'CS412'], 'S2C3': ['CS335'],
            'S3C1': ['CS331', 'CS401', 'CS413', 'CS415', 'CS419', 'CS490'],
            'S3C2': ['CS331', 'CS401', 'CS413', 'CS415', 'CS419', 'CS490'],
            'S3C3': ['CS331', 'CS401', 'CS413', 'CS415', 'CS419', 'CS490'],
            'S4C1': ['CS325', 'CS331', 'CS335', 'CS345', 'CS400', 'CS404', 'CS412', 'CS416', 'CS420', 'CS440',
                     'CS460', 'MATH305', 'ECON401', 'CS490'],
            'S4C2': ['CS420'], 'S4C3': ['CS490']
        }

        self.variables = [k for k in self.domains.keys()]

    def get_constraints_updated_so_far(self, constraints):
        return {"S1C1": 1,
                "S1C2": 1,
                "S1C3": 1,
                "S2C1": 1,
                "S2C2": 1,
                "S2C3": 1,
                "S3C1": 1,
                "S3C2": 1,
                "S3C3": 1,
                "S4C1": 1,
                "S4C2": 1,
                "S4C3": 1
                }

    def is_assign_consistent(self, candidate, val, assignment_input):
        """ returns true if the same course is not taken more than once"""
        assignment1 = dict.copy(assignment_input)
        assignment1[candidate] = val

        return self.check_consistency(assignment1)

    def check_consistency(self, assignment):
        unique_values = list()
        for value in assignment.values():
            if value not in unique_values or value is None:
                unique_values.append(value)
        # print(assignment, "      ",unique_values)
        return len(assignment) == len(unique_values)

    def is_assign_complete(self, assignment_input):
        return (self.check_consistency(assignment_input)
                and len(assignment_input) == len(self.variables)
                )


class TestCSP(unittest.TestCase):

    def test_should_return_three_solutions(self):
        bt = Backtracking(CSP1())
        solution = bt.backtracking_algorithm_first_n_solution(3)
        print(solution)
        print( len(bt.all_solutions))
        for sol in bt.all_solutions:
            print(sol)
            for k, v in sol.items():
                print(k, ": ", v)
        # if solution is not None:
        #     print(solution)
        #     print(len(solution))
        #     for k, v in sorted(bt.all_solutions.items()):
        #         print(k, v)
        # print("\n\nAll solutions are: ", bt.all_solutions)
        self.assertEqual(3, len(bt.all_solutions), "number of solutions are 3")

    def test_should_return_false_for_creating_list_copy_diff_object_same_contents(self):
        my_list = [3, 4, 7, 8, 0, 10, -1]  # {]"C1": [3,4,5,6], "C3":[3,6,5]}
        list_copy = [v for v in my_list]
        self.assertEqual(my_list, list_copy, "same list content")

    def test_should_return_false_for_creating_dict_copy_diff_object_same_contents(self):
        dictionary = {"C1": 3}
        dic_copy = dict.copy(dictionary)
        self.assertEqual(dictionary, dic_copy, "copy of dictionary")

    def test_should_return_false_for_creating_list_copy_diff_object(self):
        my_list = [3, 4, 7, 8, 0, 10, -1]  # {]"C1": [3,4,5,6], "C3":[3,6,5]}
        list_copy = [v for v in my_list]
        self.assertIsNot(my_list, list_copy, "copy of list")

    def test_should_return_false_for_creating_dict_copy_diff_object(self):
        dictionary = {"C1": 3}
        dic_copy = dict.copy(dictionary)
        self.assertIsNot(dictionary, dic_copy, "copy of dictionary")

    def test_should_return_false_for_creating_list_copy_diff_object_eight2(self):
        dictionary = {"C1": [3, 4, 5, 6, 7], "C2": [0]}
        d = {}
        for k, v in dictionary.items():
            d[k] = [course for course in v]
        self.assertIsNot(dictionary["C1"], d["C1"], "copy of dictionary and copy of its list ")

    def test_should_return_false_for_creating_list_copy_diff_object_eight(self):
        dictionary = {"C1": [3, 4, 5, 6, 7], "C2": [0]}
        dic_copy = dict.copy(dictionary)
        self.assertIsNot(dictionary["C1"], dic_copy["C1"], "copy of list")

    def test_should_remove_variables_values_that_are_already_assigned_eight(self):
        bt = Backtracking(CSP1())
        dom = {
                'S1C1': ['CS400'],
                'S1C2': ['CS404'],
                'S1C3': ['CS325', 'CS331', 'CS335', 'CS345', 'CS400', 'CS401', 'CS404', 'CS413', 'CS415', 'CS419', 'CS460', 'CS490'],
                'S2C1': ['CS331', 'CS355', 'CS442'],
                'S2C2': ['CS411', 'CS412'],
                'S2C3': ['CS335'],
                'S3C1': ['CS331', 'CS401', 'CS413', 'CS415', 'CS419', 'CS490'],
                'S3C2': ['CS331', 'CS401', 'CS413', 'CS415', 'CS419', 'CS490'],
                'S3C3': ['CS331', 'CS401', 'CS413', 'CS415', 'CS419', 'CS490'],
                'S4C1': ['CS325', 'CS331', 'CS335', 'CS345', 'CS400', 'CS404', 'CS412', 'CS416', 'CS420', 'CS440', 'CS460', 'MATH305', 'ECON401', 'CS490'],
                'S4C2': ['CS420'],
                'S4C3': ['CS490']
              }

        assignment = {'S1C1': 'CS400',
                       'S1C2': 'CS404',
                       'S2C3': 'CS335',
                       'S4C2': 'CS420',
                       'S4C3': 'CS490',
                       'S2C2': 'CS411',
                       'S2C1': 'CS331',
                       'S3C1': 'CS419'
                       }
        res = {
                # 'S1C1': ['CS400'],
                # 'S1C2': ['CS404'],
                'S1C3': ['CS325',
                         # 'CS331',

                         # 'CS335',
                         'CS345',
                         # 'CS400',
                         'CS401',
                         # 'CS404',
                         'CS413', 'CS415',
                         # 'CS419',
                         'CS460',
                         # 'CS490'
                         ],
                # 'S2C1': ['CS331', 'CS355', 'CS442'],
                # 'S2C2': ['CS411', 'CS412'],
                # 'S2C3': ['CS335'],
                # 'S3C1': [
                    # 'CS331',
                    # 'CS401', 'CS413', 'CS415', 'CS419',
                         # 'CS490'
                         # ],
                'S3C2': [
                    # 'CS331',
                    'CS401', 'CS413', 'CS415',
                         # 'CS419',

                         # 'CS490'
                         ],
                'S3C3': [
                    # 'CS331',
                    'CS401', 'CS413', 'CS415',
                         # 'CS419',

                         # 'CS490'
                         ],
                'S4C1': ['CS325',
                         # 'CS331',

                         # 'CS335',
                         'CS345',
                         # 'CS400',
                         # 'CS404',
                         'CS412', 'CS416',
                         # 'CS420',
                         'CS440', 'CS460', 'MATH305', 'ECON401',
                         # 'CS490'
                         ],
                # 'S4C2': ['CS420'],
                # 'S4C3': ['CS490']
              }
        print(len(res))
        bt.remove_variables_values_that_are_already_assigned(assignment, dom)
        print("\n\n", res.keys())
        print(dom.keys())
        self.assertNotIn('CS400', dom, "cs 400 not in dom")
        self.assertNotIn('CS404', dom, "CS404 not in dom")
        self.assertEqual(len(res), len(dom), "same length")
        self.assertEqual(len(res), len(dom), "same length")
        self.assertEqual(res.keys(), dom.keys(), "updating domains taking 400 and 404")

        self.assertDictEqual(res, dom, "updating domains taking 400 and 404")

    def test_should_remove_variables_values_that_are_already_assigned_two2(self):
        bt = Backtracking(CSP1())
        dom = {
                'S1C1': ['CS400'],
                'S1C2': ['CS404'],
                'S1C3': ['CS325', 'CS331', 'CS335', 'CS345', 'CS400', 'CS401', 'CS404', 'CS413', 'CS415', 'CS419', 'CS460', 'CS490'],
                'S2C1': ['CS331', 'CS355', 'CS442'],
                'S2C2': ['CS411', 'CS412'],
                'S2C3': ['CS335'],
                'S3C1': ['CS331', 'CS401', 'CS413', 'CS415', 'CS419', 'CS490'],
                'S3C2': ['CS331', 'CS401', 'CS413', 'CS415', 'CS419', 'CS490'],
                'S3C3': ['CS331', 'CS401', 'CS413', 'CS415', 'CS419', 'CS490'],
                'S4C1': ['CS325', 'CS331', 'CS335', 'CS345', 'CS400', 'CS404', 'CS412', 'CS416', 'CS420', 'CS440', 'CS460', 'MATH305', 'ECON401', 'CS490'],
                'S4C2': ['CS420'],
                'S4C3': ['CS490']
              }

        assignment = {'S1C1': 'CS400',
                      'S1C2': 'CS404'
                       # 'S2C3': 'CS335',
                       # 'S4C2': 'CS420',
                       # 'S4C3': 'CS490',
                       # 'S2C2': 'CS411',
                       # 'S2C1': 'CS331',
                       # 'S3C1': 'CS419'
                      }
        res = {
                # 'S1C1': ['CS400'],
                # 'S1C2': ['CS404'],
                'S1C3': ['CS325', 'CS331', 'CS335', 'CS345',
                         # 'CS400',
                         'CS401',
                         # 'CS404',
                         'CS413', 'CS415',
                         'CS419',
                         'CS460', 'CS490'],
                'S2C1': ['CS331', 'CS355', 'CS442'],
                'S2C2': ['CS411', 'CS412'],
                'S2C3': ['CS335'],
                'S3C1': ['CS331', 'CS401', 'CS413', 'CS415', 'CS419', 'CS490'],
                'S3C2': ['CS331', 'CS401', 'CS413', 'CS415',
                         'CS419',
                         'CS490'],
                'S3C3': ['CS331', 'CS401', 'CS413', 'CS415',
                         'CS419',
                         'CS490'],
                'S4C1': ['CS325', 'CS331', 'CS335', 'CS345',
                         # 'CS400',
                         # 'CS404',
                         'CS412', 'CS416', 'CS420', 'CS440', 'CS460', 'MATH305', 'ECON401', 'CS490'],
                'S4C2': ['CS420'],
                'S4C3': ['CS490']
              }
        print(len(res))
        bt.remove_variables_values_that_are_already_assigned(assignment, dom)
        print("\n\n", res.keys())
        print(dom.keys())
        self.assertNotIn('CS400', dom, "cs 400 not in dom")
        self.assertNotIn('CS404', dom, "CS404 not in dom")
        self.assertEqual(len(res), len(dom), "same length")
        self.assertEqual(len(res), len(dom), "same length")
        self.assertEqual(res.keys(), dom.keys(), "updating domains taking 400 and 404")

        self.assertDictEqual(res, dom, "updating domains taking 400 and 404")

    def test_should_remove_variables_values_that_are_already_assigned_two(self):

        bt = Backtracking(CSP1())
        dom = {
                'S1C1': ['CS400'],
                'S1C2': ['CS404'],
                'S1C3': ['CS325', 'CS331', 'CS335', 'CS345', 'CS400', 'CS401', 'CS404', 'CS413', 'CS415', 'CS419', 'CS460', 'CS490'],
                'S2C1': ['CS331', 'CS355', 'CS442'],
                'S2C2': ['CS411', 'CS412'],
                'S2C3': ['CS335'],
                'S3C1': ['CS331', 'CS401', 'CS413', 'CS415', 'CS419', 'CS490'],
                'S3C2': ['CS331', 'CS401', 'CS413', 'CS415', 'CS419', 'CS490'],
                'S3C3': ['CS331', 'CS401', 'CS413', 'CS415', 'CS419', 'CS490'],
                'S4C1': ['CS325', 'CS331', 'CS335', 'CS345', 'CS400', 'CS404', 'CS412', 'CS416', 'CS420', 'CS440', 'CS460', 'MATH305', 'ECON401', 'CS490'],
                'S4C2': ['CS420'],
                'S4C3': ['CS490']
              }


        assignment = {'S1C1': 'CS400',
                       # 'S1C2': 'CS404',
                       # 'S2C3': 'CS335',
                       # 'S4C2': 'CS420',
                       # 'S4C3': 'CS490',
                       # 'S2C2': 'CS411',
                       # 'S2C1': 'CS331',
                       'S3C1': 'CS419'
                      }
        res = {
                # 'S1C1': ['CS400'],
                'S1C2': ['CS404'],
                'S1C3': ['CS325', 'CS331', 'CS335', 'CS345',
                         # 'CS400',
                         'CS401', 'CS404', 'CS413', 'CS415',
                         # 'CS419',
                         'CS460', 'CS490'],
                'S2C1': ['CS331', 'CS355', 'CS442'],
                'S2C2': ['CS411', 'CS412'],
                'S2C3': ['CS335'],
                # 'S3C1': ['CS331', 'CS401', 'CS413', 'CS415', 'CS419', 'CS490'],
                'S3C2': ['CS331', 'CS401', 'CS413', 'CS415',
                         # 'CS419',
                         'CS490'],
                'S3C3': ['CS331', 'CS401', 'CS413', 'CS415',
                         # 'CS419',
                         'CS490'],
                'S4C1': ['CS325', 'CS331', 'CS335', 'CS345',
                         # 'CS400',
                         'CS404', 'CS412', 'CS416', 'CS420', 'CS440', 'CS460', 'MATH305', 'ECON401', 'CS490'],
                'S4C2': ['CS420'],
                'S4C3': ['CS490']
              }

        bt.remove_variables_values_that_are_already_assigned(assignment, dom)
        self.assertDictEqual(res, dom, "updating correctly the domains")


    def test_should_return_selected_variable_thing(self):
        num_constraints = {'mari': 7, 'valor': 12, 'thing': 14, 'word': 7, 'maps': 3}
        dic_legal_moves = {'mari': 2, 'valor': 2, 'thing': 2, 'word': 2, 'maps': 8}
        bt = Backtracking()
        selected_variable = bt.mrv_degree_alpha(dic_legal_moves, num_constraints)
        self.assertEqual("thing", selected_variable, "this is the message")

    def test_should_return_selected_variable_mari(self):
        num_constraints = {'mari': 12, 'valor': 12, 'thing': 4, 'word': 7, 'maps': 3}
        dic_legal_moves = {'mari': 2, 'valor': 2, 'thing': 2, 'word': 2, 'maps': 8}
        bt = Backtracking()
        selected_variable = bt.mrv_degree_alpha(dic_legal_moves, num_constraints)
        self.assertEqual("mari", selected_variable, "this is the message")

    def test_should_return_selected_variable_maps(self):
        num_constraints = {'mari': 7, 'valor': 12, 'thing': 1, 'word': 7, 'maps': 5}
        dic_legal_moves = {'mari': 2, 'valor': 12, 'thing': 1, 'word': 2, 'maps': 1}
        bt = Backtracking()
        selected_variable = bt.mrv_degree_alpha(dic_legal_moves, num_constraints)
        self.assertEqual("maps", selected_variable, "this is the message")

    def test_should_return_empty_set(self):
        class CSP1:
            def __init__(self):
                self.domains = {"mari": ["CS400"],
                                "valor": ["CS404", "CS411", "CS345"],
                                "nazanin": ["CS400"],
                                "thing": ["CS331", "CS411", "CS345", "CS355", "CS442", "CS460"],
                                "word": ["CS401", "CS411", "CS412", "CS413"],
                                "maps": ["CS335", "CS415", "CS416", "CS419", "CS400"]
                                }
                self.variables = [k for k in self.domains.keys()]

            def get_constraints_updated_so_far(self, constraints):
                return {'mari': 7, "nazanin": 4, 'valor': 12, 'thing': 14, 'word': 7, 'maps': 3}

            def is_assign_consistent(self, candidate, val, assignment_input):
                """ returns true if the same course is not taken more than once"""
                assignment1 = dict.copy(assignment_input)
                assignment1[candidate] = val

                return self.check_consistency(assignment1)

            def check_consistency(self, assignment):
                unique_values = list()
                for value in assignment.values():
                    if value not in unique_values or value is None:
                        unique_values.append(value)
                # print(assignment, "      ",unique_values)
                return len(assignment) == len(unique_values)

            def is_assign_complete(self, assignment_input):
                return (self.check_consistency(assignment_input)
                        and len(assignment_input) == len(self.variables)
                        )

        bt = Backtracking(CSP1())
        solution = bt.backtracking_algorithm()
        self.assertEqual(None, solution, "No solution")

    def test_should_return_backtrack_and_return_a_solution(self):
        class CSP1:
            def __init__(self):
                # TODO: think of a combination that makes it backtrack and test result
                self.domains = {"mari": ["CS400", "CS404"],
                                "valor": ["CS404", "CS400", "CS345", "CS415"],
                                "nazanin": ["CS400", "CS404"],
                                "thing": ["CS331", "CS411", "CS345", "CS355", "CS442", "CS460"],
                                "word": ["CS401", "CS411", "CS412", "CS413"],
                                "maps": ["CS335", "CS415", "CS416", "CS419", "CS400"]
                                }
                self.variables = [k for k in self.domains.keys()]

            def get_constraints_updated_so_far(self, constraints):
                return {'mari': 7, "nazanin": 4, 'valor': 12, 'thing': 14, 'word': 7, 'maps': 3}

            def is_assign_consistent(self, candidate, val, assignment_input):
                """ returns true if the same course is not taken more than once"""
                assignment1 = dict.copy(assignment_input)
                assignment1[candidate] = val

                return self.check_consistency(assignment1)

            def check_consistency(self, assignment):
                unique_values = list()
                for value in assignment.values():
                    if value not in unique_values or value is None:
                        unique_values.append(value)
                # print(assignment, "      ",unique_values)
                return len(assignment) == len(unique_values)

            def is_assign_complete(self, assignment_input):
                return (self.check_consistency(assignment_input)
                        and len(assignment_input) == len(self.variables)
                        )

        bt = Backtracking(CSP1())
        solution = bt.backtracking_algorithm()
        self.assertEqual(None, solution, "A solution")

    def test_should_return_backtrack_and_return_a_solution2(self):
        class CSP1:
            def __init__(self):
                # TODO: think of a combination that makes it backtrack and test result
                self.domains = {"mari": ["CS400"],
                                "valor": ["CS404", "CS400", "CS345", "CS415"],
                                "nazanin": ["CS400", "CS404"],
                                "thing": ["CS331", "CS411", "CS345", "CS355", "CS442", "CS460"],
                                "word": ["C", "CS411", "CS412", "CS413"],
                                "maps": ["CS335", "CS415", "CS416", "CS419", "CS400"]
                                }
                self.variables = [k for k in self.domains.keys()]

            def get_constraints_updated_so_far(self, constraints):
                return {'mari': 7, "nazanin": 4, 'valor': 12, 'thing': 14, 'word': 7, 'maps': 3}

            def is_assign_consistent(self, candidate, val, assignment_input):
                """ returns true if the same course is not taken more than once"""
                assignment1 = dict.copy(assignment_input)
                assignment1[candidate] = val

                return self.check_consistency(assignment1)

            def check_consistency(self, assignment):
                unique_values = list()
                for value in assignment.values():
                    if value not in unique_values or value is None:
                        unique_values.append(value)
                # print(assignment, "      ",unique_values)
                return len(assignment) == len(unique_values)

            def is_assign_complete(self, assignment_input):
                return (self.check_consistency(assignment_input)
                        and len(assignment_input) == len(self.variables)
                        )

        bt = Backtracking(CSP1())
        solution = bt.backtracking_algorithm()
        self.assertEqual(None, solution, "No solution")

    def test_should_return_the_affected_neighbors(self):

        self.assertEqual(None, None, "")


if __name__ == '__main__':
    unittest.main()
