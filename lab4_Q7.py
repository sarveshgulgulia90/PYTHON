#taking input
N= int(input("enter value till which u want to print the series:"))
#intialization variable
a = 1
b = 1
#sum
sum = a + b
#count variable
count = 1
print("Fibonacci series is: ")
#looping to save fibonacci series
while (count <= N):
	count += 1
	print(a)
	a = b
	b = sum
	sum = a + b
