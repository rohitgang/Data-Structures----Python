class Node:
    def __init__(self, data):
        self.__data= data
        self.__next= None
    def setNext(self, next):
        self.__next= next

    def getNext(self):
        return self.__next

    def getData(self):
        return self.__data

class LinkedList:
    from SingleLinkedList.LinkedList import Node
    def __init__(self):
        self.__head= None
    # Insert at the beginning of the list
    def peek(self):
        return self.__head
    def insert(self, data):
        putMeIn= Node(data)
        if self.__head is not None:
            putMeIn.setNext(self.__head)
            self.__head = putMeIn
        else:
            self.__head = putMeIn

    #Insert after the specified element
    def insertAfter(self, data, prev):
        if prev.getData is not None: #checks to see if the node exists in the list
           print('Specified node not in List, node should be in list to use this functionality')
           return

        if self.__head is not None:
            putMeIn= Node(data)
            myNext= prev.getNext()
            prev.setNext(putMeIn)
            putMeIn.setNext(myNext)
        else:
            print('No elements in list, setting specified node as head')
            self.__head= prev

    #Insert at the end
    def append(self, data):
        putMeIn= Node(data)
        if self.__head is not None:
            last= self.__head
            while last.getNext():
                last= last.getNext()
            last.setNext(putMeIn)
        else:
            self.__head= putMeIn

    def delete(self, data):
        temp=self.__head
        if temp is None:
            print('No elements in list, cannot perform delete operation')
            return
        if data== self.__head.getData(): # node to be deleted is head
            nextOne= self.__head.getNext()
            self.__head= nextOne
            temp = None
        else: #node is either the tail or in between
            temp= self.__head.getNext()
            prev= self.__head
            while temp is not None:
                # print(temp.getData())
                if temp.getData() == data:
                    break
                temp= temp.getNext()
                prev= prev.getNext()
            if temp is not None: # we found the element in the list
                if temp.getNext(): # not a tail
                    prev.setNext(temp.getNext())
                    found= None
                else: # tail
                    prev.setNext(None)
            else: # oops there was no element matching the data in the list
                print('Specified element not in the list.')

    def toString(self):
        res=''
        temp= self.__head
        while temp is not None:
            res+= '| '+str(temp.getData())+' | -> '
            temp= temp.getNext()
        res+= '| NULL |'
        return res