file=open("people1.exercise.txt")
f=file.read().splitlines()
for i in f:
    if 'delhi' in i:
        f1=open("delhi.txt",'a')
        f1.write(i)
        f1.write('\n')
        f1.close()
    elif 'cochin' in i:
        f2=open('cochin.txt','a')
        f2.write(i)
        f2.write('\n')
        f2.close()
    elif 'meerut' in i:
        f3=open('meerut.txt','a')
        f3.write(i)
        f3.write('\n')
        f3.close()
    elif 'shimla' in i:
        f3= open('shimla.txt','a')
        f3.write(i)
        f3.write('\n')
        f3.close()
    elif "kanpur" in i:
        f4=open("kanpur.txt",'a')
        f4.write(i)
        f4.write("\n")
        f4.close()
    elif 'jaipur' in i:
        f5=open("jaipur.txt",'a')
        f5.write(i)
        f5.write('\n')
        f5.close()
    else:
        f6=open('tokyo.txt','a')
        f6.write(i)
        f6.write('\n')
        f6.close()
