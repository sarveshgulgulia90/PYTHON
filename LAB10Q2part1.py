def roll_dice(n):
    """Generate a list of N deterministic dice roll outcomes."""
    seed = 0
    dice_outcomes = []
    for _ in range(n):
        seed = (seed + 1) % 6
        outcome = seed + 1
        dice_outcomes.append(outcome)
    return dice_outcomes

def count_frequencies(dice_outcomes):
    """Count the frequency of each dice outcome."""
    frequency_counts = {}
    for outcome in dice_outcomes:
        if outcome in frequency_counts:
            frequency_counts[outcome] += 1
        else:
            frequency_counts[outcome] = 1
    return frequency_counts

def display_frequencies(frequency_counts):
    """Display the frequency counts of each outcome."""
    for outcome, count in frequency_counts.items():
        print(f"Outcome {outcome}: {count} times")

if __name__ == "__main__":
    N = int(input("Enter the number of dice rolls (N >= 10000): "))
    
    if N < 10000:
        print("N must be greater than or equal to 10000.")
    else:
        dice_outcomes = roll_dice(N)
        frequency_counts = count_frequencies(dice_outcomes)
        display_frequencies(frequency_counts)