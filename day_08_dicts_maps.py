"""Input Format
The first line contains an integer, n , denoting the number of entries in the phone book.
Each of the  subsequent lines describes an entry in the form of 2 space-separated values on a single line.
The first value is a friend's name, and the second value is an 8-digit phone number.
After the n lines of phone book entries, there are an unknown number of lines of queries.
Each line (query) contains a name to look up, and you must continue reading lines until there is no more input.
"""

import sys

# Read input and assemble Phone Book
num_of_entries = int(input())
# Create empty Phone Book type dict
phoneBook = {}
# Repeat input() n times, split input (based on space) into a list
# Use index[0] (name) as key and index[1] (8-digit number in str format) as value
for i in range(num_of_entries):
    contact_data = input().split(' ')
    phoneBook[contact_data[0]] = contact_data[1]

# Process Queries
# Will create a list (lines) with string each ending with '\n'
lines = sys.stdin.readlines()
# print(lines)
# print(type(lines))
for name in lines:
    # We have to get rid of '\n' characters, do this with strip
    name = name.strip()
    if name in phoneBook:
        print(name + '=' + str(phoneBook[name]))
    else:
        print('Not found')

"""
The same effect could be reached with input()
Input() will try to read a line from input source
if it encounters EOF - this is caught by the except block and exit from while loop

while True:
    try:
        search_query = input()
        if search_query in phonebook:
            print(f"{search_query}={phonebook[search_query]}")
        else:
            print("Not found")
    except:
        break"""
