Odd = {}
Even = {}

while True:
    user_input = input("Enter a number (or 'over' to stop): ")

    if user_input.lower() == 'over':
        break

    try:
        number = int(user_input)

        if number % 2 == 0:  # Even number
            Even[number] = [number**2, number**3]
        else:  # Odd number
            Odd[number] = [number**2, number**3]
    except ValueError:
        print("Invalid input. Please enter a valid number or 'over' to stop.")

# Print the resulting dictionaries
print("Even =", Even)
print("Odd =", Odd)



