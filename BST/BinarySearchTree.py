class Node:
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

class DLLNode:
    def __init__(self, data):
        self.data= data
        self.__next= None
        self.__prev= None
    def setNext(self,node):
        self.__next= node
    def setPrev(self, node):
        self.__prev= node
    def getNext(self):
        return self.__next

class BST:
    def __init__(self):
        self.root= None
        self.dll= []
        self.dllHead= None
    def insert(self, d):
        if self.root:
            return self.root.insert(d)
        else:
            self.root= Node(d)
            return True

    def find(self, d):
        if self.root:
            return self.root.find(d)
        else:
            return False

    def remove(self, d):
        #Case 1: Empty Tree
        if self.root == None:
            return False
        #Case 2: Deleting root node
        if self.root.data == d:
            #Case 2.1: Root node has no children
            if self.root.left is None and self.root.right is None:
                self.root= None
                return True
            #Case 2.2: Root node has left child
            elif self.root.left and self.root.right is None:
                self.root= set.root.left
                return True
            #Case 2.3: Root node has right child
            elif self.root.right and self.root.left is None:
                self.root= self.root.right
                return True
            #Case 2.4: Root node has two children
            else:
                moveNode= self.root.right
                moveNodeParent= None
                while moveNode.left:
                    moveNodeParent= moveNode
                    moveNode= moveNode.left
                self.root.data= moveNode.data
                if moveNode.data < moveNodeParent.data:
                    moveNodeParent.left= None
                else:
                    moveNodeParent.right= None
                return True
        #Find node to remove
        parent=None
        node= self.root
        while node and node.data != d:
            parent= node
            if d < node.data:
                node= node.left
            elif d> node.data:
                node= node.right
            #Case 3: Node not found
        if node == None or node.data!=d:
            return False
        #Case 4: node has no children
        elif node.left is None and node.right is None:
            if d < parent.data:
                parent.left= None
            else:
                parent.right= None
            return True
        #Case 5: Node has left child only
        elif node.left and node.right is None:
            if d < parent.data:
                parent.left= node.left
            else:
                parent.right= node.left
            return True
        #Case 6: Node has right child only
        elif node.right and node.left is None:
            if d < parent.data:
                parent.left= node.right
            else:
                parent.right= node.right
            return True
        #Case 7: node has right and left child
        else:
            moveNodeParent=node
            moveNode= node.right
            while moveNode.left:
                moveNodeParent= moveNode
                moveNode= moveNode.left
            node.data= moveNode.data
            if moveNode.right:
                if moveNode.data < moveNodeParent.data:
                    moveNodeParent.left= moveNode.right
                else:
                    moveNodeParent.right= moveNode.right
            else:
                if moveNode.data < moveNodeParent.data:
                    moveNodeParent.left= None
                else:
                    moveNodeParent.right= None
            return True

    def preOrder(self, node):
        if node is None:
            return
        print(node.data)
        if node.left is not None:
            self.preOrder(node.left)
        if node.right is not None:
            self.preOrder(node.right)

    def postOrder(self, node):
        if node is None:
            return
        # print(node.data)
        if node.left is not None:
            self.postOrder(node.left)
            # print(node.data)
        if node.right is not None:
            self.postOrder(node.right)
        print(node.data)

    def inOrder(self,node):
        if node is None:
            return
        if node.left is not None:
            self.inOrder(node.left)
        print(node.data)
        if node.right is not None:
            self.inOrder(node.right)

    def __setProperties(self):
        for i in range(len(self.dll)):
            curr= DLLNode(self.dll[i])
            if i == 0: #head
                print('Head',curr.data)
                next= DLLNode(self.dll[i+1])
                self.dllHead=curr
                curr.setNext(next)
            elif i == len(self.dll)-1 : #tail
                print('Tail',curr.data)
                prev= DLLNode(self.dll[i-1])
                curr.setPrev(prev)
            else:
                print('In Between',curr.data)
                prev= DLLNode(self.dll[i-1])
                next= DLLNode(self.dll[i+1])
                curr.setPrev(prev)
                curr.setNext(next)

    def __firstStep(self, node):
        if node is None:
            return
        if node.left is not None:
            self.__firstStep(node.left)
        self.dll.append(node.data)
        if node.right is not None:
            self.__firstStep(node.right)

    def __toList(self):
        print(self.dll)
        temp= self.dllHead
        res=''
        while temp is not None:
            res+='|'+str(temp.data)+'| -> '
            temp= temp.getNext()
        res+= '| null |'
        print(res)
    def bstToDll(self, node):
        self.__firstStep(node)
        self.__setProperties()
        self.__toList()
        return self.dllHead