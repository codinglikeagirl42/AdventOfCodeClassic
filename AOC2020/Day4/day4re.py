import re

#Get data from text file, blank line is just two new lines.
data = open("AOC2020/Day4/day4.txt", "r").read().split("\n\n")

passports_valid = []
new_passport_valid = 0

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
#part 2       

eye_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
for passport in passports_valid:
    sorted_passport = sorted(passport)
    eye_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    pieces = []
    new_count = 0
    eye_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    for items in sorted_passport:
        pieces.append(items[4:])  
    if 1920 <= int(pieces[0]) <= 2002:
        new_count += 1
    if pieces[1] in eye_colors:
        new_count += 1
    if 2020 <= int(pieces[2]) <= 2030:
        new_count += 1
    if len(pieces[3]) == 7 and pieces[3][0] == "#":
        #https://docs.python.org/3/howto/regex.html#regex-howto
        if re.match("^[0-9a-f${6}]", pieces[3][1:]):
            new_count += 1
    if pieces[4][-2:] == "cm" and 150 <= int(pieces[4][:-2])<=193:
        new_count += 1
    if pieces[4][-2:] == "in" and 59 <= int(pieces[4][:-2])<=76:
        new_count += 1
    if 2010 <= int(pieces[5]) <= 2020:
        new_count += 1
    if re.match("^[0-9${9}]", pieces[6]) and len(pieces[6]) == 9:
        new_count += 1
    if new_count == 7:
        new_passport_valid += 1 
print("Part 1: " + str(len(passports_valid)))
print("Part 2: " + str(new_passport_valid))
 