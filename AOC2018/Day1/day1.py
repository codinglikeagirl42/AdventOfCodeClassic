#Get data from text file
data = open("AOC2018/Day1/day1.txt", "r").read().split("\n")

"""
for line in data:
    print(line)
"""
frequency = 0
for line in data:
    frequency += int(line)
print("Part 1: " + str(frequency))

