#taking input
year=int(input("Enter the year:"))
#checking whether year is leap or not
if (year%100==0 and year%400==0):
    print("Leap year")
elif(year%4==0 and year%100!=0):
    print("It is leap year")
else:
    print("NOT")
