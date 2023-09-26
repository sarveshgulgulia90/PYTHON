#taking input
N=int(input("enter the number:"))
#checking if word is negative or zero
if N<0:
    print(f'Enter a positive no')
if N==0:
    print("enter number greater than zero")
#initializing and looping looping and printing output
sum=0
for i in range(1,N+1):
    sum=sum+(1/i)
print(f'{sum:.9f}')

