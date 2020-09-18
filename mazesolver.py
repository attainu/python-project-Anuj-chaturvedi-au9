# to get input from .txt file

input_file = open('input.txt', 'r')
mat = []
N = input_file.readline()
N = int(N)
for i in range(N + 1):
    line = input_file.readline()

    # if i > 0:

    mat.append(list(map(int, line.rstrip().split())))
input_file.close()


# To find posible path between source and destination

def ValidMove(maze, x, y):

    if x >= 0 and x < N and y >= 0 and y < N and maze[x][y] == 1:
        return True

    return False


# Check whether given cell(row,col)
# is a valid cell or not

def FindPath(maze):

    # check source and destination cell
    # of the matrix have value 1

    sol = [[0 for j in range(N)] for i in range(N)]

    if not MazeSolver(maze, 0, 0, sol):
        return '-1'
    return sol


def MazeSolver(maze, x, y, sol ):

    if x == N - 1 and y == N - 1 and maze[x][y] == 1:
        sol[x][y] = 1
        return True

    if ValidMove(maze, x, y):
        sol[x][y] = 1

        if MazeSolver(maze, x + 1, y, sol):
            return True

        if MazeSolver(maze, x, y + 1, sol):
            return True

        sol[x][y] = 0
        return False


        # to display output in .txt file

temp = FindPath(mat)
output_file = open('output.txt', 'w')

if type(temp) is list:
    for i in temp:
        for j in i:
            output_file.write(str(j))
            output_file.write(' ')

        output_file.write('\n')
    output_file.close()
else:

    output_file.write(str(temp))
    output_file.close()
