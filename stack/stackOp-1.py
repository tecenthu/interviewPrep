# Brute Force
# # Stack Push inperation
# inp = []
# capacity = 2
# inp.append(1)
# print(inp)
# inp.append(2)
# print(inp)
# inp.append(3)
# print(inp)

# # Stack pinp inperation
# inp.pop()
# print(inp)

# # Return Tinp element of stack
# print(inp[-1])

# # validate Stack is Empty or not
# if len(inp) == 0:
#     print("Stack is empty")
# else:
#     print("Stack is not empty")

# if len(inp) == capacity:
#     print("Stack is Full")
# else:
#     print("Stack is not full")

"""
# Implementation Using List:
   - Python Built-in data Strucutre list can be used as a stack. Instead of push(), append() is used to add elements to the top of stack while pop() removes the element in LIFO order

   - List has a few shortcomings. The biggest issue is it's become slow when it's grow.
    It's required to do some memory allocations which leads append() calls taking much longer than other ones
"""

def createStack():
    inp = []
    return inp

def pushStack(inp, elem, cap):
    # before pushing the element to the stack,check the stack is full
    if isFull(inp, cap):
        return inp.append(elem)
    else:
        print(f"Stack Overflows cannot insert {elem}")

def popStack(inp):
    # before poping  the element to the stack,check the stack is empty or not
    if isEmpty(inp):
        inp.pop()
    else:
        print(f"Stack underflows")

def topStack(inp):
    if isEmpty(inp):
        return inp[-1]
    else:
        print(f"Stack is empty")

def isFull(inp,cap):
    if len(inp) == cap:
        return False
    return True

def isEmpty(inp):
    if len(inp) == 0:
        return False
    return True

inp = createStack()
print(type(inp))
pushStack(inp, 2, 4)
pushStack(inp, 12, 4)
pushStack(inp, 22, 4)
pushStack(inp, 32, 4)
pushStack(inp, 42, 4)
print(inp)
popStack(inp)
print(inp)
popStack(inp)
popStack(inp)
popStack(inp)
print(inp)
topStack(inp)
popStack(inp)