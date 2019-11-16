class Backtracking:

    # instantiate
    def __init__(self, assignment, num_constraints_for_each):
        self.variables = self.getVariables()
        self.domain = self.getDomains()
        self.assignment = assignment
        self.num_constraints_for_each = num_constraints_for_each

    # def Backtrack(self, assignment_input):
    #     if self.isAssigComplete(assignment_input):
    #         return assignment_input
    #     self.selectUnassignedVariable(assignment_input)
    #
    # def selectUnassignedVariable(self, assignment_input):
    #     vars_after_mrv = self.MRV(assignment_input)


    def sort_by_values_len(dict):
        dict_len = {key: len(value) for key, value in dict.items()}
        import operator
        sorted_key_list = sorted(dict_len.items(), key=operator.itemgetter(1), reverse=False)
        sorted_dict = [{item[0]: dict[item[0]]} for item in sorted_key_list]
        len_smallest = 99999
        for i in sorted_dict:
            if len(sorted_dict[i]) < len_smallest:
                len_smallest = len(sorted_dict[i])

        for j in sorted_dict:
            if len_smallest < len(sorted_dict[j]):
                del sorted_dict[j]

        return sorted_dict

    def getNumConstraints(self):
        return self.num_constraints_for_each


    # def MRV(self, assignment_input):
    #     possible_variables = sort_by_values_len(assignment_input)


    def degree(self):
        return 2

    def LCV(self):
        return 3

    def getAssignment(self):
        return self.assignment

    def getVariables(self):
        return ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]

    def getDomains(self):
        return {"A1": [7, 8, 9],
                "A2": [7, 8, 9],
                "A3": [7, 8, 9],
                "B1": [7, 8, 9],
                "B2": [7, 8, 9],
                "B3": [7, 8, 9],
                "C1": [7, 8, 9],
                "C2": [7, 8, 9],
                "C3": [7, 8, 9]
                }

    def isAssigConsistent(self, assignment_input):
        assignment = assignment_input
        return ((assignment["A1"] != assignment["A2"] or assignment["A1"] == None or assignment["A2"] == None)
            and (assignment["A1"] != assignment["A3"] or assignment["A1"] == None or assignment["A3"] == None)
            and (assignment["A2"] != assignment["A3"] or assignment["A2"] == None or assignment["A3"] == None)
            and (assignment["B1"] != assignment["B2"] or assignment["B1"] == None or assignment["B2"] == None)
            and (assignment["B1"] != assignment["B3"] or assignment["B1"] == None or assignment["B3"] == None)
            and (assignment["B2"] != assignment["B3"] or assignment["B2"] == None or assignment["B3"] == None)
            and (assignment["C1"] != assignment["C2"] or assignment["C1"] == None or assignment["C2"] == None)
            and (assignment["C1"] != assignment["C3"] or assignment["C1"] == None or assignment["C3"] == None)
            and (assignment["C2"] != assignment["C3"] or assignment["C2"] == None or assignment["C3"] == None)
            and (assignment["A1"] != assignment["B1"] or assignment["A1"] == None or assignment["B1"] == None)
            and (assignment["A1"] != assignment["C1"] or assignment["A1"] == None or assignment["C1"] == None)
            and (assignment["B1"] != assignment["C1"] or assignment["B1"] == None or assignment["C1"] == None)
            and (assignment["A2"] != assignment["B2"] or assignment["A2"] == None or assignment["B2"] == None)
            and (assignment["A2"] != assignment["C2"] or assignment["A2"] == None or assignment["C2"] == None)
            and (assignment["B2"] != assignment["C2"] or assignment["B2"] == None or assignment["C2"] == None)
            and (assignment["A3"] != assignment["B3"] or assignment["A3"] == None or assignment["B3"] == None)
            and (assignment["A3"] != assignment["C3"] or assignment["A3"] == None or assignment["C3"] == None)
            and (assignment["B3"] != assignment["C3"] or assignment["B3"] == None or assignment["C3"] == None)
                 )

    def isAssigComplete(self, assignment_input):
        assignment = assignment_input
        return (self.isAssigConsistent(assignment_input)
                and assignment["A1"] != None
                and assignment["A2"] != None
                and assignment["A3"] != None
                and assignment["B1"] != None
                and assignment["B2"] != None
                and assignment["B3"] != None
                and assignment["C1"] != None
                and assignment["C2"] != None
                and assignment["C3"] != None
                )





 #########################################################################################
## Demo / Test of Backtracking class


assignment0 = {"A1": 7,
              "A2": 8,
              "A3": 9,
              "B1": 8,
              "B2": 7,
              "B3": 9,
              "C1": None,
              "C2": None,
              "C3": 7
              }
assignment1 = {"A1": 7,
              "A2": 7,
              "A3": 8,
              "B1": 8,
              "B2": 9,
              "B3": 7,
              "C1": None,
              "C2": None,
              "C3": 9
              }
assignment2 = {"A1": None,
              "A2": None,
              "A3": None,
              "B1": 7,
              "B2": 8,
              "B3": 9,
              "C1": 7,
              "C2": None,
              "C3": 8
              }
assignment3 = {"A1": 1,
              "A2": 2,
              "A3": 3,
              "B1": None,
              "B2": None,
              "B3": 9,
              "C1": 2,
              "C2": 8,
              "C3": 1
              }
assignment4 = {"A1": None,
              "A2": None,
              "A3": None,
              "B1": None,
              "B2": None,
              "B3": None,
              "C1": None,
              "C2": None,
              "C3": None
              }
num_constraints = {"A1": 4, "A2": 4, "A3": 4,
                   "B1": 4, "B2": 4, "B3": 4,
                   "C1": 4, "C2": 4, "C3": 4}



csp0 = Backtracking(assignment0, num_constraints)
csp1 = Backtracking(assignment1, num_constraints)
csp2 = Backtracking(assignment2, num_constraints)
csp3 = Backtracking(assignment3, num_constraints)
csp4 = Backtracking(assignment4, num_constraints)

print("testing whether assignments are consistent:")
print(csp0.isAssigConsistent(assignment0)) ## true
print(csp1.isAssigConsistent(assignment1)) ## false
print(csp2.isAssigConsistent(assignment2)) ## false
print(csp3.isAssigConsistent(assignment3)) ## true
print(csp4.isAssigConsistent(assignment4)) ## true

print("\ntesting whether assignments are complete and consistent!")
print(csp0.isAssigComplete(assignment0)) ## false
print(csp1.isAssigComplete(assignment1)) ## false
print(csp2.isAssigComplete(assignment2)) ## false
print(csp3.isAssigComplete(assignment3)) ## true
print(csp4.isAssigComplete(assignment4)) ## false

## let's work with assignment4 because there are no values assigned
# print(csp4.Backtrack(assignment3))


dict = {"A1": [7, 8, 9],
                "A2": [7, 8, 9],
                "A3": [7],
                "B1": [7, 8],
                "B2": [7, 8],
                "B3": [7, 8, 9],
                "C1": [7],
                "C2": [7, 8, 9],
                "C3": [7, 8, 9, 2, 1]
                }

dict= {'a': [9,2,3,4,5], 'b': [1,2,3,4, 5, 6], 'c': [], 'd': [1,2,3,4], 'e': [1,2]}
dict_temp = {'a': 'hello', 'b': 'bye', 'c': '', 'd': 'aa', 'e': 'zz'}

def sort_by_values_len(dict):
    dict_len= {key: len(value) for key, value in dict.items()}
    import operator
    sorted_key_list = sorted(dict_len.items(), key=operator.itemgetter(1), reverse=False)
    sorted_dict = [{item[0]: dict[item [0]]} for item in sorted_key_list]
    return sorted_dict

# print (sort_by_values_len(dict))
# new_dict = sort_by_values_len(dict)
# print(new_dict)

print("testing")
print(assignment3["A1"] != assignment3["A2"] != assignment3["A3"] != assignment3["B2"])
print(len(assignment3))

unique_values = list()
duplicate_values = list()
for value in assignment3.values():
    if value not in unique_values or value is None:
        unique_values.append(value)
    else:
        duplicate_values.append(value)

print("Unique values: ", unique_values)
print("Duplicate values: ", duplicate_values)
#list_of_sorted_dict = sorted(dict, key = lambda key: len(dict[key]))

#print(list_of_sorted_dict)