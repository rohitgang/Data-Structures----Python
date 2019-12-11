from BinarySearchTree import BST,Node

if __name__=='__main__':
    myItems= [5,1,8,2,0.5,6,7]
    bst= BST()
    for el in myItems:
        bst.insert(el)
    bst.preOrder(bst.root)
    print(' ')
    bst.postOrder(bst.root)
    print(' ')
    bst.inOrder(bst.root)
    head= bst.bstToDll(bst.root)