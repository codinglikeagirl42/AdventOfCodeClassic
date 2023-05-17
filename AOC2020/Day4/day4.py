#Get data from text file, blank line is just two new lines.
data = open("AOC2020/Day4/day4.txt", "r").read().split("\n\n")

documentation = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid",]

passport_valid = 0
for item in data:
    new_items = item.split( )
    pieces = []
    for items in new_items:
        pieces.append(items[:3])
    
    print(pieces)   
    count = 0
    for piece in pieces:
        #print(piece)
        if piece in documentation:
            count += 1
            print(count)
    if count == 7:
        passport_valid += 1
print("Part 1: " + str(passport_valid))