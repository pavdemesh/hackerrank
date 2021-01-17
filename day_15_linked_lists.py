class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            # print(f"current is now: {current}")
            current = current.next
            # print(f"current is now: {current}")

    def insert(self, head, data):
        if head is None:
            return Node(data)
        else:
            current = head
            while True:
                if current.next is None:
                    current.next = Node(data)
                    return head
                current = current.next


mylist = Solution()
head = mylist.insert(None, 15)
head = mylist.insert(head, 20)
mylist.display(head)

# mylist = Solution()
# T = int(input())
# head = None
# for i in range(T):
#     data = int(input())
#     head = mylist.insert(head, data)
# mylist.display(head)

# x = Node(15)
# y = Node(25)
# x.next = y
# print(x.next)
