#taking input
seconds = int(input("enter time in seconds: "))
##converting seconds to hours and minutes
seconds= seconds % (24 * 3600)
hour = seconds // 3600
seconds%= 3600
minutes = seconds // 60
seconds %= 60
#displaying the output
print( hour, "Hours", minutes,"Minutes",seconds,"Seconds")
print()