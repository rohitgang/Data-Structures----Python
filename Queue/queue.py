class Queue:

    """ Queue is first` in first out. 
        top -> |a|b|c|
        enqueue(d) -> |a|b|c|d|
        dequeue() -> a
    """
    #constructor
    def __init__(self, len):
        self.q= list()
        self.MAXLEN= len    
    # adds the given element to the bottom of the list
    def enqueue(self, element):
        self.q.append(element)
        self.MAXLEN+=1

    # removes the top element
    def dequeue(self):
        ret= self.q[0]
        self.q= self.q[1:]
        self.MAXLEN-=1
        return ret
    
    def isfull(self):
        return len(self.q) == self.MAXLEN
    
    def peek(self):
        return self.q[0]

    def isempty(self):
        return len(self.q) == 0
    def display(self):
        return self.q