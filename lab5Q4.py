#taking positive number
num=int(input("\n enter number:"))
#initialise counters
divisible_count=0
indivisible_count=0
#looping till the user enters -999
n=int(input("\n enter number:"))
while num!=-999:
    if n%num==0:
        divisible_count=divisible_count+1
    else:
        indivisible_count=indivisible_count+1
        #get another number
    num=int(input("\n enter number :"))
#printing the counts 
print(f'"The divisible count is:",\t{divisible_count}\n')
print(f'"The indivisible count is:",\t{indivisible_count}\n')