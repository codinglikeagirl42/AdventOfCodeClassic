#Get data from text file
data = open("AOC2019/Day2/day2.txt", "r").read().split(",")

data[1] = 12
data[2] = 2
def intcode(data):
    for opcode in range(0, len(data), 4):
        opcode = int(opcode)
        what_to_do = int(data[opcode])
        input_1 = int(data[opcode + 1])
        input_2 = int(data[opcode + 2])
        where_to_put = int(data[opcode + 3])

        if what_to_do == 1:
            data[where_to_put] = int(data[input_1]) + int(data[input_2])
        elif what_to_do == 2:
            data[where_to_put] = int(data[input_1]) * int(data[input_2])
        else:
            print(what_to_do)
            return(data)

answer = intcode(data)
print(answer)

