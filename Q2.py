file=open('people1.exercise.txt')
f=file.read().splitlines()

count=0
for i in f:
    count+=1
print(count)