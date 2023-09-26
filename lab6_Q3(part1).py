# Input values from the user
x = float(input("Enter the value of x: "))
eps = float(input("Enter a positive error value (e): "))

# Initialize variables
F_x = 0.0
n = 0  # Term count

# Calculate the sum
while F_x < x + eps:
    F_x += 1 / (2**n)
    n += 1

# Display the result
print(f"The sum of the series F(x) is {F_x:.6f}")
print(f"The minimum number of terms to achieve F(x) < {x + eps} is {n}")