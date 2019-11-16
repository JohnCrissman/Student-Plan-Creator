class CoursesOffered:
    # let's assume the student will start in the Fall or the Spring.  They will not START in the Summer.
    # instantiate

    # use the schedule (fall, summer, spring, odd, even) that was uploaded in Piazza.

    def __init__(self):
        self.schedule = self.getSchedule(self)

    def getSummerOdd(self):
        # return a list of summer odd classes

    def getFallOdd(self):
        # return a list of fall odd classes

    def getSpringEven(self):
        # return a list of spring even classes

    def getSummerEven(self):
        # return a list of summer even classes

    def getFallEven(self):
        # return a list of fall even classes

    def getSpringOdd(self):
        # return a list of spring odd classes

    def getSchedule(self):
        # return a dictionary structured like below...
        #    dict = { "fall_odd": [list of the classes],
        #             "spring_even": [list of the classes],
        #             "summer_even": [list of the classes],... etc..


    def getDomainForVariables(self, csp_object):
        print("here")
        # Return a dictionary with the variables and their appropriate domain using the schedule and user input!
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