#Get data from text file
data = open("AOC2020/Day1/day1.txt", "r").read().split("\n")

part1 = 0
part2 = 0
for line in data:
    for lines in data:
        if int(line) + int(lines) == 2020:
            part1 =  (int(line)) * (int(lines))
        for more_lines in data:
            if int(line) + int(lines) + int(more_lines) == 2020:
                part2 = (int(line)) * (int(lines)) * (int(more_lines))

print("Part 1: " + str(part1))
print("Part 2: " + str(part2))
