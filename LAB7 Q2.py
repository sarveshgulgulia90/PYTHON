#taking input from user
sto=str(input("Enter a string: "))
#initializing count to 0
count=0
#loop to count the length of string
for i in sto:
    if i!=" ":
        count=count+1
#displaying results
print(f'Length of string is:{count}')      