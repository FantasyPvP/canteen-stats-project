
import random

def generateUsers(num, options):
    students = []
    for i in range(num):
        students.append(Student(i, options))
    return(students)






class Student():
    def __init__(self, index, options):
        self.name = (str(random.randint(1,100000)))
        self.index = index
        self.meal = random.choice(options)
        self.year = random.randint(7,11)


