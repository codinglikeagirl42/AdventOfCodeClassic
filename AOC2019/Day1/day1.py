#Get data from text file
data = open("AOC2019/Day1/day1.txt", "r").read().split("\n")

from math import floor
#https://favtutor.com/blogs/round-down-python#:~:text=Python%27s%20floor%20division%20operator%2C%20aka,with%20the%20floor()%20method.

fuel_need = 0

for number in data:
    
    fuel_need += ((floor((int(number))/3)) - 2)

all_fuel_need = []
for module in data:
    extra_fuel = 0
    need_more = False
    while need_more == False:
        extra_fuel += ((floor((int(module))/3)) - 2)
        print(extra_fuel)
        module = ((floor((int(module))/3)) - 2)
        if module < 9:
            need_more = True
    all_fuel_need.append(extra_fuel)
    
print("Part1: " + str(fuel_need))
print("Part2: " + str(sum(all_fuel_need)))