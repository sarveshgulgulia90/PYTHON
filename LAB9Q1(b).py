n = int(input("enter (length of list of integers):")) 
l=list() 
l2=list() 
  
  
for i in range(n): 
    l.append(int(input("enter a integer: "))) 
  
for j in l: 
    if j not in l2: 
        l2.append(j) 
a=set(l2) 
b=list(a)
print(f'original list: {l}')
print("list: ",b )
print(f'set: {a}')
