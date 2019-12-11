import heapq
import math


class Backtracking:

    # constructor
    def __init__(self, csp):
        self.csp = csp
        self.assignment = {}
        # self.num_constraints = {}
        # self.num_constraints_for_each = {}
        self.all_solutions = []
        self.__find_all = False
        self.__max_number_of_solutions = 1

    def backtracking_algorithm_one_solution(self):
        self.backtracking_algorithm_first_n_solution(1)

    def backtracking_algorithm_first_n_solution(self, n):
        self.__max_number_of_solutions = n
        self.backtracking_algorithm()

    def backtracking_algorithm_all_solutions(self):
        self.__find_all = True
        self.backtracking_algorithm()

    def backtracking_algorithm(self):
        # starts with nothing assigned
        self.assignment = self.backtrack(self.assignment, self.csp)
        return self.assignment

    def backtrack(self, assignment, csp):
        l = [(k, len(v)) for k, v in self.csp.domains.items()]
        print("\n\n+++++ Domains so far: ", l, "\n\n")
        assignment_so_far = dict.copy(assignment)
        # returns None if failure
        if csp.is_assign_complete(assignment_so_far):
            if self.__find_all or len(self.all_solutions) < self.__max_number_of_solutions:
                self.all_solutions.append(dict.copy(assignment_so_far))
                return None
            else:
                return assignment_so_far

        print("BT* MRV (Start) =========")
        candidate = self.select_unassigned_variable(assignment_so_far, csp)
        print("BT* MRV (End) ========= --> candidate: ", candidate, "\n")

        for val in self.order_domain_variables(candidate, assignment_so_far, csp):
            print("BT* LVC ========= checking if {", candidate, " : ", val, "} is consistent ?")
            if csp.is_assign_consistent(candidate, val, assignment_so_far):
                # the assignment is consistent
                print("\t\tBT* YES!")
                # we add the candidate and value to our assignment
                assignment_so_far[candidate] = val
                print("+++++++++++ ",  [(k, len(v)) for k, v in self.csp.domains.items()])
                result = self.backtrack(assignment_so_far, csp)
                if result is not None:
                    # print("\nBT* Assignment so far:", result, "\n")
                    return result
                # returned None
                # here I undo all changes I made assuming the val was going to work
                # I mean specially in the domain, if any were made
                # remove val from assignment and inferences from the the csp
                assignment_so_far.pop(candidate)
            else:
                print("\t\tBT* NO!")
            print("BT* The assignment so far: ", assignment_so_far, "the assignment is not consistent or returned Failure\n\n")
            # the assignment is not consistent

        return None

    def select_unassigned_variable(self, assignment_so_far, csp_so_far):
        constraints = csp_so_far.get_constraints_updated_so_far(assignment_so_far)
        # deletes the the already assigned variables and values from the csp
        dom = self.get_csp_updated_so_far(assignment_so_far)
        legal_moves = self.__get_legal_moves(dom)
        return self.mrv_degree_alpha(legal_moves, constraints)

    def order_domain_variables(self, candidate_name, assignment, csp):
        """
        returns an ordered list with the values to be evaluated based on the least constraining value
        :param candidate_name: variable to be assigned a value
        :param assignment: a dictionary with whats already assigned (key-value pair)
        :param csp: csp object containing the original csp
        :return: a list with the values to be evaluated ordered by the LCV -> alphabetically
        """
        domains = dict.copy(csp.domains)
        print("\t|- Order the values for LCV:")
        print("\t\tassignment\t", assignment, "\n\t\tdomains:\t", domains, "\n\t\tcandidate:\t", candidate_name)

        # remove variables that have been assigned already from the domains
        # self.__eliminate_variables_from_all_domains(domains, assignment)

        # create affecting neighbors dictionary

        affected = self.number_of_affected_neighbors(assignment, candidate_name, domains)

        heapq.heapify(affected)
        # print("\t|- affected:\t", affected)

        final_ordered_list = [heapq.heappop(affected)[1] for i in range(len(affected))]
        print("\t|- final LCV ordered list: \t", final_ordered_list)

        return final_ordered_list

    def number_of_affected_neighbors(self, assignment, candidate_name, dom):
        candidate_values = dom.pop(candidate_name)
        affect_neighbors = {}
        affected = []
        # print("\t\tChoosing a value for: ", candidate_name)
        for possible_value in candidate_values:
            # hypothetically we think that possible value will be assigned to candidate_name
            # print("\t\t\tIF =>  ", candidate_name, " :", possible_value)
            temp_assignment = dict.copy(assignment)
            temp_assignment[candidate_name] = possible_value
            # print("\t\t\tIF =>  ", temp_assignment)

            # get the new domain if candidate_name and possible_value are added to the assignment
            temp_dom = self.get_csp_updated_so_far(temp_assignment)

            # get the new legal moves assuming new assignment has added candidate_name: possible value
            legal_moves_per_name = self.__get_legal_moves(temp_dom)
            # print("\t\t\tIF => legal_moves_per_name\t", legal_moves_per_name)

            # for now I assume that everyone is a neighbor of everyone
            sum_up = self.sum_up_neighbors_with_possible_values(legal_moves_per_name)
            affect_neighbors[possible_value] = sum_up
            tup = ((-1) * sum_up, possible_value)
            affected.append(tup)
        print("\t\taffect_neighbors:\t", affect_neighbors)
        return affected

    def sum_up_neighbors_with_possible_values(self, legal_moves_per_name):
        """
        Reduction of dictionary to the number of moves of the neighbors given the fact that the value "possible_value"
        might be chosen for the candidate variable
        :param legal_moves_per_name: a dictionary with neighbor as key and length of the updated domain as value
        :return: sum of all the number of moves of its neighbors given the potential value chosen
        """
        return sum(legal_moves_per_name.values())

    def __get_legal_moves(self, dom):
        return {key: len(value) for key, value in dom.items()}

    def __crete_copy_of_variables(self):
        """
        private method
        returns a copy of the all initial keys in the domains as a list"""
        return [k for k in self.csp.domains.keys()]

    def __crete_copy_of_domain(self):
        """
        private method
        returns a copy of the dictionary with all initial domains"""
        d = {}
        for k, v in self.csp.domains.items():
            d[k] = [course for course in v]
        return d

    def get_csp_updated_so_far(self, assignment):
        """
        private method
        Given the assignment, returns the variables and domain of variables
        that still need to be assigned the Domain is also updated with the constraint
        that a value cannot be assigned more than once
        :param assignment:
        :return: a list of two objects [0] the new variables [1] the new domains given the assignment
        """
        print("\t\t ============ UPDATE CSP - START\n")
        print("\t\t--Assignment:\t", assignment)
        new_domains = self.__crete_copy_of_domain()
        # new_variables = [k for k in new_domains.keys()]  # self.__crete_copy_of_variables()
        # print("\t\t--(copy) ini Variables:\t", new_domains.keys())
        # print("\t\t--(copy) ini Domains\t", new_domains)

        self.remove_variables_values_that_are_already_assigned(assignment, new_domains)

        # print("\n\t\t--new Variables:\t", new_domains.keys(), "\n\t\t--new Domains\t", new_domains)
        print("\t\t ============ UPDATE CSP - END\n")
        return new_domains

    def remove_variables_values_that_are_already_assigned(self, assignment, new_domains):
        for variable, value in assignment.items():
            # print("variable,value: (", variable, ",", value, ")\t ")
            # remove the variables that are already assigned from the new variable set
            new_domains.pop(variable)
            # remove the value that are already selected from all available domains
            self.__eliminate_value_from_domains(new_domains, value)

    def __eliminate_value_from_domains(self, all_domains, value_to_be_removed):
        """
        private method
        Removes the assigned value from all domains maybe a form of forward checking:
        all variables must have different assigned values
        :param all_domains:
        :param value_to_be_removed:
        :return: no return
        """
        # print("******========= BEFORE eliminate value (", value_to_be_removed, ")\nBefore:", [(k,len(v)) for k,v in all_domains.items()])
        for variable, domain in all_domains.items():
            # make sure to eliminate the selected value from the other options
            try:
                # print("trying... ", variable, "from: ", domain)
                domain.remove(value_to_be_removed)
            except ValueError:
                continue
        # print("After:", [(k, len(v)) for k, v in all_domains.items()], "\n******========= AFTER")


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

