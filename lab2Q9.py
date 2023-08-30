
P=int(input("Enter the principal amount:"))
r=7.1
t=int(input("enter the time:"))
n=int(input("enter the no of times interest compounds in a year:"))
if  P<500 or t<6:
    print("ERROR")
else:
    A =(P*(( 1 + r/n)**(n * t)))
    print(A)




