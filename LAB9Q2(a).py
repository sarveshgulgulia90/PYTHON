n1 = int(input("enter length of integers:")) 
n2 = int(input("enter length of integers:"))
l1=list() 
l2=list() 
  
  
for i in range(n1): 
    l1.append(int(input("enter a integer: ")))
for j in range(n2):
    l2.append(int(input("enter a integer: ")))

a=set(l1)
b=set(l2)
print(f'original list: {l1}')
print(f'original list: {l2}')
print(f'set1: {a}')
print(f'set2: {b}')
