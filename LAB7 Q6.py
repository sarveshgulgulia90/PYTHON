#taking input
stion=str(input("Enter a string: "))    
print("Original String:",stion) 

#reversing order of words
j=stion.split()
l=len(j)
#loop to reverse the order of words
for i in range(-1,-l-1,-1):
    print(j[i],end=" ")
