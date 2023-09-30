# progra to take a string and creates a new string without any duplicate characters
#taking input from user
sti=str(input("Enter a string:"))
#empty string
p=""
#loop to check for duplicate characters
for char in sti:
    if char not in p:
        p=p+char
#displaying results
print(f'Original string is: {sti}')
print(f'New string without duplicate characters is: {p}')

