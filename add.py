import sys

# Check the number of arguments passed
argc = len(sys.argv)

# Check if the correct number of arguments is provided
if argc != 3:
    print("""You exceed the number limit. You can use only two numbers to add.
    Use only two numbers.""")
    sys.exit(1)

# Add the numbers
result = float(sys.argv[1]) + float(sys.argv[2])

# Print the result
print("The sum of given numbers is:", result)
# Exit with success status
sys.exit(0)
