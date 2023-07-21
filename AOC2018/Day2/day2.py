from collections import Counter

#Get data from text file
data = open("AOC2018/Day2/test.txt", "r").read().split("\n")
three = 0
two = 0
boxes = []
for line in data:
    counting = Counter(line)
    values = counting.values()
    if 2 in values:
        two += 1
        boxes.append(line)
    if 3 in values:
        three += 1
        boxes.append(line)
    if 2 in values and 3 in values:
        boxes.remove(line)

checksum = two * three
print("Part 1: " + str(checksum))
print(boxes)