"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value=None, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
            # return self.value
        if self.next:
            self.next.prev = self.prev
            # return self.value


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0
    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        self.length += 1
        current = ListNode(value)
        if not self.head: 
            self.head = current
            self.tail = current
        if self.head:
            print('add_to_head self.head +++++++++++> : ', self.head.value, 'current: ', current.value)
            
            # self.head.prev = self.head
            # new_head = self.head.prev
            # self.head.next = new_head
            previous = ListNode(value, current, self.head)
            self.head.next = previous.next
            self.head = previous
            print('add_to_head self.head *******> : ', self.head.value, '|current: ', current.value, '|previous: ', previous.prev.value, 'next', previous.next.value) # 'previous: ', self.head.prev.value, 'next', self.head.next.value)
                # NEXT = self.head.insert_before(current)
                # self.head = NEXT
                
        # pass
    
    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        print('remove_from_head self.head : ---> : ', self.head.value)
        if not self.head: 
            return None
    
        else:
            if self.head:   
                head2 = self.head
                previous = self.head.prev
                if self.head == self.tail: 
                    self.head = None
                    self.tail = None
                self.head = None
                self.length -= 1
                return head2.value
                
            self.head = previous
            print('remove_from_head self.head : ---> : ')
        
        

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):

        current = ListNode(value)
        # print('self.head in add_to_tail: ', self.tail.value)
        if not self.head: 
            self.tail = current
            self.head = current
            self.length += 1
        else: 
            #set tails current value to be previous
            previous = self.tail

            #set next tail to point  current value
            self.tail.next = current
            #set previous to a variable 
            tail_previous = self.tail.prev
            #set self.tail.prev to be previous with these variables
            tail_previous = previous
            

            # self.tail to be the to be value since we pointed to it on 111
            self.tail = current
            self.length += 1
            self.tail.insert_before(tail_previous.value)
            print('previous add_to_tail: ', self.tail.prev.value)
            print('next add_to_tail: ',self.tail.value)
        # self.length += 1
        # if self.length == 0: 
        #     self.tail = DoublyLinkedList(value)
        #     return self.tail
        # else: 
        #     self.tail = value
        #     return self.tail
        pass
    def __str__(self): 
        return f"tail: {self.tail}"
    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        if not self.head: 
            return None
        value = self.tail.value
        end_of_tail = self.tail.next
        previous = self.tail.prev
        print('head value:', self.head.value, 'current:', value, 'previous: ', previous, 'EOtail: ', end_of_tail) 
        if self.head == self.tail: 
            print('head == tail')
            
            tail = self.tail
            tail2 = self.tail
            head2 = self.head
            self.tail = None
            
            self.head = None
            self.length -= 1
            return tail.value
        
        # if end_of_tail == None:

            
        # tail_val = DoublyLinkedList(self.tail)
        # return self.tail
        

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        # self.head = self.node.value
        pass
        

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        # self.tail = self.node.value
        current_tail = ListNode(self.tail.value, self.tail.next, node)
        # print('-------------------------move_to_end', self.tail.value, self.tail.next.value, node.value)
        self.tail.next = current_tail.next
        while self.tail.next != None: 
            previous_tail = current_tail.prev
        # self.tail.prev = current_tail
            self.tail = current_tail.next
            current_tail2 = ListNode(current_tail.next, previous_tail, None)
            self.tail = current_tail2.value
            self.tail.prev = current_tail2.prev
            self.tail.next = current_tail2.next
            print('*******************************************************self.tail.prev: ', self.tail.prev, 'self.tail: ', self.tail.value)
        

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        # self.node.delete()
        pass
        
    """Returns the highest value currently in the list"""
    def get_max(self):
        pass

# one = DoublyLinkedList(1)
# one.add_to_head(20)
# print(one.head)


###------------------------------------------In class solutions-------------------------------------------------

# """Each ListNode holds a reference to its previous node
# as well as its next node in the List."""
# class ListNode:
#     def __init__(self, value, prev=None, next=None):
#         self.value = value
#         self.prev = prev
#         self.next = next

#     """Wrap the given value in a ListNode and insert it
#     after this node. Note that this node could already
#     have a next node it is point to."""
#     def insert_after(self, value):
#         current_next = self.next
#         self.next = ListNode(value, self, current_next)
#         if current_next:
#             current_next.prev = self.next

#     """Wrap the given value in a ListNode and insert it
#     before this node. Note that this node could already
#     have a previous node it is point to."""
#     def insert_before(self, value):
#         current_prev = self.prev
#         self.prev = ListNode(value, current_prev, self)
#         if current_prev:
#             current_prev.next = self.prev

#     """Rearranges this ListNode's previous and next pointers
#     accordingly, effectively deleting this ListNode."""
#     def delete(self):
#         if self.prev:
#             self.prev.next = self.next
#         if self.next:
#             self.next.prev = self.prev


# """Our doubly-linked list class. It holds references to
# the list's head and tail nodes."""
# class DoublyLinkedList:
#     def __init__(self, node=None):
#         self.head = node
#         self.tail = node
#         self.length = 1 if node is not None else 0

#     def __len__(self):
#         return self.length

#     """Wraps the given value in a ListNode and inserts it 
#     as the new head of the list. Don't forget to handle 
#     the old head node's previous pointer accordingly."""
#     def add_to_head(self, value):
#         new_node = ListNode(value, None, None)
#         self.length += 1
#         if not self.head and not self.tail: 
#             self.head = new_node
#             self.tail = new_node
#         else: 
#             # the new node becomes the head of our list

#             # set the current head's prev to the new node
#             new_node.next = self.head
#             # set the new node's next to the current head
#             self.head.prev = new_node
#             # reassign self.head to point to the new node
#             self.head = new_node
#     """Removes the List's current head node, making the
#     current head's next node the new head of the List.
#     Returns the value of the removed Node."""
#     def remove_from_head(self):
#         value = self.head.value
#         self.delete(self.head)
#         return value

#     """Wraps the given value in a ListNode and inserts it 
#     as the new tail of the list. Don't forget to handle 
#     the old tail node's next pointer accordingly."""
#     def add_to_tail(self, value):
#         new_node = ListNode(value, None, None)
#         self.length += 1
#         if not self.head and not self.tail: 
#             self.head = new_node
#             self.tail = new_node
#         else: 
#             new_node.prev = self.tail
#             self.tail.next = new_node
#             self.tail = new_node

#     """Removes the List's current tail node, making the 
#     current tail's previous node the new tail of the List.
#     Returns the value of the removed Node."""
#     def remove_from_tail(self):
#         value = self.tail.value
#         self.delete(self.tail)
#         return value

#     """Removes the input node from its current spot in the 
#     List and inserts it as the new head node of the List."""
#     def move_to_front(self, node):
#         # check if the node is the head
#         if node is self.head:
#             return None
#         #store a regerence to the node we're going to move

#         value = node.value
#         if node is self.tail: 
#             self.remove_from_tail()

#         else: 
#             node.delete()
#             self.length -= 1
#         self.add_to_head(value)

#     """Removes the input node from its current spot in the 
#     List and inserts it as the new tail node of the List."""
#     def move_to_end(self, node):
#         if node is self.tail: 
#             return None
#         value = node.value
#         if node is self.head: 
#             self.remove_from_head()
#         else: 
#             node.delete()
#             self.length -= 1
#         self.add_to_tail(value)

#     """Removes a node from the list and handles cases where
#     the node was the head or the tail"""
#     def delete(self, node):
#         if not self.head and not self.tail: 
#             return None
#         self.length -= 1
#         if self.head is self.tail: 
#             self.head = None
#             self.tail = None
#         # check if nod is the head of the list.
#         elif self.head is node: 
#             self.head = node.next
#             node.delete()
#         elif self.tail is node: 
#             self.tail = node.prev
#             node.delete()

#         else: 
#             node.delete()

        
        
#     """Returns the highest value currently in the list"""
#     def get_max(self):
#         # initialize a variable that will keep track of largest element
#         current_max = self.head.value
#         current = self.head.next
#         while current is not None: 
#             if current.value > current_max: 
#                 current_max = current.value
#             current = current.next
#         return current_max


