from py.Student import Student

class CoursesOffered:

    def __init__(self, student):
        self.student = student
        self.semesters = self.get_semesters()


    def get_semesters(self):
        list_of_semesters = ["FALL_EVEN", "SPRING_ODD", "SUMMER_ODD",
                             "FALL_ODD", "SPRING_EVEN", "SUMMER_EVEN"]
        int_year = int(self.student.year)
        if (int_year % 2 == 0):
            semester_year = "EVEN"
        else:
            semester_year = "ODD"
        if self.student.semester == 'SUMMER':
            self.student.semester = 'FALL'
        starting_semester = self.student.semester + "_" + semester_year
        index = list_of_semesters.index(starting_semester)
        scheduled_semesters = []
        while len(scheduled_semesters) < 4:
            if index < 6:
                scheduled_semesters.append(list_of_semesters[index])
            else:
                index = 0
                scheduled_semesters.append(list_of_semesters[index])
            index = index + 1
        return(scheduled_semesters)

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
        return ["CS327", "CS331", "CS335", "CS355", "CS400", "CS401", "CS404",
                "CS413", "CS415", "CS417", "CS419", "CS442", "CS490"]

    def get_category_1(self):
        return ["CS331", "CS345", "CS355", "CS442", "CS460"]

    def get_category_2(self):
        return ["CS401", "CS411", "CS412", "CS413"]

    def get_category_3(self):
        return ["CS335", "CS415", "CS416", "CS419"]

    def get_domain_for_variables(self):
        courses_to_domains, our_semesters = self.initialize_domain_for_vars()

        list_cat_1 = self.get_category_1()
        list_cat_2 = self.get_category_2()
        list_cat_3 = self.get_category_3()

        self.compare_domain_to_categories(courses_to_domains, list_cat_1, list_cat_2, list_cat_3, our_semesters)
        print("Here is our CSP ------------------------------------------------------------------------")
        print(courses_to_domains)
        print("That was our CSP -----------------------------------------------------------------------")
        return courses_to_domains

    def compare_domain_to_categories(self, courses_to_domains, list_cat_1, list_cat_2, list_cat_3, our_semesters):
        if "SPRING" in our_semesters[0]:
            print("spring")
            s3c1_list = []
            for i in list_cat_1:
                if i in courses_to_domains["S3C1"]:
                    s3c1_list.append(i)
            courses_to_domains["S3C1"] = s3c1_list
            s3c2_list = []
            for i in list_cat_2:
                if i in courses_to_domains["S3C2"]:
                    s3c2_list.append(i)
            courses_to_domains["S3C2"] = s3c2_list
            s3c3_list = []
            for i in list_cat_3:
                if i in courses_to_domains["S3C3"]:
                    s3c3_list.append(i)
            courses_to_domains["S3C3"] = s3c3_list
        elif "FALL" in our_semesters[0]:
            print("fall")
            s2c1_list = []
            for i in list_cat_1:
                if i in courses_to_domains["S2C1"]:
                    s2c1_list.append(i)
            courses_to_domains["S2C1"] = s2c1_list
            s2c2_list = []
            for i in list_cat_2:
                if i in courses_to_domains["S2C2"]:
                    s2c2_list.append(i)
            courses_to_domains["S2C2"] = s2c2_list
            s2c3_list = []
            for i in list_cat_3:
                if i in courses_to_domains["S2C3"]:
                    s2c3_list.append(i)
            courses_to_domains["S2C3"] = s2c3_list

    def initialize_domain_for_vars(self):
        courses_to_domains = {"S1C1": ["CS400"],
                              "S1C2": ["CS404"],
                              "S1C3": None,
                              "S2C1": None,
                              "S2C2": None,
                              "S2C3": None,
                              "S3C1": None,
                              "S3C2": None,
                              "S3C3": None,
                              "S4C1": None,
                              "S4C2": ["CS420"],
                              "S4C3": ["CS490"]
                              }
        our_semesters = self.semesters
        courses_to_semesters = {"S1C1": our_semesters[0],
                                "S1C2": our_semesters[0],
                                "S1C3": our_semesters[0],
                                "S2C1": our_semesters[1],
                                "S2C2": our_semesters[1],
                                "S2C3": our_semesters[1],
                                "S3C1": our_semesters[2],
                                "S3C2": our_semesters[2],
                                "S3C3": our_semesters[2],
                                "S4C1": our_semesters[3],
                                "S4C2": our_semesters[3],
                                "S4C3": our_semesters[3]
                                }
        for k, v in courses_to_semesters.items():
            if v == "FALL_ODD" and k != "S1C1" and k != "S1C2" and k != "S4C2" and k != "S4C3":
                courses_to_domains[k] = self.get_fall_odd()
            elif v == "SPRING_EVEN" and k != "S1C1" and k != "S1C2" and k != "S4C2" and k != "S4C3":
                courses_to_domains[k] = self.get_spring_even()
            elif v == "SUMMER_EVEN" and k != "S1C1" and k != "S1C2" and k != "S4C2" and k != "S4C3":
                courses_to_domains[k] = self.get_summer_even()
            elif v == "FALL_EVEN" and k != "S1C1" and k != "S1C2" and k != "S4C2" and k != "S4C3":
                courses_to_domains[k] = self.get_fall_even()
            elif v == "SPRING_ODD" and k != "S1C1" and k != "S1C2" and k != "S4C2" and k != "S4C3":
                courses_to_domains[k] = self.get_spring_odd()
            elif v == "SUMMER_ODD" and k != "S1C1" and k != "S1C2" and k != "S4C2" and k != "S4C3":
                courses_to_domains[k] = self.get_summer_odd()
        return courses_to_domains, our_semesters

