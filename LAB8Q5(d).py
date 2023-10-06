N=int(input("enter no of elements:"))
l=[]
s=0
for i in range(N):
   a=str(input("enter the numbers:"))
   l.append(a)
print(f'the list  is {l}')

new_list=[i.title() if not i.title() else i for i in l]
print(f'the new list is {new_list}')