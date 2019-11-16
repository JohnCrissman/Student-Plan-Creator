class CSP:
    def __init__(self, num_constraints_for_each):
        self.variables = self.getVariables()
        self.domain = self.getDomains()
        self.num_constraints_for_each = num_constraints_for_each

    def getVariables(self):
        return ["S1C1", "S1C2", "S1C3", "S2C1", "S2C2", "S2C3",
                "S3C1", "S3C2", "S3C3", "S4C1", "S4C2", "S4C3"]

    def getDomains(self):
        return {"S1C1": ["CS400"],
                "S1C2": ["CS404"],
                "S1C3": ["CS331", "CS345", "CS355", "CS442", "CS460"],
                "S2C1": ["CS401", "CS411", "CS412", "CS413"],
                "S2C2": ["CS335", "CS415", "CS416", "CS419"],
                "S2C3": ["CS33333"],
                "S3C1": ["CS44444"],
                "S3C2": ["CS55555"],
                "S3C3": ["CS66666"],
                "S4C1": ["CS77777"],
                "S4C2": ["CS420"],
                "S4C3": ["CS490"]
                }

    def isAssigConsistent(self, assignment_input):
        assignment = assignment_input
        unique_values = list()
        for value in assignment.values():
            if value not in unique_values or value is None:
                unique_values.append(value)
        # print(assignment, "      ",unique_values)
        return len(assignment) == len(unique_values)

    def isAssigComplete(self, assignment_input):
        assignment = assignment_input
        return (self.isAssigConsistent(assignment_input)
                and assignment["S1C1"] != None
                and assignment["S1C2"] != None
                and assignment["S1C3"] != None
                and assignment["S2C1"] != None
                and assignment["S2C2"] != None
                and assignment["S2C3"] != None
                and assignment["S3C1"] != None
                and assignment["S3C2"] != None
                and assignment["S3C3"] != None
                and assignment["S4C1"] != None
                and assignment["S4C2"] != None
                and assignment["S4C3"] != None
                )
 #########################################################################################
## Demo / Test of Backtracking class


assignment0 = {"S1C1": None,
               "S1C2": None,
               "S1C3": None,
               "S2C1": None,
               "S2C2": None,
               "S2C3": None,
               "S3C1": None,
               "S3C2": None,
               "S3C3": None,
               "S4C1": None,
               "S4C2": None,
               "S4C3": None
              }
assignment1 = {"S1C1": "CS400",
               "S1C2": "CS404",
               "S1C3": None,
               "S2C1": None,
               "S2C2": None,
               "S2C3": None,
               "S3C1": None,
               "S3C2": None,
               "S3C3": None,
               "S4C1": "CS420",
               "S4C2": "CS490",
               "S4C3": "CS455"
              }
assignment2 = {"S1C1": "CS400",
               "S1C2": "CS404",
               "S1C3": "CS335",
               "S2C1": "CS404",
               "S2C2": None,
               "S2C3": None,
               "S3C1": None,
               "S3C2": None,
               "S3C3": None,
               "S4C1": None,
               "S4C2": None,
               "S4C3": None
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



csp0 = CSP(num_constraints)
csp1 = CSP(num_constraints)
csp2 = CSP(num_constraints)
csp3 = CSP(num_constraints)
print("Consistency")
print(csp3.isAssigConsistent(assignment2)) #False
print(csp3.isAssigConsistent(assignment0)) #True
print(csp3.isAssigConsistent(assignment1)) #True
print(csp3.isAssigConsistent(assignment3)) #True

print("Completeness")
print(csp3.isAssigComplete(assignment3)) #True
print(csp3.isAssigComplete(assignment1)) #False