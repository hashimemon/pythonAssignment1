l=["Aneeqa","Hamza","Aneeqa",1,1,0.4,0.4,2,3,4,5,6]
n=[]
d=[]
for i in l:
    if i in n:
        d.append(i)
    else:
        n.append(i)
print("Original List: ",l,"\n")
print("Found Duplicate Values in List: ",d)
