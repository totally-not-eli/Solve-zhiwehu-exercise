# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (bot included). The numbers obtained should be printed in a comma-separated sequence on a single line.

start = 2000
end = 3200
x = []
for i in range(int(start),int(end+1)):
    if i % 7 == 0 and i % 5 != 0:
        x.append(str(i))
print(",".join(x))