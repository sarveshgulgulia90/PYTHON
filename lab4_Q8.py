#taking input
num = int(input("Enter a number:"))  
#initialization variables
f = 0
i = 2
#checking
if num<0:
    print("invalid input")
if num==1:
    print("1 is neither prime nor composite")
##looping
while i <= num / 2:
    if num % i == 0:
        f=1
    break
i=i+1
#checking
if f==0:
    print("The entered number is a PRIME number")
else:
    print("The entered number is not a PRIME number")