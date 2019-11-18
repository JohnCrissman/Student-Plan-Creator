

class Student:

    def __init__(self, semester, year, solution, filename, list_of_classes):
        self.semester = semester
        self.year = year
        self.solution = solution
        self.filename = filename
        self.list_of_classes = list_of_classes

    @staticmethod
    def load(self, filename):
        print("This load file to student object")

    def get_semester(self):
        return self.semester

    def set_semester(self):
        return self.semester

    def get_year(self):
        return self.year

    def set_year(self):
        return self.year

    def get_filename(self):
        return self.filename

    def set_filename(self):
        return self.filename

    def get_list_of_classes(self):
        return self.list_of_classes

    def set_list_of_classes(self):
        return self.list_of_classes
