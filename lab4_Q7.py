#taking input
n = int(input("enter value :"))
#intialization variable
a = 1
b = 1
#sum
sum = a + b
#count variable
count = 1
print("Fibonacci series is: ")
#looping to save fibonacci series
while (count <= n):
	count += 1
	print(a)
	a = b
	b = sum
	sum = a + b
