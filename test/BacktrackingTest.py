import unittest
from py.Backtracking import Backtracking


class TestCSP(unittest.TestCase):

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
        self.assertEqual(None, solution, "No solution")


if __name__ == '__main__':
    unittest.main()
