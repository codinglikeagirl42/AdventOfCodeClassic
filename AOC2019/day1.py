#Get data from text file
data = open("AOC2019/day1.txt", "r").read().split("\n")

from math import floor
#https://favtutor.com/blogs/round-down-python#:~:text=Python%27s%20floor%20division%20operator%2C%20aka,with%20the%20floor()%20method.

fuel_need = 0
fuel_per_module = []
for number in data:
    
    fuel_need += ((floor((int(number))/3)) - 2)
    fuel_per_module.append((floor((int(number))/3)) - 2)

all_fuel_need = []
for module in fuel_per_module:
    extra_fuel = 0
    current_fuel = module
    need_more = True
    while need_more == True:
        extra_fuel += ((floor((int(current_fuel))/3)) - 2)
        current_fuel = ((floor((int(current_fuel))/3)) - 2)
        if current_fuel < 9:
            need_more = False
    all_fuel_need.append(extra_fuel)
print("Part1: " + str(fuel_need))
print("Part2: " + str(sum(all_fuel_need)))