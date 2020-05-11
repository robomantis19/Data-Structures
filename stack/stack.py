"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
import sys
sys.path.append("../doubly_linked_list")
from doubly_linked_list import ListNode

# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.array = []
#         #self.storage = ?

#     def __len__(self):
#         return self.size

#     def push(self, value):
#         self.array.append(value)
#         self.size += 1
#         return self.array

#     def pop(self):
#         if self.__len__() > 0: 
#             popped_item = self.array.pop()
#             self.size -= 1
#             return popped_item
#         else: 
#             return None

# stack = Stack1()
# stack.push(1)
# stack.push(23)
# stack.push(46)
# print(stack.__len__())
# print(stack.array)

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = ListNode(1)

    def __len__(self):
        return self.size
        

    def push(self, value):
        # self.storage = ListNode(value)
        self.storage.insert_after(value)
        self.size += 1
        return self.storage
    def pop(self):
        if self.size > 0: 
            popped = self.storage.delete()
            print(popped)
            self.size -= 1
            return popped
        else: 
            return None
            
        