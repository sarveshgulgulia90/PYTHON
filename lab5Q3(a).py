#taking the no of rows as input
num = int(input('Enter number of rows : '))
#intializing 
i = 1
##looping through the numbers till the entered number with help of nested while loop
while i <= num :
    j = 1
    while j <= i:
        print('*', end = " ")
        j += 1
    print()
    i += 1
