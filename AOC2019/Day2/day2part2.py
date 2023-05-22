#Get data from text file
data = open("AOC2019/Day2/day2.txt", "r").read().split(",")

def pairs_needed(data):

    for noun in range(100):
        for verb in range(100):

            data[1] = noun
            data[2] = verb
    
            answer = intcode(data)
            
    if answer == 19690720:
        return(100 * noun + verb)
           


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
            return data[0]
        
answer_2 = pairs_needed(data)
print("Part 2: " + str(answer_2))