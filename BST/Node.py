class Node(object):

    def __init__(self, d):
        self.data= d
        self.left= None
        self.right= None

    def insert(self, d):
        if self.data == d:
            return False
        elif d < self.data :
            if self.left:
                return self.left.insert(d)
            else:
                self.left= Node(d)
                return True
        else:
            if self.right:
                return self.right.insert(d)
            else:
                self.right= Node(d)
                return True

    def find(self, d):
        if self.data == d:
            return True
        elif d < self.data:
            return self.left.find(d)
        elif d > self.data:
            return self.right.find(d)
        return False

    def preorder(self, l):
        l.append(self.data)
        if self.left:
            self.left.preorder(l)
        if self.right:
            self.right.preorder(l)
        return l
    
    def inorder(self,l):
        if self.left:
            self.left.preorder(l)
        l.append(self.data)
        if self.right:
            self.right.preorder(l)
        return l

    def postorder(self,l):
        if self.left:
            self.left.preorder(l)
        if self.right:
            self.right.preordeR(l)
        l.append(self.data)
        return l