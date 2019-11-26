import unittest
from py.CoursesOffered import CoursesOffered
from py.Student import Student


class TestCSP(unittest.TestCase):

    def test_should_return_correct_domain_for_fall_2019(self):
        filename = "fall_2019.txt"
        student = Student(filename)
        courses_offered = CoursesOffered(student)
        domains = courses_offered.get_domain_for_variables()
        self.assertEqual({'S1C1': ['CS400'],
                          'S1C2': ['CS404'],
                          'S1C3': ['CS325', 'CS331', 'CS335', 'CS345', 'CS400', 'CS401', 'CS404', 'CS413', 'CS415',
                                   'CS419', 'CS460', 'CS490'],
                          'S2C1': ['CS331', 'CS355', 'CS442'],
                          'S2C2': ['CS411', 'CS412'],
                          'S2C3': ['CS335'],
                          'S3C1': ['CS331', 'CS401', 'CS413', 'CS415', 'CS419', 'CS490'],
                          'S3C2': ['CS331', 'CS401', 'CS413', 'CS415', 'CS419', 'CS490'],
                          'S3C3': ['CS331', 'CS401', 'CS413', 'CS415', 'CS419', 'CS490'],
                          'S4C1': ['CS325', 'CS331', 'CS335', 'CS345', 'CS400', 'CS404', 'CS412', 'CS416', 'CS420',
                                   'CS440', 'CS460', 'MATH305', 'ECON401', 'CS490'],
                          'S4C2': ['CS420'],
                          'S4C3': ['CS490']},
                         domains, "test that should get the correct domain for fall 2019")

    def test_should_return_correct_domain_for_fall_2008(self):
        filename = "fall_2008.txt"
        student = Student(filename)
        courses_offered = CoursesOffered(student)
        domains = courses_offered.get_domain_for_variables()
        self.assertEqual({'S1C1': ['CS400'],
                          'S1C2': ['CS404'],
                          'S1C3': ['CS325', 'CS331', 'CS335', 'CS345', 'CS400', 'CS404', 'CS412', 'CS416', 'CS420',
                                   'CS440', 'CS460', 'MATH305', 'ECON401', 'CS490'],
                          'S2C1': ['CS331', 'CS355', 'CS442'],
                          'S2C2': ['CS401', 'CS413'],
                          'S2C3': ['CS335', 'CS415', 'CS419'],
                          'S3C1': ['CS331', 'CS412', 'CS420', 'CS440', 'CS490'],
                          'S3C2': ['CS331', 'CS412', 'CS420', 'CS440', 'CS490'],
                          'S3C3': ['CS331', 'CS412', 'CS420', 'CS440', 'CS490'],
                          'S4C1': ['CS325', 'CS331', 'CS335', 'CS345', 'CS400', 'CS401', 'CS404', 'CS413', 'CS415',
                                   'CS419', 'CS460', 'CS490'],
                          'S4C2': ['CS420'],
                          'S4C3': ['CS490']},
                         domains, "test that should get the correct domain for fall 2008")

    def test_should_return_correct_domain_for_spring_2019(self):
        filename = "spring_2019.txt"
        student = Student(filename)
        courses_offered = CoursesOffered(student)
        domains = courses_offered.get_domain_for_variables()
        self.assertEqual({'S1C1': ['CS400'],
                          'S1C2': ['CS404'],
                          'S1C3': ['CS327', 'CS331', 'CS335', 'CS355', 'CS400', 'CS401', 'CS404', 'CS413', 'CS415',
                                   'CS417', 'CS419', 'CS442', 'CS490'],
                          'S2C1': ['CS331', 'CS412', 'CS420', 'CS440', 'CS490'],
                          'S2C2': ['CS331', 'CS412', 'CS420', 'CS440', 'CS490'],
                          'S2C3': ['CS331', 'CS412', 'CS420', 'CS440', 'CS490'],
                          'S3C1': ['CS331', 'CS345', 'CS460'],
                          'S3C2': ['CS401', 'CS413'],
                          'S3C3': ['CS335', 'CS415', 'CS419'],
                          'S4C1': ['CS327', 'CS331', 'CS335', 'CS355', 'CS400', 'CS404', 'CS408', 'CS411', 'CS412',
                                   'CS417', 'CS420', 'CS442', 'CS490'],
                          'S4C2': ['CS420'],
                          'S4C3': ['CS490']},
                         domains, "test that should get the correct domain for spring 2019")

    def test_should_return_correct_domain_for_spring_2008(self):
        filename = "spring_2008.txt"
        student = Student(filename)
        courses_offered = CoursesOffered(student)
        domains = courses_offered.get_domain_for_variables()
        self.assertEqual({'S1C1': ['CS400'],
                          'S1C2': ['CS404'],
                          'S1C3': ['CS327', 'CS331', 'CS335', 'CS355', 'CS400', 'CS404', 'CS408', 'CS411', 'CS412', 'CS417', 'CS420', 'CS442', 'CS490'],
                          'S2C1': ['CS331', 'CS401', 'CS413', 'CS415', 'CS419', 'CS490'],
                          'S2C2': ['CS331', 'CS401', 'CS413', 'CS415', 'CS419', 'CS490'],
                          'S2C3': ['CS331', 'CS401', 'CS413', 'CS415', 'CS419', 'CS490'],
                          'S3C1': ['CS331', 'CS345', 'CS460'],
                          'S3C2': ['CS412'],
                          'S3C3': ['CS335', 'CS416'],
                          'S4C1': ['CS327', 'CS331', 'CS335', 'CS355', 'CS400', 'CS401', 'CS404', 'CS413', 'CS415', 'CS417', 'CS419', 'CS442', 'CS490'],
                          'S4C2': ['CS420'],
                          'S4C3': ['CS490']},
                         domains, "test that should get the correct domain for spring 2008")

    def test_should_return_correct_domain_for_summer_2019(self):
        filename = "summer_2019.txt"
        student = Student(filename)
        courses_offered = CoursesOffered(student)
        domains = courses_offered.get_domain_for_variables()
        self.assertEqual({'S1C1': ['CS400'],
                          'S1C2': ['CS404'],
                          'S1C3': ['CS325', 'CS331', 'CS335', 'CS345', 'CS400', 'CS401', 'CS404', 'CS413', 'CS415', 'CS419', 'CS460', 'CS490'],
                          'S2C1': ['CS331', 'CS355', 'CS442'],
                          'S2C2': ['CS411', 'CS412'],
                          'S2C3': ['CS335'],
                          'S3C1': ['CS331', 'CS401', 'CS413', 'CS415', 'CS419', 'CS490'],
                          'S3C2': ['CS331', 'CS401', 'CS413', 'CS415', 'CS419', 'CS490'],
                          'S3C3': ['CS331', 'CS401', 'CS413', 'CS415', 'CS419', 'CS490'],
                          'S4C1': ['CS325', 'CS331', 'CS335', 'CS345', 'CS400', 'CS404', 'CS412', 'CS416', 'CS420', 'CS440', 'CS460', 'MATH305', 'ECON401', 'CS490'],
                          'S4C2': ['CS420'],
                          'S4C3': ['CS490']},
                         domains, "test that should get the correct domain for summer 2019")

    def test_should_return_correct_domain_for_summer_2008(self):
        filename = "summer_2008.txt"
        student = Student(filename)
        courses_offered = CoursesOffered(student)
        domains = courses_offered.get_domain_for_variables()
        self.assertEqual({'S1C1': ['CS400'],
                          'S1C2': ['CS404'],
                          'S1C3': ['CS325', 'CS331', 'CS335', 'CS345', 'CS400', 'CS404', 'CS412', 'CS416', 'CS420', 'CS440', 'CS460', 'MATH305', 'ECON401', 'CS490'],
                          'S2C1': ['CS331', 'CS355', 'CS442'],
                          'S2C2': ['CS401', 'CS413'],
                          'S2C3': ['CS335', 'CS415', 'CS419'],
                          'S3C1': ['CS331', 'CS412', 'CS420', 'CS440', 'CS490'],
                          'S3C2': ['CS331', 'CS412', 'CS420', 'CS440', 'CS490'],
                          'S3C3': ['CS331', 'CS412', 'CS420', 'CS440', 'CS490'],
                          'S4C1': ['CS325', 'CS331', 'CS335', 'CS345', 'CS400', 'CS401', 'CS404', 'CS413', 'CS415', 'CS419', 'CS460', 'CS490'],
                          'S4C2': ['CS420'],
                          'S4C3': ['CS490']},
                         domains, "test that should get the correct domain for summer 2008")


if __name__ == '__main__':
    unittest.main()
