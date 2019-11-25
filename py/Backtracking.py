import heapq
import math
import pprint
from py.m_CSP import CSP


class Backtracking:

    # instantiate
    def __init__(self):
        self.csp = CSP()
        self.assignment = {}
        # self.legal_moves = {}
        self.num_constraints = {}
        self.num_constraints_for_each = {}

    def backtracking_algorithm(self):
        # starts with nothing assigned
        return self.backtrack({}, self.csp)

    def backtrack(self, assignment_so_far, csp):
        # returns None if failure
        if csp.is_assign_complete(assignment_so_far):
            return assignment_so_far

        candidate = self.select_unassigned_variable(assignment_so_far, csp)
        print("candidate: ", candidate)

        for val in self.order_domain_variables(candidate, assignment_so_far, csp.domain):
            print("checking if candidate with selected value are consistent:\t", candidate, " : ", val)
            if csp.is_assign_consistent(candidate, val, assignment_so_far):
                # the assignment is consistent
                print("the assignment is consistent")
                assignment_so_far[candidate] = [val]
                result = self.backtrack(assignment_so_far, csp)
                if result is not None:
                    print("Assignment so far:", result)
                    return result
            print("assignment_so_far: ", assignment_so_far, "the assignment is not consistent or returned Failure")
            # the assignment is not consistent or returned Failure
            # here I undo all changes I made assuming the val was going to work
            # I mean specially in the domain, if any were made
            assignment_so_far.pop(candidate, val)
            # remove val from assignment and inferences from the the csp

        return None


    def select_unassigned_variable(self, assignment_so_far, csp_so_far):
        # TODO: still needs CSP get_constraints_updated_so_far(assignment_so_far)
        constraints = csp_so_far.get_containts_updated_so_far(assignment_so_far)
        var, dom = self.get_csp_updated_so_far(assignment_so_far)
        legal_moves = self.__get_legal_moves(dom)
        return self.mrv_degree_alpha(legal_moves, constraints)

    def order_domain_variables(self, candidate_name, assignment, domains):
        """
        returns an ordered list with the values to be evaluated based on the least constraining value
        :param candidate_name:
        :param assignment:
        :param domains:
        :return:
        """
        print("\tcandidate:\t", candidate_name)
        print("\tassignment\t", assignment)
        print("\tdomains:\t", domains)

        # create affecting neighbors dictionary
        affect_neighbors = {}
        affected = []
        candidate_values = domains.pop(candidate_name)
        for possible_value in candidate_values:
            print("\t\tlcv value: ", possible_value)
            # get the new legal moves assuming new assignment has candidate_name: possible value
            temp_assignment = dict.copy(assignment)
            temp_assignment[candidate_name] = possible_value

            print("\t\ttemporary assignment\t", temp_assignment, "\tfor ", candidate_name, ":", possible_value)

            temp_var, temp_dom = self.get_csp_updated_so_far(temp_assignment)
            legal_moves_per_name = {name: len(values) for name, values in temp_dom.items()}
            print("\t\tlegal_moves_per_name\t", legal_moves_per_name)

            # TODO: filter neighbors of candidate given the constraints
            # constaint_graph = []
            # legal_moves_per_name2 = {{var: num} for var, num in legal_moves_per_name if var in constraint_graph}
            #     if variable in constraint_graph:
            #       legal_moves_per_name[variable] = number

            # for now I assume that everyone is a neighbor of everyone
            sum_up = self.sum_up_neighbors_with_possible_values(legal_moves_per_name)
            affect_neighbors[possible_value] = sum_up
            tup = ((-1)*sum_up, possible_value)
            affected.append(tup)

        print("\taffect_neighbors:\t", affect_neighbors)
        heapq.heapify(affected)
        print("\taffected:\t", affected)

        final_ordered_list = [heapq.heappop(affected)[1] for i in range(len(affected))]
        print("\tfinal ordered list: \t", final_ordered_list)

        return final_ordered_list

    def sum_up_neighbors_with_possible_values(self, legal_moves_per_name):
        """
        Reduction of dictionary to the number of moves of the neighbors given the fact that the value "possible_value"
        might be chosen for the candidate variable
        :param legal_moves_per_name: a dictionary with neighbor as key and length of the updated domain as value
        :return: sum of all the number of moves of its neighbors given the potential value chosen
        """
        # total = 0
        # for k, v in legal_moves_per_name.items():
        #     print("k ", k, "\tv ",v)
        #     total = total + v
        # print("total: ", total, "\tsum(): ", sum(legal_moves_per_name.values()))

        return sum(legal_moves_per_name.values())

    def __get_legal_moves(self, dom):
        return {key: len(value) for key, value in dom.items()}

    # def get_variables_updated_so_far(self, assignment):
    #     """return new variables given the assignment"""
    #     new_variables = self.__crete_copy_of_variables()
    #     for k, v in assignment.items():
    #         print("k,v: (", k, ",", v, ")\t ")
    #         new_variables.remove(k)
    #
    #     return new_variables

    def __crete_copy_of_variables(self):
        """
        private method
        returns a copy of the list"""
        return self.csp.variables[:]

    def __crete_copy_of_domain(self):
        """
        private method
        returns a copy of the dictionary"""
        return dict.copy(self.csp.domain)

    def get_csp_updated_so_far(self, assignment):
        """
        private method
        Given the assignment, returns the variables and domain of variables
        that still need to be assigned the Domain is also updated with the constraint
        that a value cannot be assigned more than once
        :param assignment:
        :return: a list of two objects [0] the new variables [1] the new domains given the assignment
        """
        print("\t\t--Assignment:\t", assignment)
        new_variables = self.__crete_copy_of_variables()
        new_domains = self.__crete_copy_of_domain()
        print("\t\t--Variables:\t", new_variables)
        print("\t\t--Domains\t", new_domains)
        for variable, value in assignment.items():
            # print("k,v: (", k, ",", v, ")\t ")
            # remove the variables that are already assigned from the new variable set
            new_variables.remove(variable)
            # remove the variables that are already assigned
            new_domains.pop(variable)
            # remove the value from all domains
            self.__eliminate_assigned_values_from_each_domain(new_domains, value)

        print("\n\t\t--initial Variables:\t", self.csp.variables, "\n\t\t--initial Domains\t", self.csp.domain)
        print("\n\t\t--new Variables:\t", new_variables, "\n\t\t--new Domains\t", new_domains)
        return new_variables, new_domains

    def __eliminate_assigned_values_from_each_domain(self, all_domains, value_assigned):
        """
        private method
        Removes the assigned value from all domains maybe a form of forward checking:
        all variables must have different assigned values
        :param all_domains:
        :param value_assigned:
        :return: no return
        """
        for variable, domain in all_domains.items():
            # make sure to eliminate the selected value from the other options
            try:
                domain.remove(value_assigned)
            except ValueError:
                continue

    def mrv_degree_alpha(self, dic_legal_moves, dic_num_constraints):
        """
        Sorts the dictionary based on mrv, then num of constraints and finally alphabetically
        :param dic_legal_moves: refers to the dictionary with variable as key and # legal moves as value
        :param dic_num_constraints: refers to the dictionary with variable as key and # constraints as value
        :return: returns the name of the variable or None if there aren't any to be assigned
        """
        legal_moves = [(v, (-1) * dic_num_constraints[k], k) for k, v in dic_legal_moves.items()]
        # print("Legal moves:  ", legal_moves)
        heapq.heapify(legal_moves)
        # print("Heap Legal moves: ", legal_moves)
        degree_moves = []
        more = True
        count = 0
        prev = math.inf
        while legal_moves and more:
            popped = heapq.heappop(legal_moves)
            var_nro_moves = popped[0]
            var_num_const = popped[1]
            var_name = popped[2]
            # print(popped, "\t", var_name, ": \t Nro: moves: ", var_nro_moves, "\t Nro Constraints: ", (-1) * var_num_const)
            if count is 0:
                heapq.heappush(degree_moves, popped)
            else:
                if prev == var_nro_moves:
                    heapq.heappush(degree_moves, popped)
                else:
                    heapq.heappush(legal_moves, popped)
                    more = False

            prev = var_nro_moves
            count = count + 1
        # print("Legal Moves: ", legal_moves)
        # print("Choices for MRV: ", degree_moves)
        try:
            popped = heapq.heappop(degree_moves)
        except IndexError:
            print("No variables left to be assigned")
            return None
        # print("after selection: ", degree_moves)
        # print("\nSelected variable: ", popped, "\t-->", popped[2])
        return popped[2]

