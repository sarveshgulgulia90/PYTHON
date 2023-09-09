#taking positive number
num=int(input("enter number:"))
#initialise counters
divisible_count=0
indivisible_count=0
#looping
n=int(input("enter number:"))
while num!=-999:
    if n%num==0:
        divisible_count=divisible_count+1
    else:
        indivisible_count=indivisible_count+1
        #get another number
    num=int(input("enter number:"))
#printing the counts 
print(divisible_count)
print(indivisible_count)


       


