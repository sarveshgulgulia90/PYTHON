#taking input
N=int(input("enter the number:"))
#checking if word is negative or zero
if N<0:
    print(f'Enter a positive no')
elif N==0:
    print(f'enter number greater than zero')
else:
    #intializing and looping looping and printing output
    sum=0
    fact=1
    for i in range(1,N+1):
        fact=fact*i
        sum=sum+(1/fact)
    print(f'{sum:.9f}')
   
 
   
 