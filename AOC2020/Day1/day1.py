#Get data from text file
data = open("AOC2020/Day1/day1.txt", "r").read().split("\n")
#Code does not account for multiplies
for line in data:
    for lines in data:
        if int(line) + int(lines) == 2020:
            print("Part 1: " + str((int(line)) * (int(lines))))
        for more_lines in data:
            if int(line) + int(lines) + int(more_lines) == 2020:
                print("Part 2: " + str((int(line)) * (int(lines)) * (int(more_lines))))