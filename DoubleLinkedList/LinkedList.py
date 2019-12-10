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

    def insertAfter(self, data, prev):
        putMeIn= Node(data)
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
                prevsNext= prev.getNext()
                prev


