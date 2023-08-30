#calculate area of a plot
#taking input of length and width
length=int(input("Enter the length in feet:"))
width=int(input("Enter the width in feet:"))
#area
areainfeet=(length*width)
areainsqmeter=(areainfeet)*(0.3048*0.3048)
#output
print("Area of the plot in feet is:",areainfeet)
#area in square meter
print("Area in square meter is:", areainsqmeter)
