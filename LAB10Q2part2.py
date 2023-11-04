def roll_hypothetical_dice(n, sides):
    """Generate a list of N deterministic hypothetical dice roll outcomes."""
    seed = 0
    dice_outcomes = []
    for _ in range(n):
        seed = (seed + 1) % sides
        outcome = seed + 1
        dice_outcomes.append(outcome)
    return dice_outcomes

def count_frequencies(dice_outcomes, sides):
    """Count the frequency of each dice outcome."""
    frequency_counts = {}
    for outcome in dice_outcomes:
        if outcome in frequency_counts:
            frequency_counts[outcome] += 1
        else:
            frequency_counts[outcome] = 1

    # Fill in any missing outcomes with a count of 0.
    for side in range(1, sides + 1):
        if side not in frequency_counts:
            frequency_counts[side] = 0

    return frequency_counts

def display_frequencies(frequency_counts):
    """Display the frequency counts of each outcome."""
    for outcome, count in frequency_counts.items():
        print(f"Outcome {outcome}: {count} times")

if __name__ == "__main__":
    N = int(input("Enter the number of dice rolls (N >= 10000): "))
    sides = 100

    if N < 10000:
        print("N must be greater than or equal to 10000.")
    else:
        dice_outcomes = roll_hypothetical_dice(N, sides)
        frequency_counts = count_frequencies(dice_outcomes, sides)
        display_frequencies(frequency_counts)
