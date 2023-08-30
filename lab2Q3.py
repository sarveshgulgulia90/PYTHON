#taking input
x=int(input("enter the value of x:"))
y=int(input("enter the value of y:"))
#negative or not
if (x<0 or y<0):
    print("Invalid Input")

#divisble or not

elif (y%x==0):
    print("Divisble")
else:
    print("Not divisble")