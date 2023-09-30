#this program checks whether a string is pangram or not
#taking input from user
sty=str(input("Enter a string:"))
#initializing alphabet wtih all the alphabets
alphabet="abcdefghijklmnopqrstuvwxyz"
#loop to check if all the alphabets are present in the string
for char in alphabet:
    if char not in sty.lower():
        print("Not Pangram")
        break
else:
    print("Pangram")
