#taking a list as input
n=int(input("Enter number of elements : "))
l=list()
for i in range(n):
    l.append(int(input("enter a number:")))
#sorting the list
l2=[]
for j in range(n):
    s=min(l)
    l2.append(s)
    l.remove(s)

print(f"the sorted list is {l2}")