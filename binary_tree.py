class BinTree(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    def add(self, data):
        """Add new leaf to tree"""
        if data < self.data:
            if self.left:
                self.left.add(data)
            else:
                self.left = BinTree(data)
        else:
            if self.right:
                self.right.add(data)
            else:
                self.right = BinTree(data)
        return
    def find(self, data):
        if data < self.data:
            if self.left:
                self.left.find(data)
            else:
                return False
        elif data > self.data:
            if self.right:
                self.right.find(data)
            else:
                return False
        else:
            return True
    def inorder(self):
        output = []
        if self.left:
            output += self.left.inorder()
        output.append(str(self.data))
        if self.right:
            output += self.right.inorder()
        return output
    def __str__(self):
        return '[' + ', '.join(self.inorder()) + ']'

# create a new Binary Tree
t = BinTree(0)
# add values to Binary Tree
t.add(1)
t.add(2)
t.add(3)
print(t)
# search for values in Binary Tree
print("Binary Tree contains the value 1? ", "Yes" if t.find(1) else "No")
print("Binary Tree contains the value 2? ", "Yes" if t.find(2) else "No")
print("Binary Tree contains the value 5? ", "Yes" if t.find(5) else "Three, sir.")
