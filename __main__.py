
import statistics
import math
import time
import random
import matplotlib.pyplot as plt
import user_generator









def main():    
    students = user_generator.generateUsers(16000, ["pasta","cookie","main meal","cake","panini","burger","hotdog","waffle"])
    for student in students:
        print(student.name, student.index, student.meal)



    #positions = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    #keys = ["a","b","c","pasta king","e","f","g","h","i","j","a","b","c","d","e","f","g","h","i","j"]
    #values = []
    #grapher = Grapher()
    #grapher.barChartPlotter(keys,randomvalues(20, [1,30]))
    #grapher.lineGraphPlotter(positions,randomvalues(20, [20,30]))
    return


class Grapher():
    def __init__(self):
        pass

    def barChartPlotter(self,x,y):
        plt.bar(x,y)
        plt.xlabel("item")
        plt.ylabel("frequency")
        plt.title("frequency of meals sold in the canteen")
        plt.show()

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




def randomvalues(num, numRange):
    values = []
    for i in range(num):
        values.append(random.randint(numRange[0], numRange[1]))
    return(values)




if __name__ == "__main__":
    main()


class DataSet():
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

    def iterate(meal):
        
