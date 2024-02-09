l=[14,8,15,12,10]
pointer=0
swapcounter=0
for i in range(len(l)):
    pointer=pointer+1
    for j in range(pointer,len(l)):
        if l[i]>l[j]:
            l[i],l[j]=l[j],l[i]
            swapcounter=swapcounter+1
            print(l)
print(l,swapcounter)