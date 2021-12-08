
import statistics
import math
import time
import random
import matplotlib.pyplot as plt









def main():
    positions = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    keys = ["a","b","c","pasta king","e","f","g","h","i","j","a","b","c","d","e","f","g","h","i","j"]
    values = []
    grapher = Grapher()
    grapher.barChartPlotter(keys,randomvalues(20, [1,30]))


class Grapher():
    def __init__(self):
        pass

    def barChartPlotter(x,y):
        plt.bar(x,y)
        plt.xlabel("item")
        plt.ylabel("frequency")
        plt.title("frequency of meals sold in the canteen")
        plt.show()

    def lineGraphPlotter(x,y):
        plt.plot(x,y)
        plt.xlabel("item")
        plt.ylabel("frequency")
        plt.title("frequency of meals sold in the canteen")
        plt.show()





class DataObject():
    def __init__(self, keys, values):
        self.keys = keys
        self.values = values




def randomvalues(num, range):
    values = []
    for i in range(num):
        values.append(random.randint(range[0], range[1]))
    return(values)















if __name__ == "__main__":
    main()