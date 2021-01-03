# String s of lowercase English letters that is repeated infinitely many times.
# Given an integer n, find and print the number of letter "a" in the first n letters of the infinite string.
# Example: s = 'abcac', n = 10
#  The substring we consider is "abcacabcac, the first 10 characters of the infinite string.
#  There are 4 occurrences of "a" in the substring.

def fn_repeated_string(s, n):
    # Set the initial repetitions counter to 0
    count_repetitions = 0
    for _i in range(n):
        if s[_i % len(s)] == 'a':
            count_repetitions += 1
    return count_repetitions


print(fn_repeated_string('abcac', 10))
# print(fn_repeated_string('a', 1_000_000_000_000))
# With running time O(n) the program will be very slow on large n like above
