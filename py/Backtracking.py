from py.CSP import CSP


class Backtracking:

    # instantiate
    def __init__(self, assignment, num_constraints_for_each):
        self.csp = CSP()
        self.variables = self.csp.getVariables()
        self.domain = self.csp.getDomains()
        self.assignment = assignment
        self.num_constraints_for_each = num_constraints_for_each

    def backtracking_algorithm(self):
        # starts with nothing assigned
        return self.backtrack({}, self.csp)

    def backtrack(self, assignment_so_far, csp):
        # returns None if failure
        if csp.isAssigComplete(assignment_so_far):
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
        # vars_after_mrv = self.MRV(assignment_so_far, csp_so_far)
        # TODO: order the variables by MRV first, then degree, then alphabetical order
        # TODO: return the first variable of this ordered process
        return "var"

    def apply_mrv(self):
        # TODO: ordered variables by minimum legal moves
        # if needed call apply_degree with only the variables that had the same value from the mrv
        return ["", "", ""]

    def apply_degree(self):
        # TODO: ordered variables by minimum legal moves
        return ["", "", ""]





    def sort_by_values_len(dict):
        dict_len = {key: len(value) for key, value in dict.items()}
        import operator
        sorted_key_list = sorted(dict_len.items(), key=operator.itemgetter(1), reverse=False)
        sorted_dict = [{item[0]: dict[item[0]]} for item in sorted_key_list]
        len_smallest = 99999
        for i in sorted_dict:
            if len(sorted_dict[i]) < len_smallest:
                len_smallest = len(sorted_dict[i])

        for j in sorted_dict:
            if len_smallest < len(sorted_dict[j]):
                del sorted_dict[j]

        return sorted_dict

    def getNumConstraints(self):
        return self.num_constraints_for_each


    # def MRV(self, assignment_input):
    #     possible_variables = sort_by_values_len(assignment_input)


    def degree(self):
        return 2

    def LCV(self):
        return 3

    def getAssignment(self):
        return self.assignment

    def getVariables(self):
        return ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]

    def getDomains(self):
        return {"A1": [7, 8, 9],
                "A2": [7, 8, 9],
                "A3": [7, 8, 9],
                "B1": [7, 8, 9],
                "B2": [7, 8, 9],
                "B3": [7, 8, 9],
                "C1": [7, 8, 9],
                "C2": [7, 8, 9],
                "C3": [7, 8, 9]
                }

    # def isAssigConsistent(self, assignment_input):
    #     assignment = assignment_input
    #     return ((assignment["A1"] != assignment["A2"] or assignment["A1"] == None or assignment["A2"] == None)
    #         and (assignment["A1"] != assignment["A3"] or assignment["A1"] == None or assignment["A3"] == None)
    #         and (assignment["A2"] != assignment["A3"] or assignment["A2"] == None or assignment["A3"] == None)
    #         and (assignment["B1"] != assignment["B2"] or assignment["B1"] == None or assignment["B2"] == None)
    #         and (assignment["B1"] != assignment["B3"] or assignment["B1"] == None or assignment["B3"] == None)
    #         and (assignment["B2"] != assignment["B3"] or assignment["B2"] == None or assignment["B3"] == None)
    #         and (assignment["C1"] != assignment["C2"] or assignment["C1"] == None or assignment["C2"] == None)
    #         and (assignment["C1"] != assignment["C3"] or assignment["C1"] == None or assignment["C3"] == None)
    #         and (assignment["C2"] != assignment["C3"] or assignment["C2"] == None or assignment["C3"] == None)
    #         and (assignment["A1"] != assignment["B1"] or assignment["A1"] == None or assignment["B1"] == None)
    #         and (assignment["A1"] != assignment["C1"] or assignment["A1"] == None or assignment["C1"] == None)
    #         and (assignment["B1"] != assignment["C1"] or assignment["B1"] == None or assignment["C1"] == None)
    #         and (assignment["A2"] != assignment["B2"] or assignment["A2"] == None or assignment["B2"] == None)
    #         and (assignment["A2"] != assignment["C2"] or assignment["A2"] == None or assignment["C2"] == None)
    #         and (assignment["B2"] != assignment["C2"] or assignment["B2"] == None or assignment["C2"] == None)
    #         and (assignment["A3"] != assignment["B3"] or assignment["A3"] == None or assignment["B3"] == None)
    #         and (assignment["A3"] != assignment["C3"] or assignment["A3"] == None or assignment["C3"] == None)
    #         and (assignment["B3"] != assignment["C3"] or assignment["B3"] == None or assignment["C3"] == None)
    #              )

    # def isAssigComplete(self, assignment_input):
    #     assignment = assignment_input
    #     return (self.isAssigConsistent(assignment_input)
    #             and assignment["A1"] != None
    #             and assignment["A2"] != None
    #             and assignment["A3"] != None
    #             and assignment["B1"] != None
    #             and assignment["B2"] != None
    #             and assignment["B3"] != None
    #             and assignment["C1"] != None
    #             and assignment["C2"] != None
    #             and assignment["C3"] != None
    #             )





