#taking input
N=int(input("enter the number:"))
X=int(input("enter the number:"))
#checking if word is negative or zero
if N<0 or X<0:
    print(f'Enter a positive no')
else:
    #intializing and looping and printing output
    sum=1
    for i in range(1,N+1):
        sum=sum+((X**i)/i)
    print(f'{sum:.9f}')    