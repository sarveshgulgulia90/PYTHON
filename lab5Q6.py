#taking inputs fromm user
a = int(input(" Please Enter the First Value : "))
b = int(input(" Please Enter the Second Value : "))
#initialising
i = 1
#looping till the hcf/gcd is found
while(i <= a and i <= b):
    if(a % i == 0 and b % i == 0):
        val = i
    i = i + 1
#displaying the hcf/gcd   
print(f'The HCF/GCD of {a} and {b} is {val}')