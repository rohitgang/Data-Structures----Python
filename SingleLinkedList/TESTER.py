from SingleLinkedList.LinkedList import LinkedList

if __name__ == '__main__':
    myListOfData= ['apples','oranges','watermelon','cucumber','banana','mango']
    myList= LinkedList()
    for el in myListOfData:
        print(el)
        myList.insert(el)
    # print(myList.peek().getData())
    print(myList.toString())
    myList.delete('watermelon')
    print(myList.toString())