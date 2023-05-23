#Get data from text file
data = open("AOC2019/Day2/day2.txt", "r").read().split(",")

# https://www.educative.io/answers/how-to-copy-a-list-in-python

def intcode(test_data):
    for opcode in range(0, (len(test_data)-4), 4):
        
        opcode = int(opcode)
        what_to_do = int(test_data[opcode])
        input_1 = int(test_data[opcode + 1])
        input_2 = int(test_data[opcode + 2])
        
        if what_to_do == 99:
            return test_data
        
        #where_to_put = int(test_data[opcode + 3])

        if what_to_do == 1:
            test_data[int(test_data[opcode + 3])] = int(test_data[input_1]) + int(test_data[input_2])
        if what_to_do == 2:
            test_data[int(test_data[opcode + 3])] = int(test_data[input_1]) * int(test_data[input_2])
        #else:
            #return test_data[0]
  
#Part 1
test_data = data[:]
test_data[1] = 12
test_data[2] = 2
       
answer = intcode(test_data)
print("Part 1: " + str(answer[0]))


for noun in range(100):
    for verb in range(100):

        test_data = data[:]
        test_data[1] = noun
        test_data[2] = verb

        #print(test_data[0:3])
        check = intcode(test_data)
        #print(check[0])
        if check[0] == 19690720:
            print("Part 2: " + str(100 * noun + verb))
           
                      