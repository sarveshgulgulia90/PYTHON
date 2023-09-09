#taking input
n=int(input("Enter a   number:"))
#storing value in another variable
temp=n
#initialization
re=0
#looping
while(n>0):
    dig=n%10
    re=(re*10)+dig
    n=n//10
#checking if they are equal
if(temp==re):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")