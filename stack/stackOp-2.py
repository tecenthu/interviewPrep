# Implementions using collections.deque
""" 
  - Python stack can be implemented using the deque class from the collections module.
  - Deque is preffered over the list in the case where we need quicker append and pop operations.
  - It provide O(1) time complexity for append and pop operation as comapred to list which provides O(n) time complexity
"""
from collections import deque

# stack = deque()
# print(stack, type(stack))
# print(dir(stack))

def createStack():
    stack = deque()
    return stack

def pushStack(stack, elem, cap):
    if isFull(stack, cap):
        return stack.append(elem)
    else:
        print(f"Stack Overflow")
    
def popStack(stack):
    if isEmpty(stack):
        return stack.pop()
    else:
        print(f"Stack Underflow")
    
def topStack(stack):
    #import pdb;pdb.set_trace()
    if isEmpty(stack):
        return stack[-1]

def isFull(stack, cap):
    if len(stack) == cap:
        return False
    return True

def isEmpty(stack):
    if len(stack) == 0:
        return False
    return True

cap = 4
st1 = createStack()
print(st1)  
pushStack(st1, 101, cap)
print(st1) 
pushStack(st1, 201, cap)
print(st1) 
pushStack(st1, 301, cap)
print(st1) 
pushStack(st1, 401, cap)
print(st1) 
pushStack(st1, 501, cap)
print(st1)
print(f"top element")
print(popStack(st1))
print(st1)
popStack(st1)
topStack(st1)
print(st1)
popStack(st1)
print(st1)
popStack(st1)
print(st1)
popStack(st1)
print(st1)

