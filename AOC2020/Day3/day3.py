#Get data from text file
data = open("AOC2020/Day3/day3.txt", "r").read().split("\n")

# Reading
# https://betterprogramming.pub/making-grids-in-python-7cf62c95f413

# Number of Columns (x)
columns = len(data)
print(columns)

# Number of Rows (y)
rows = (len(data[0]))
#print(rows)

#x_move = 3
#y_move = 1

def total_trees(x_move, y_move):

    tree = "#"
    trees = 0
    x = 0
    y = 0

    for row in range(columns-1):
        x += x_move
        if rows <= x:
            x = x-rows
        y += y_move

        #print(x)
        #print(y)
        #print(data[y][x])
        

        if data[y][x] == tree:
            trees += 1
    return trees

    
trees_part1 = total_trees(3,1)  
print("Part 1: " + str(trees_part1))

trees_part2 = total_trees(3,1) * total_trees(1,1) * total_trees(5,1) * total_trees(7,1) 
#trees_more = total_trees(1,2) 
print("Part 2: " + str(trees_part2))
#print(trees_more)