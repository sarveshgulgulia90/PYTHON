N=int(input("enter no of elements:"))
l=[]
s=0
for i in range(N):
   a=int(input("enter the numbers:"))
   l.append(a)
print(f'the list  is {l}')
new_list=[]
for i in l:
    if i>0:
         new_list.append(i**2)
         
    elif i<0:
         new_list.append(0)
print(f'the new list is {new_list}')