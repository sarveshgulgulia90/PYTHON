#task: Write a program to check whether a string is palindrome or not.
#taking input from user
st=str(input("Enter a string: "))
#empty string
w=""
#loop to reverse the string
for i in st[::-1]:
    w=w+i
#checking if the reversed string is equal to the original string
if st==w:
    print("Palindrome")
else:
    print("Not Palindrome") 