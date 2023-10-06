N=int(input("enter no of elements:"))
l=[]
s=0
for i in range(N):
   a=str(input("enter a string:"))
   l.append(a)
print(f"the list of strings is {l}")
b=str(input("enter a string to be searched:"))
for j in l:
    if b==j:
        s=s+1
print(f"the string {b} is repeated {s} times")

