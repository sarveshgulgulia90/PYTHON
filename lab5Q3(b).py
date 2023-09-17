#taking no of rows as input
rows = int(input("Please Enter the Total Number of Rows  : "))
#intializing
i = 1
#looping through the numbers till the entered number with help of while loop
while(i <= rows):
    #output
    print(f'The pattern is as follows: \n')
    print(' ' * (rows - i) + '*' * i)
    i=i+1   
    