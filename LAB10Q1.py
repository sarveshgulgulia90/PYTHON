# Get a paragraph from the user
user_paragraph = input("Enter a paragraph: ")

# Initialize a dictionary to store the frequency counts of vowels
vowel_frequency = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

# Convert the paragraph to lowercase to make the counting case-insensitive
user_paragraph = user_paragraph.lower()

# Iterate through the characters in the paragraph
for char in user_paragraph:
    if char in vowel_frequency:
        vowel_frequency[char] += 1

# Sort the dictionary by values in ascending order
sorted_vowel_frequency = {}
sorted_keys = sorted(vowel_frequency, key=vowel_frequency.get)
for key in sorted_keys:
    sorted_vowel_frequency[key] = vowel_frequency[key]

# Display the frequency counts in ascending order
for vowel in sorted_vowel_frequency:
    count = sorted_vowel_frequency[vowel]
    print(f'{vowel}: {count}') 