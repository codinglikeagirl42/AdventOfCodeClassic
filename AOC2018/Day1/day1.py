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

# This part 2 solution takes a few minutes to compute, must have patience 
frequency = 0
double = [0]
is_double = False

while is_double == False:
    for item in data:
        frequency += int(item)
        if frequency in double:
            print("Part 2: " + str(frequency))
            is_double = True
            break
        else:
            double.append(frequency)
        
