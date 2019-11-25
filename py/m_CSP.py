

class CSP:
    def __init__(self):
        self.variables = ["mari", "valor", "thing", "word", "maps"]
        self.domains = {"mari": ["CS400", "CS404"],
                        "valor": ["CS404", "CS411", "CS345"],
                        "thing": ["CS331", "CS411", "CS345", "CS355", "CS442", "CS460"],
                        "word": ["CS401", "CS411", "CS412", "CS413"],
                        "maps": ["CS335", "CS415", "CS416", "CS419", "CS400"]
                        }
        self.constraints = self.get_constaints_updated_so_far({})
        self.num_constraints = {'mari': 7, 'valor': 12, 'thing': 14, 'word': 7, 'maps': 3}

    # def get_variables_updated_so_far(self, assignment):
    #     # TODO: return new variables given the assignment
    #     new_variables = self.variables[:]
    #     for k, v in assignment.items():
    #         print("k,v: (", k, ",", v, ")\t ")
    #         new_variables.remove(k)
    #         print(new_variables)
    #     return new_variables

    def get_domain_updated_so_far(self, assignment):
        # TODO: return new domain based on the assignment
        return {"mari": ["CS400"],
                "valor": ["CS404"],
                "thing": ["CS331", "CS345", "CS355", "CS442", "CS460"],
                "word": ["CS401", "CS411", "CS412", "CS413"],
                "maps": ["CS335", "CS415", "CS416", "CS419"]
                }

    def get_constaints_updated_so_far(self, constraints):
        # TODO: load the contraints given the asignment

        return {'mari': 14, 'valor': 1, 'thing': 14, 'word': 7, 'maps': 3}


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




# ########################################################################################
# # Demo / Test of Backtracking class
'''

assignment0 = {}
assignment1 = {"S1C1": "CS400",
               "S1C2": "CS404",
               "S4C1": "CS420",
               "S4C2": "CS490",
               "S4C3": "CS455"
              }
assignment2 = {"S1C1": "CS400",
               "S1C2": "CS404",
               "S1C3": "CS335",
               "S2C1": "CS404",
              }
assignment3 = {"S1C1": "CS400",
               "S1C2": "CS404",
               "S1C3": "CS460",
               "S2C1": "CS401",
               "S2C2": "CS331",
               "S2C3": "CS335",
               "S3C1": "CS450",
               "S3C2": "CS445",
               "S3C3": "CS5000",
               "S4C1": "CS420",
               "S4C2": "CS490",
               "S4C3": "CS455"
              }

num_constraints = {"S1C1": [7, 8, 9],
                   "S1C2": [7, 8, 9],
                   "S1C3": [7, 8, 9],
                   "S2C1": [7, 8, 9],
                   "S2C2": [7, 8, 9],
                   "S2C3": [7, 8, 9],
                   "S3C1": [7, 8, 9],
                   "S3C2": [7, 8, 9],
                   "S3C3": [7, 8, 9],
                   "S4C1": [],
                   "S4C2": [],
                   "S4C3": []
                  }



# csp0 = CSP(num_constraints)
# csp1 = CSP(num_constraints)
# csp2 = CSP(num_constraints)
# csp3 = CSP(num_constraints)
# print("Consistency")
# print(csp3.isAssigConsistent(assignment2)) #False
# print(csp3.isAssigConsistent(assignment0)) #True
# print(csp3.isAssigConsistent(assignment1)) #True
# print(csp3.isAssigConsistent(assignment3)) #True


'''