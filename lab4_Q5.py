#taking input
n=int(input("Enter the value:"))
#initilization variables
i=1
fact=1
#condition if number is less than zero
if n<0:
    print("error")
#if no is 0 
if n==0:
    print("Factorial is 1")
#till initialization variable is less than given number
while i<=n:
    fact=fact*i
    i=i+1
#output
print(fact)
