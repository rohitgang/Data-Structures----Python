from stack import Stack

class QueueFromStack():
    
    def __init__(self, len):
        self.s1= Stack(len)
        self.s2= Stack(len)
        self.MAXLEN= len

    def enqueue(self, el):
        # pop all the eleements from s1 to s2
        for i in range(self.s1.size()):
            self.s2.push(self.s1.pop())
        # push element to be added to s1
        self.s1.push(el)
        # pop elements from s2 to s1
        for i in range(self.s2.size()):
            self.s1.push(self.s2.pop())
        self.MAXLEN+=1

    def dequeue(self):
        ret= self.s1.pop()
        # self.s1= self.s1[1:]
        self.MAXLEN-=1
        return ret

    def isEmpty(self):
        return self.s1.isEmpty()
    
    def isFull(self):
        return self.s1.isFull()
    
    def display(self):
        return self.s1.display()
    def size(self):
        return self.s1.size()