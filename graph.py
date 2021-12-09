
import statistics
import math
import time
import random
import matplotlib.pyplot as grapher



def barChart(keys, values):
    for i in range(len(keys)):
        print(keys[i] + ( " " * ( 20 -  len(keys[i]) ) ) + "|   " + ("-" * values[i])) 





positions = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
keys = ["a","b","c","pasta king","e","f","g","h","i","j","a","b","c","d","e","f","g","h","i","j"]
values = []

for i in range(20):
    values.append(random.randint(0,50))

