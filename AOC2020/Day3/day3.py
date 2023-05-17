#Get data from text file
data = open("AOC2020/Day3/day3.txt", "r").read().split("\n")

# Reading
# https://betterprogramming.pub/making-grids-in-python-7cf62c95f413

# Number of Columns (x)
columns = len(data)
print(columns)

# Number of Rows (y)
rows = (len(data[0]))
print(rows)
tree = "#"
trees = 0
x = 0
y = 0
x_move = 3
y_move = 1

for row in range(columns-1):
    x += x_move
    if rows <= x:
        x = x-rows
    y += y_move

    #print(x)
    #print(y)
    print(data[y][x])
    

    if data[y][x] == tree:
        trees += 1


    
  
print("Part 1: " + str(trees))
