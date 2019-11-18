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





if __name__ == '__main__':
    unittest.main()
