# Write a program which can compute the factorial of a given numbers. The results should be printed in a comma-separated sequence on a single line. Suppose the following input is supplied to the program: 8 Then, the output should be: 40320

def fac(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    return n * fac(n-1)

print(fac(int(input("Please enter an integer: "))))