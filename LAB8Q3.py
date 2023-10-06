#taking a list as input
n=int(input("Enter number of elements : "))
l=list()
for i in range(n):
    l.append(int(input("enter a number:")))
for j in range(n):
    for k in range(j+1,n):
        if l[j]>=l[k]:
            l[j],l[k]=l[k],l[j]
print(f"the sorted list is {l}")