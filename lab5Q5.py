#taking inputs from user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if num1<0 or num2<0:
    print("Please enter positive numbers")
if num1==0 or num2==0:
    print("Please enter numbers greater than zero")
#checking the greater number  
if(num1 > num2):
    lcm = num1 
else:
    lcm=num2
#looping till the lcm is found
while(True):
    if((lcm % num1 == 0) and (lcm % num2 == 0)):
        print(f'The LCM of {num1} and {num2} is {lcm}')
        break
    lcm += 1