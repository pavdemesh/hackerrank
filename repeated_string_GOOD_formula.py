# String s of lowercase English letters that is repeated infinitely many times.
# Given an integer n, find and print the number of letter "a" in the first n letters of the infinite string.
# Example: s = 'abcac', n = 10
#  The substring we consider is "abcacabcac, the first 10 characters of the infinite string.
#  There are 4 occurrences of "a" in the substring.

def fn_repeated_string(s, n):
    # Set the total count of "a" to 0
    count_a_total = 0

    # Calculate the number of "a" in a single string
    count_a_single_string = 0
    for char in s:
        if char == "a":
            count_a_single_string += 1

    # Calculate the number of whole string in the given substring
    # e.g. if n = 12 and string s is "abcac" - the resulting substring will contain 2 whole strings s
    # Calculate via integer division of n over len(s)
    num_whole_strings = n // len(s)

    # Calculate the number of "a" in the whole strings within the substring
    count_a_total += count_a_single_string * num_whole_strings

    # Now we have to account for the "hanging" letters, i.e. incomplete string
    # And count "a" in them
    # Calculate the number of remaining chars of the string
    # If n = 12 and s = "abcac": the resulting substring will contain 2 whole strings s
    # And 2 first chars from s. Calculate via modulo
    num_remain_chars = n % len(s)
    for char in s[:num_remain_chars]:
        if char == "a":
            count_a_total += 1

    return count_a_total


print(fn_repeated_string('aba', 10))
print(fn_repeated_string('a', 1_000_000_000_000))
