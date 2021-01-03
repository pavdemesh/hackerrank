# String s of lowercase English letters that is repeated infinitely many times.
# Given an integer n, find and print the number of letter "a" in the first n letters of the infinite string.
# Example: s = 'abcac', n = 10
#  The substring we consider is "abcacabcac, the first 10 characters of the infinite string.
#  There are 4 occurrences of "a" in the substring.

def fn_repeated_string(s, n):
    num_whole_strings = n // len(s)
    num_single_chars = n % len(s)

    substring = s * num_whole_strings + s[:num_single_chars]

    return substring


print(fn_repeated_string('abcac', 100))

# print(fn_repeated_string('abcac', 1000000000000))
# Will produce Memory Error on large n = 1000000000000
