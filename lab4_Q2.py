#taking inputs
X=int(input("enter a number:"))
Y=int(input("enter a number:"))
N=int(input("enter a number:"))
#check if X is less than Y
if X>=Y:
    print("Invalid Input , X should be less than Y")
#initialize a variable for current number
i=X+1
#using a while loop to display numbers betn X and Y that are divisible  by N
print("Numbers between", X, 'and' , Y ,"divisible by ", N )
while i<Y:
    if i%N==0:
        print(i)
    i=i+1
    