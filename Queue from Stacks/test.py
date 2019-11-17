from queueStack import QueueFromStack 

q= QueueFromStack(5)
q.enqueue('a')
print(q)
print(q.isEmpty())
print(q.isFull())

chars= ['b','c','d']
for el in chars:
    q.enqueue(el)
print(q.display())
print(q.dequeue())