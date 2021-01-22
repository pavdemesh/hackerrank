"""
Input: string s.
To solve this challenge, we must first take each character in s:
Enqueue it in a queue, and also push that same character onto a stack.
Once that's done, we must dequeue the first character from the queue
and pop the top character off the stack,
then compare the two characters to see if they are the same;
as long as the characters match, we continue dequeueing, popping, and comparing each character
until our containers are empty (a non-match means  isn't a palindrome).

Write the following declarations and implementations:

Two instance variables: one for your stack, and one for your queue.
A void pushCharacter(char ch) method that pushes a character onto a stack.
A void enqueueCharacter(char ch) method that enqueues a character in the queue instance variable.
A char popCharacter() method that pops and returns the character at the top of the stack instance variable.
A char dequeueCharacter() method that dequeues and returns the first character in the queue instance variable.
"""

import sys


class Solution:
    def __init__(self):
        self.queue = list()
        self.stack = list()

    def pushCharacter(self, data):
        self.stack.append(data)

    def enqueueCharacter(self, data):
        self.queue.append(data)

    def popCharacter(self):
        char = self.stack.pop()
        return char

    def dequeueCharacter(self):
        char = self.queue.pop(0)
        return char


# read the string s
s = input()
# Create the Solution class object
obj = Solution()

l = len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

isPalindrome = True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
'''
for i in range(l // 2):
    if obj.popCharacter() != obj.dequeueCharacter():
        isPalindrome = False
        break
# finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, " + s + ", is a palindrome.")
else:
    print("The word, " + s + ", is not a palindrome.")