#Get data from text file
data = open("AOC2019/day1.txt", "r").read().split("\n")

from math import floor
#https://favtutor.com/blogs/round-down-python#:~:text=Python%27s%20floor%20division%20operator%2C%20aka,with%20the%20floor()%20method.

fuel_need = 0
for number in data:
    
    fuel_need += (floor((int(number))/3))
    #print(type(floor(int(number/3)) - 2))

print("Part1: " + str(fuel_need))