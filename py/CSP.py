from py.CoursesOffered import CoursesOffered


class CSP:
    def __init__(self, student):
        self.variables = self.get_variables()
        self.num_constraints = self.get_constraints_updated_so_far({})
        self.courses_offered = CoursesOffered(student)
        self.domains = self.get_domains()

    def get_variables(self):
        return ["S1C1", "S1C2", "S1C3", "S2C1", "S2C2", "S2C3",
                "S3C1", "S3C2", "S3C3", "S4C1", "S4C2", "S4C3"]

    def get_domains(self):
        my_domains = self.courses_offered.get_domain_for_variables()
        print("\nDomains: \n", my_domains)
        return my_domains

    def get_constraints_updated_so_far(self, current_assignment):
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

        return self.__check_consistency(assignment1)

    def __check_consistency(self, assignment):
        unique_values = list()
        for value in assignment.values():
            if value not in unique_values or value is None:
                unique_values.append(value)
        # print(assignment, "      ",unique_values)
        return len(assignment) == len(unique_values)

    def is_assign_complete(self, assignment_input):
        return (self.__check_consistency(assignment_input)
                and len(assignment_input) == len(self.variables)
                )

