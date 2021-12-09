
import random

# generates a list of user profiles for the number of students "num" by iterating until a set number of students have been created
# the students will each be chosen a random meal out of the parameter "options" which is a list of meals
def generateUsers(num, options):
    students = []
    for i in range(num):
        students.append(Student(i, options))
    return(students)




# the class that creates the student object where the information about each student is stored

# name is a random number between 1 and 100000 (unnecessary but just as an example of some of the data that the program might be inputted with even if its not used)
# index is a unique identifier for each student, it iterates by 1 for each student that is created 
# meal is a random choice of meal from the options that are given to it as a parameter
# year is just a year between 7 and 11 so that we can look at purchase patterns between different year groups

class Student():
    def __init__(self, index, options):
        self.name = (str(random.randint(1,100000)))
        self.index = index
        self.meal = random.choice(options)
        self.year = random.randint(7,11)


