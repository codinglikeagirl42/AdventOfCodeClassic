#Get data from text file
data = open("AOC2019/Day2/day2.txt", "r").read().split(",")

def intcode(data, noun, verb):
    for opcode in range(0, (len(data)-4), 4):
        test_data = data
        test_data[1] = noun
        test_data[2] = verb
        print(test_data[1])
        print(test_data[2])
        opcode = int(opcode)
        what_to_do = int(test_data[opcode])
        input_1 = int(test_data[opcode + 1])
        input_2 = int(test_data[opcode + 2])
        
        if what_to_do == 99:
            return test_data[0]
        
        #where_to_put = int(test_data[opcode + 3])

        if what_to_do == 1:
            test_data[int(test_data[opcode + 3])] = int(test_data[input_1]) + int(test_data[input_2])
        if what_to_do == 2:
            test_data[int(test_data[opcode + 3])] = int(test_data[input_1]) * int(test_data[input_2])
        #else:
            #return test_data[0]
"""    
#Part 1

answer = intcode(data, 12, 2)
print("Part 1: " + str(answer))
"""
for noun in range(100):
    for verb in range(100):
        check = intcode(data, noun, verb)
        print(check)
        if check == 19690720:
            print("Part 2: " + str(100 * noun + verb))
            
 