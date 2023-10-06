sum=0
product=1
n = int(input("Enter number of elements : "))
l=list()
for i in range(n):
    l.append(int(input("enter a number:")))
maximum=l[0]
for a in (l):
    sum = sum + a
for b in l:
    product=product*b
for c in l:
    if maximum<c:
        maximum=c
print(f"the list of the integers {l}")
print(f"the sum of the elements of the list is {sum}")
print(f"the product of the elements of the list is product {product}")
print(f"greatest of the list is {maximum}")

    
