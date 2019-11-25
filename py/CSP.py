from py.CoursesOffered import CoursesOffered

class CSP:
    def __init__(self):
        self.variables = self.get_variables()
        self.domains = self.getDomains()
        self.num_constraints = self.get_constraints_updated_so_far({})
        self.courses_offered = CoursesOffered()

    def get_variables(self):
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

    def get_constraints_updated_so_far(self, constraints):
        # TODO: load the contraints given the asignment
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

