"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
from queue import Queue
from stack import Stack
# import collections 

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
   
        # print('value: ', self.value)
        
        if value < self.value:
            if self.left is None:  
                Node = BSTNode(value)
                self.left= Node             
            else:
                return self.left.insert(value)         
        else:    
            if not self.right: 
                Node = BSTNode(value)
                self.right = Node
            else:     
                return self.right.insert(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # when we start searching, self will be the root
        # compare the target against self
        if target == self.value:
            return True
        # if not self.value: 
        #     return False
        if target < self.value:
            # go left
            if not self.left: 
                return False
            return self.left.contains(target)
        else: 
            # go right
            if not self.right: 
                return False
            return self.right.contains(target)
        
    # Return the maximum value found in the tree
    def get_max(self):
        
        if not self.left and not self.right:
            return self.value
        else:
            if self.right:
                return self.right.get_max()
            else:
                return self.value

    def iterative_get_max(self): 
        current_max = self.value

        current = self
        # traverse our structure adn update current_max variable if we see a larger value
        while current is not None: 
            if current.value > current_max: 
                current_max = current.value
            current = current.right
        return current_max



    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        
        if not self.left and not self.right:
            print('function: ', fn(self.value))
        else:
            if self.right:
                fn(self.value)
                self.right.for_each(fn)
                if self.left:
                    fn(self.value)
                    self.left.for_each(fn)
                
            else:
                fn(self.value)
                self.left.for_each(fn)
                
    # def iterative_for_each(self, fn): 
    #     stack = []
    #     stack.append(self)

    #     while len(stack) > 0: 
    #         current = stack.pop()
    #         if current.right: 
    #             stack.append(current.right)
    #         if current.left: 
    #             stack.append(current.left)
    #         fn(current.value)    


            

    # def breadth_first_search(self, fn): 
    #     queue = deque()
    
    #     queue.append(self)
    #     while len(queue) > 0: 
    #         current = queue.popleft()
    #         if current.left: 
    #             queue.append(current.left)
    #         if current.right: 
    #             queue.append(current.right)

    #         fn(current.value)


    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
    #     #may neeed to research this method.
        if node is None: 
            return 
        self.in_order_print(node.left)
        print(node.value)
        self.in_order_print(node.right)


    #     if node.left != None: 
            
    #         self.in_order_print(node.left)
    #         print(node.value)

    #     # else: 
    #         # print(node.value) 
    #     if node.right != None:
    #         self.in_order_print(node.right)

   
    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        """
        Print each vertex in breadth-first order
        beginning from starting_node.
        """
        

        # print('hi')
        qq = Queue()
        qq.enqueue(node)

        while qq.len() > 0:
            
            current = qq.dequeue()
            if current.left:
                qq.enqueue(current.left)
            if current.right:
                qq.enqueue(current.right)
        return current.value

        # queue.append(node)
        # while len(queue) > 0: 
        #     current = queue.popleft()
        #     if current.left: 
        #         queue.append(current.left)
        #     if current.right: 
        #         queue.append(current.right)
        #     print(current.value)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        print('hi there')
        s = Stack()
        s.push(node)
        while s.__len__() > 0: 
            current = s.pop()
            print(current.value)
            if current.left: 
                s.push(current.left)
            if current.right: 
                s.push(current.right)
            


    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
