import sys

if len(sys.argv) < 2:
    print("Provide at least one number")
    sys.exit(1)

length = sys.argv[1:]
total = 0

for i in length:
    total += float(i)

print("The sum is:", total)
