from queue import Queue 

q= Queue(5)
q.enqueue('a')
print(q)
print(q.isempty())
print(q.isfull())

chars= ['b','c','d']
for el in chars:
    q.enqueue(el)
print(q.display())
print(q.dequeue())