#taking input from user
string=input("Enter a string: ")
#replacing space with hyphen
a=string.replace(" ","-")
print(f'Original string is: {string}')
print(f'Hyphen-separated string is: {a}')

#snakecase
b=a.replace("-","_")
print(f'Original string is: {string}')
print(f'Snakecase string is: {b}')

#camelcase
print(f'Original string is: {string}')
temp=string.split(" ")
for ele in temp[1:]:
    res=temp[0]+"".join(ele.title())
print(f'Camelcase string is: {res}')