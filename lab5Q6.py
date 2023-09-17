#taking inputs fromm user
a = int(input(" Please Enter the First Value : "))
b = int(input(" Please Enter the Second Value : "))
#if nos are less than zero
if a<0 or b<0:
    print("Invalid")
#if they are zero
if a==0 or b==0:
    print("please enter num greater than zero")
    
#initialising
i = 1
#looping till the hcf/gcd is found
while(i <= a and i <= b):
    if(a % i == 0 and b % i == 0):
        val = i
    i = i + 1
#displaying the hcf/gcd   
print(f'The HCF/GCD of {a} and {b} is {val}')
