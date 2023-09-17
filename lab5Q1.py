#taking a number as input
x = int(input("enter a number:"))
#checking if number is negative
if x<0:
    print("please enter a positive number")
#checking if number is zero
if x==0:
    print("please enter a number greater than zero")
print(f'Multiplication table \n ')
#looping through the numbers till the entered number 
i=1
while i<=x:
    y=1
    while y<=20:
        print(f'{i}*{y}={i*y}\n')
        y=y+1
    i=i+1
