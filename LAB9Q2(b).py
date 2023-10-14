n1 = int(input("enter length of integers:")) 
n2 = int(input("enter length of integers:"))
l1=list() 
l2=list() 
  
  
for i in range(n1): 
    l1.append(int(input("enter a integer: ")))
for j in range(n2):
    l2.append(int(input("enter a integer: ")))

set_a=set(l1)
set_b=set(l2)

print(f'Union of set1 and set2: {set_a | set_b}')
print(f'Intersection of set1 and set2: {set_a & set_b}')
print(f'Difference of set1 and set2: {set_a - set_b}')
print(f'Symmetric difference of set1 and set2: {set_a ^ set_b}')