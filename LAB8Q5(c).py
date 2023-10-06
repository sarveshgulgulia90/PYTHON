N=int(input("enter no of elements:"))
l=[]
s=0
for i in range(N):
   a=int(input("enter the numbers:"))
   l.append(a)
print(f'the list  is {l}')
new_list=[]
for i in l:
    if i>=10 and i<=20:
         new_list.append(i**2)
         
    else:
         new_list.append(i)
print(f'the new list is {new_list}')
       