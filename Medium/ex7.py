# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j. Note: i=0,1.., X-1; j=0,1,¡­Y-1. Example Suppose the following inputs are given to the program: 3,5 Then, the output of the program should be: [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

prompt = "Please enter two integers, for row and column respectively: "
numbers = input(prompt)

def solve(numbers):
    dimension = [int(a) for a in numbers.split(",")]
    rowNum = dimension[0]
    colNum = dimension[1]
    array = [[0 for i in range(colNum)] for x in range(rowNum)]
    for i in range(rowNum):
        for j in range(colNum):
            array[i][j] = i*j
    return array
