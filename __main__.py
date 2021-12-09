
# imports all libraries necessary for the project in addition to other code files in the project
import statistics
import math
import time
import random
import matplotlib.pyplot as plt
import user_generator







# the main function of the file that is called when the program starts by the if __name__ == "__main__" statement at the bottom of the page

def main():    

    # initialises the grapher and dataset objects

    grapher = Grapher()
    dataSet = DataSet()

    # generates a list of students with a unique index that is iterated for each student added, a random meal, number (name) and random year group
    students = user_generator.generateUsers(16000, ["mainMeal", "panini", "pastaKing", "sandwich", "pastaBowl", "hotDog", "burger", "garlicBread", "cookie", "cake" , "biscuits", "waffle"])
    
    # creates a 2d array (basically a list full of lists)
    record = [
        [],
        [],
        [],
        []
    ]   
    

    # outputs the details of the students and iterates the dataset object
    # this updates the counter for the frequency of meals eaten using the information from the student
    i = 0
    for student in students:
        print(student.name, student.index, student.meal)
        dataSet.iterate(student.meal)

    print(dataSet.mealsEaten)


    # plots a graph of the frequencies of meals eaten
    xValues = []
    yValues = []

    for x in dataSet.mealsEaten.keys():
        xValues.append(x)
    for y in dataSet.mealsEaten.values():
        yValues.append(y)
    # this is the function that plots the graph of the results
    grapher.barChartPlotter(xValues, yValues)





    #positions = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    #keys = ["a","b","c","pasta king","e","f","g","h","i","j","a","b","c","d","e","f","g","h","i","j"]
    #values = []
    #grapher = Grapher()
    #grapher.barChartPlotter(keys,randomvalues(20, [1,30]))
    #grapher.lineGraphPlotter(positions,randomvalues(20, [20,30]))
    return








# this object / class plots graphs, input an x and y value for the graph

class Grapher():
    def __init__(self):
        pass

    # plots a bar chart using an x and y input
    def barChartPlotter(self,x,y):
        plt.bar(x,y)
        plt.xlabel("item")
        plt.ylabel("frequency")
        plt.title("frequency of meals sold in the canteen")
        plt.show()

    # plots a line graph using an x and y input
    def lineGraphPlotter(self,x,y):
        plt.plot(x,y)
        plt.xlabel("item")
        plt.ylabel("frequency")
        plt.title("frequency of meals sold in the canteen")
        plt.show()










class DataObject():
    def __init__(self, keys, values):
        self.keys = keys
        self.values = values
















# generates a list of random values (the number of values in the list is equal to the "num" variable) 
# the value will be in the range "numRange" which is 2 values a minimum and a maximum


def randomvalues(num, numRange):
    values = []
    for i in range(num):
        values.append(random.randint(numRange[0], numRange[1]))
    return(values)













# this is the dataset class for the program that stores the most important data for the program.
# it records the data using a dictionary (surrounded by {} brackets)

class DataSet():

    # sets all of the frequencies for each meal to 0
    def __init__(self):
        self.mealsEaten = {
            "mainMeal" : 0,
            "panini" : 0,
            "pastaKing" : 0,
            "sandwich" : 0,
            "pastaBowl" : 0,
            "hotDog" : 0,
            "burger" : 0,
            "garlicBread" : 0,
            "cookie" : 0,
            "cake" : 0,
            "biscuits" : 0,
            "waffle" : 0
        }

    # iterates the number for the meal that the student has eaten for each
    def iterate(self, meal):
        if meal == "mainMeal":
            self.mealsEaten["mainMeal"] += 1
        if meal == "panini":
            self.mealsEaten["panini"] += 1
        if meal == "pastaKing":
            self.mealsEaten["pastaKing"] += 1
        if meal == "sandwich":
            self.mealsEaten["sandwich"] += 1
        if meal == "pastaBowl":
            self.mealsEaten["pastaBowl"] += 1
        if meal == "hotDog":
            self.mealsEaten["hotDog"] += 1
        if meal == "burger":
            self.mealsEaten["burger"] += 1
        if meal == "garlicBread":
            self.mealsEaten["garlicBread"] += 1
        if meal == "cookie":
            self.mealsEaten["cookie"] += 1
        if meal == "cake":
            self.mealsEaten["cake"] += 1
        if meal == "biscuits":
            self.mealsEaten["biscuits"] += 1
        if meal == "waffle":
            self.mealsEaten["waffle"] += 1



















# this statement starts the main() function of the file if the name of the program is __main__ (which it is)
# this is common practice for object oriented programming as it gives the program a clear entry point

if __name__ == "__main__":
    main()