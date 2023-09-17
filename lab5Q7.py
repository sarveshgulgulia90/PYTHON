#taking inputs from user
Input = int(input("Please enter the amount of rows: "))
#initialising
row = 0
#ooping
while(row < Input):
    row += 1
    spaces = Input - row
#initialising
    spaces_counter = 0
    #looping
    while(spaces_counter < spaces):
        print(" ", end='')
        spaces_counter += 1
#looping
    num_stars = 2*row-1
    while(num_stars > 0):
        print("*", end='')
        num_stars -= 1

    print()

    
    