#taking no of rows as input
no = int(input("Please enter the amount of rows: "))
##intialization variable
row = 0
#looping 
while(row < no):
    row += 1
    spaces = no - row
#intialization variable
    spaces_counter = 0
    #looping
    while(spaces_counter < spaces):
        print(" ", end='')
        spaces_counter += 1
#intialization variable
    num_stars = 2*row-1
    #looping
    while(num_stars > 0):
        print("*", end='')
        num_stars -= 1

    print()