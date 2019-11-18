import heapq
import math
import pprint
from py.m_CSP import CSP


class Backtracking:

    # instantiate
    def __init__(self):
        self.csp = CSP([], {}, {})
        self.assignment = {}
        self.legal_moves = {}
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

        for val in self.order_domain_variables(candidate, assignment_so_far, csp):
            print("checking if candidate with selected value are consistent:", candidate,val)
            if csp.isAssigConsistent(val, assignment_so_far):
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
            assignment_so_far.pop("key", None)
            # remove val from assignment and inferences from the the csp

        return None


    def order_domain_variables(self,candidate, assignment, csp):
        print(candidate, assignment, csp)
        # TODO: the LCV will be implemented here
        # TODO: sort by least affecting neighbors and natural order
        # I might need a method call, affected_neighbors(assignment) that
        # returns a dictionary with the values as keys and number of affected neighbors as value
        return []

    def select_unassigned_variable(self, assignment_so_far, csp_so_far):
        # TODO: use assignment_so_far, csp_so_far to get the legal moves and num constraints
        constraints = csp_so_far.get_containts_updated_so_far(assignment_so_far)
        var, dom = self.get_csp_updated_so_far(assignment_so_far)
        legal_moves = self.get_legal_moves(dom)
        return self.mrv_degree_alpha(legal_moves, constraints)

    def get_legal_moves(self, dom):
        return {key: len(value) for key, value in dom.items()}

    def get_variables_updated_so_far(self, assignment):
        """return new variables given the assignment"""
        new_variables = self.crete_copy_of_variables()
        for k, v in assignment.items():
            print("k,v: (", k, ",", v, ")\t ")
            new_variables.remove(k)

        return new_variables

    def crete_copy_of_variables(self):
        """returns a copy of the list"""
        return self.csp.variables[:]

    def crete_copy_of_domain(self):
        """returns a copy of the dictionary"""
        return dict.copy(self.csp.domain)

    def get_csp_updated_so_far(self, assignment):
        """
        Given the assignment, returns the variables and domain of variables
        that still need to be assigned the Domain is also updated with the constraint
        that a value cannot be assigned more than once
        """
        print("\tAssignment:\t", assignment)
        new_variables = self.crete_copy_of_variables()
        new_domains = self.crete_copy_of_domain()
        print("\tVariables:\t", new_variables, "\n\tDomains\t", new_domains)
        for variable, value in assignment.items():
            # print("k,v: (", k, ",", v, ")\t ")
            # remove the variables that are already assigned from the new variable set
            new_variables.remove(variable)
            # remove the variables that are already assigned
            new_domains.pop(variable)
            # remove the value from all domains
            self.eliminate_assigned_values_from_each_domain(new_domains, value)

        print("\n\told Variables:\t", self.csp.variables, "\n\told Domains\t", self.csp.domain)
        print("\n\tnew Variables:\t", new_variables, "\n\tnew Domains\t", new_domains)
        return new_variables, new_domains

    def eliminate_assigned_values_from_each_domain(self, all_domains, value_assigned):
        # removes the value assigned from all domains
        # maybe a form of forward checking: all variables must have different assigned values
        for variable, domain in all_domains.items():
            # make sure to eliminate the selected value from the other options
            try:
                domain.remove(value_assigned)
            except ValueError:
                continue

    def mrv_degree_alpha(self, dic_legal_moves, dic_num_constraints):
        # dic_legal_moves refers to the dictionary with variable as key and # legal moves as value
        # dict_num_constraints
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
        popped = heapq.heappop(degree_moves)
        # print("after selection: ", degree_moves)
        # print("\nSelected variable: ", popped, "\t-->", popped[2])
        return popped[2]

