#Get data from text file
data = open("AOC2020/Day1/day1.txt", "r").read().split("\n")

for line in data:
    for lines in data:
        if int(line) + int(lines) == 2020:
            print((int(line)) * (int(lines)))