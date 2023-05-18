import re

#Get data from text file, blank line is just two new lines.
data = open("AOC2020/Day4/day4.txt", "r").read().split("\n\n")

passports_valid = []

for line in data:
    new_lines = line.split( )
    count = 0
    for piece in new_lines:
        if (piece[:3]) == "cid":
            del new_lines[count]
        else:
            count += 1
    if len(new_lines) == 7:
        passports_valid.append(new_lines)
     
print("Part 1: " + str(len(passports_valid)))
 