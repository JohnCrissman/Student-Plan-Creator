from py.Student import Student
from py.Display import Display
import csv


def main():
    # stu = Student('n_info.txt')
    # stu = Student('n_info2.txt')
    sol = [{"S1C1": "CS400",
                         "S1C2": "CS404",
                         "S1C3": "CS331",
                         "S2C1": "CS401",
                         "S2C2": "CS335",
                         "S2C3": "CS33333",
                         "S3C1": "CS44444",
                         "S3C2": "CS55555",
                         "S3C3": "CS66666",
                         "S4C1": "CS77777",
                         "S4C2": "CS420",
                         "S4C3": "CS490"},
                       {"S1C1": "CS400",
                        "S1C2": "CS404",
                        "S1C3": "CS331",
                        "S2C1": "CS401",
                        "S2C2": "CS335",
                        "S2C3": "CS33333",
                        "S3C1": "CS44444",
                        "S3C2": "CS55555",
                        "S3C3": "CS66666",
                        "S4C1": "CS77777",
                        "S4C2": "CS420",
                        "S4C3": "CS490"}]

    solution = Display(sol, 'n_schedule.csv')

if __name__ == '__main__':
    main()