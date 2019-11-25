
class Student:

    # TODO: read the text file

    def __init__(self, filename):
        self.filename = filename  # n_info.txt
        self.semester = ""
        self.year = ""
        self.number_of_classes = ""
        self.list_of_classes = []
        self.load()

    def load(self):
        with open('../resources/' + self.filename) as file:
            content = file.readlines()
            content = [x.rstrip() for x in content]
            self.semester = content.pop(0)
            self.year = content.pop(0)
            self.number_of_classes = content.pop(0)
            self.list_of_classes = content

        #print(content)
        print(self.semester)
        print(self.year)
        print(self.number_of_classes)
        #print(len(self.list_of_classes))
        print(self.list_of_classes)