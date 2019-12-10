
class Student:

    # TODO: read the text file

    def __init__(self, filename):
        if len(filename) == 0:
            raise FileNotFoundError
        self.filename = filename
        self.filepath = '../resources/' + self.filename
        self.semester = None
        self.year = None
        self.number_of_classes = None
        self.list_of_classes = list()

        self.load()

    def load(self):
        with open(self.filepath) as file:
            content = file.readlines()
            content = [x.rstrip() for x in content]
            self.semester = content.pop(0).upper()
            self.year = content.pop(0)
            self.number_of_classes = content.pop(0)
            self.list_of_classes = content

        #print(content)
        # print(self.semester)
        # print(self.year)
        # print(self.number_of_classes)
        #print(len(self.list_of_classes))
        # print(self.list_of_classes)