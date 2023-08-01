# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (bot included). The numbers obtained should be printed in a comma-separated sequence on a single line.

start = 2000
end = 3200
x = [i for i in range(start,end) if (i % 7 == 0 and i % 5 != 0)] 
print(",".join(x))
