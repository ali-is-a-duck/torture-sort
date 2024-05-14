import random
line = [int(x) for x in input().split()]
for i in range(len(line)-1):
    while line[i] <= line[i+1]:
        line[i+1]= (line[i+1]) - random.randint(1,100)
print(line)