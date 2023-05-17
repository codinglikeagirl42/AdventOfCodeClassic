#Get data from text file
data = open("AOC2020/Day2/day2.txt", "r").read().split("\n")

password_valid = 0
password_valid2 = 0

for line in data:

    new_line = line.split()
    line_range = (new_line[0].split("-"))
    letter_1 = new_line[2][(int(line_range[0])-1)]
    letter_2 = new_line[2][(int(line_range[1])-1)]
    line_letter = new_line[1][0]
    
     #Part 1
    count = 0
    for letter in new_line[2]:
        if letter == line_letter:
            count += 1
    
    if int(line_range[0]) <= count and count<= int(line_range[1]):
        password_valid += 1

    #Part 2
    if letter_1 != letter_2:
        if line_letter == letter_1 or line_letter == letter_2:
            password_valid2 += 1
    
print("Part 1: " + str(password_valid))
print("Part 2: " + str(password_valid2))
