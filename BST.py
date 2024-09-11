class Node:
    def __init__(self, key = 0, value = "Empty String", left = None, right = None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None
        self.size = 0


    def __add(self, node, value):
        if value < node.value:
            if node.left == None:
                node.left = Node(self.size, value, None, None)
            else:
                self.__add(node.left, value)
        else:
            if node.right == None:
                node.right = Node(self.size, value, None, None)
            else:
                self.__add(node.right, value)
        
        return True
                
    def add(self, value):
        self.size += 1
        
        if not self.root:
            self.root = Node(0, value, None, None)
            return True
        
        if value < self.root.value:
            if self.root.left == None:
                self.root.left = Node(self.size, value, None, None)
            else:
                self.__add(self.root.left, value)
        else:
            if self.root.right == None:
                self.root.right = Node(self.size, value, None, None)
            else:
                self.__add(self.root.right, value)
        
        return True

    def __search(self, node, value):
        if not node:
            return -1
        
        if node.value == value:
            return node.key
        
        if value < node.value:
            if node.left != None:
                return self.__search(node.left, value)
        else:
            if node.right != None:
                return self.__search(node.right, value)
        
        return -1
    
    def search(self, value):
        return self.__search(self.root, value)
    
    def __print_tree(self, node, lvl=0):
        if not node:
            return False
        
        print('  '*lvl + f'(key={node.key}, value={node.value})') if node else None
        self.__print_tree(node.left, lvl+1) if node.left else None
        self.__print_tree(node.right, lvl+1) if node.right else None
        
        return True
    
    def print_tree(self,):
        if not self.root:
            print("Tree is clear")
            return False

        print(f'(key={self.root.key}, value={self.root.value})')
        if self.root.left:
            self.__print_tree(self.root.left, 1)
        if self.root.right:
            self.__print_tree(self.root.right, 1)
        
        return True
