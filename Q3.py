b = ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]
i=0
while i<len(b):
    f=open("bank_lists",'a')
    c=f.write(b[i])
    f.write('\n')
    f.close()
    i=i+1
    
