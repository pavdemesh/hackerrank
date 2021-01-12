"""Given a base-10 integer, n, convert it to binary (base-2).
Then find and print the base-10 integer denoting the maximum number of
Consecutive 1's in n's binary representation"""

n = int(input())

# First step is to convert th base-10 int to a binary stored as string
binary_string = ""
# Take modulo 2 - this will be the last, the second-last etc digit
# So append it in front of existing digits
# Then do floor division of n by 2 and repeat
# If n gets equal to 0 - stop
while n > 0:
    digit = n % 2
    binary_string = str(digit) + binary_string
    n = n // 2

# next step is to calculate the longest consecutive sequence of 1's
seq_maximum = 0
seq_current = 0

for single_digit in binary_string:
    if single_digit == "1":
        seq_current += 1
    else:
        seq_maximum = max(seq_current, seq_maximum)
        seq_current = 0

# For the case that the binary representation contained only 1's
# We need to compare maximum with current sequence
seq_maximum = max(seq_current, seq_maximum)

print(seq_maximum)
