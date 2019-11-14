

class Student:

    def __init__(self, semester, year, solution, filename, list_of_classes):
        self.semester = semester
        self.year = year
        self.solution = solution
        self.filename = filename
        self.list_of_classes = list_of_classes

    def load(self, filename):
        print("This load file to student object")



