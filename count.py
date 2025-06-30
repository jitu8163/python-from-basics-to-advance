# Input string
input_string = "Hello, world!"

# Initialize an empty dictionary to store character counts
char_count = {}

# Count the characters in the string
for char in input_string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

# Print the character counts
print("Character counts:")
for char, count in char_count.items():
    print(f"'{char}': {count}")
