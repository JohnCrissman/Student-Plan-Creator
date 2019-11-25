from py.Student import Student


class CoursesOffered:
    # let's assume the student will start in the Fall or the Spring.  They will not START in the Summer.
    # instantiate

    # use the schedule (fall, summer, spring, odd, even) that was uploaded in Piazza.

    def __init__(self, filename):
        self.filename = filename
        self.schedule = self.get_schedule(self.student.semester, self.student.year)
        self.student = Student(self.filename)


    def get_schedule(self, semester, year):
        list_of_semesters = ["FALL_EVEN", "SPRING_ODD", "SUMMER_ODD",
                             "FALL_ODD", "SPRING_EVEN", "SUMMER_EVEN"]
        int_year = int(year)
        if (int_year % 2 == 0):
            semester_year = "EVEN"
        else:
            semester_year = "ODD"

        starting_semester = semester + "_" + semester_year
        print(starting_semester)
        return starting_semester

    def get_summer_odd(self):
        # TODO: return a list of summer odd classes
        return ["CS331", "CS412", "CS420", "CS440", "CS490"]

    def get_fall_odd(self):
        # TODO: return a list of fall odd classes
        return ["CS325", "CS331", "CS335", "CS345", "CS400", "CS401", "CS404", "CS413",
                "CS415", "CS419", "CS460", "CS490"]

    def get_spring_even(self):
        # TODO: return a list of spring even classes
        return ["CS327", "CS331", "CS335", "CS355", "CS400", "CS404", "CS408", "CS411",
                "CS412", "CS417", "CS420", "CS442", "CS490"]

    def get_summer_even(self):
        # TODO: return a list of summer even classes
        return ["CS331", "CS401", "CS413", "CS415", "CS419", "CS490"]

    def get_fall_even(self):
        # TODO: return a list of fall even classes
        return ["CS325", "CS331", "CS335", "CS345", "CS400", "CS404", "CS412",
                "CS416", "CS420", "CS440", "CS460", "MATH305", "ECON401", "CS490"]

    def get_spring_odd(self):
        # TODO: return a list of spring odd classes
        return ["CS327", "CS331", "CS335", "CS355", "CS400", "CS401", "CS404",
                "CS413", "CS415", "CS417", "CS419", "CS442", "CS490"]

    def get_schedule(self):
        # TODO: return a dictionary structured like below...
        #    dict = { "fall_odd": [list of the classes],
        #             "spring_even": [list of the classes],
        #             "summer_even": [list of the classes],... etc..
        print('some printing to avoid broken files')
        return dict()

    def get_category_1(self):
        return ["CS331", "CS345", "CS355", "CS442", "CS460"]

    def get_category_2(self):
        return ["CS401", "CS411", "CS412", "CS413"]

    def get_category_3(self):
        return ["CS335", "CS415", "CS416", "CS419"]

    def get_domain_for_variables(self, csp_object):
        print("here")
        # TODO: Return a dictionary with the variables and their appropriate domain using the schedule and user input!
        # A CSP object will need to call this method to set it's domains according to the schedule.
        # set all variables domain's according to the schedule.
        # The schedule has courses for FALL EVEN YEAR, SPRING ODD YEAR, SUMMER ODD YEAR, FALL ODD YEAR, SPRING EVEN YEAR, and SUMMER EVEN YEAR

        # the dictionary that we need to return will be in the format below
        # The list of classes for each semester will come from that schedule table.
        # Get the starting semester and year from the Student Class which got the information from a TXT file.
        '''
            {"S1C1": ["CS400"],
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
        '''
        return list()
