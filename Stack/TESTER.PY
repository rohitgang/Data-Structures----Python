from stack import Stack 

s= Stack(5)
s.push('a')
print(s.isEmpty())
print(s.isFull())

chars= ['b','c','d']
for el in chars:
    s.push(el)
print(s.display())
print(s.pop())
