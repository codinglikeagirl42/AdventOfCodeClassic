import re

#Get data from text file, blank line is just two new lines.
data = open("AOC2020/Day4/day4.txt", "r").read().split("\n\n")

documentation = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid",]
"""
byr (Birth Year) - four digits; at least 1920 and at most 2002.
iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
hgt (Height) - a number followed by either cm or in:
If cm, the number must be at least 150 and at most 193.
If in, the number must be at least 59 and at most 76.
hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeroes.
"""
valid_passports = []
passport_valid = 0
for item in data:
    new_items = item.split( )
    pieces = []
    for items in new_items:
        pieces.append(items[:3])
    
    #print(pieces)   
    count = 0
    for piece in pieces:
        #print(piece)
        if piece in documentation:
            count += 1
            #print(count)
    if count == 7:
        passport_valid += 1
        valid_passports.append(new_items)
#print(valid_passports)
#print("Part 1: " + str(passport_valid))

new_passport_valid = 0
for passport in valid_passports:
    sorted_passport = sorted(passport)
    if len(sorted_passport) == 8:
        del sorted_passport[1]
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
    print(new_count)
print(new_passport_valid)   
   