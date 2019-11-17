class Stack:
    """ Stack is last in first out. 
        top -> |a|b|c|
        enqueue(d) -> |d|a|b|c|
        dequeue() -> |d|
    """
    def __init__(self, len):
        self.s= list()
        self.MAXLEN= len

    def push(self, el):
        self.s.insert(0,el)
        self.MAXLEN+=1

    def pop(self):
        ret= self.s[0]
        self.s= self.s[1:]
        self.MAXLEN-=1
        return ret

    def peek(self):
        return self.s[0]
    
    def isEmpty(self):
        return len(self.s) == 0

    def isFull(self):
        return len(self.s) == self.MAXLEN

    def display(self):
        return self.s    

    def size(self):
        return len(self.s)