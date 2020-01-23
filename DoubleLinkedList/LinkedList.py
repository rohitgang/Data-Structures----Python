class Node:
    def __init__(self, data):
        self.__data= data
        self.__next= None
        self.__prev= None

    def setNext(self, next):
        self.__next= next

    def getNext(self):
        return self.__next

    def setPrevious(self, prev):
        self.__prev= prev

    def getPrev(self):
        return self.__prev

    def getData(self):
        return self.__data

class LinkedList:
    def __init__(self):
        self.__head= None
        self.__tail= None

    def insert(self, data):
        putMeIn= Node(data)
        if self.__head is not None:
            putMeIn.setNext(self.__head)
            self.__head.setPrevious(putMeIn)
            self.__head= putMeIn
        else:
            self.__head= putMeIn
            self.__tail= putMeIn

    def insertAfter(self, data, prev):
        putMeIn= Node(data)
        if prev.getData() is None:
            print("Invalid: node doesn't exist.")
            return
        if self.__head is not None:
            if prev.getData() == self.__head.getData(): #insert node after head
                headsNext= self.__head.getNext()
                putMeIn.setPrevious(self.__head)
                putMeIn.setNext(headsNext)
                self.__head.setNext(putMeIn)
            elif prev.getData() == self.__tail.getData(): #insert after tail and make the new node the tail
                self.__tail.setNext(putMeIn)
                putMeIn.setPrevious(self.__tail)
                self.__tail= putMeIn
            else: # insert somewhere in between
                # |prev| -><-|prevsNext|
                prevsNext= prev.getNext()
                prev.setNext(putMeIn)
                putMeIn.setNext(prevsNext)
                prevsNext.setPrevious(putMeIn)
                putMeIn.setPrevious(prev)
                # |prev| -><-|putMeIn| -><- |prevsNext|
        else:
            print("The list is empty. Invalid operation")

    def append(self, data):
        putMeIn= Node(data)
        if self.__tail is not None:
            putMeIn.setPrevious(self.__tail)
            self.__tail.setNext(putMeIn)
            self.__tail= putMeIn
        else:
            self.__tail= putMeIn
            self.__head= putMeIn

    def remove(self, data):
        if self.__head is None:
            print("The list is empty. Invalid operation")
            return
        temp= self.__head
        if temp.getData() == data: #node to remove is head
            headsNext= temp.getNext()
            headsNext.setPrevious(None)
            self.__head= headsNext
        elif self.__tail.getData() == data: # node to remove is tail
            tailsPrev= self.__tail.getPrevious()
            tailsPrev.setNext(None)
            self.__tail= tailsPrev
        else: # node to remove in between

