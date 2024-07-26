"""
Array implementations of Queue
    - For implementing queue, we need to keep track of indices, front and rear.
    - We enqueue an item at the rear and dequeue at the front
    - If we simply increment front and rear indices, then there may be problems, the front may reach the end of the array.
    - The solution to this problem is to increase front and rear in circular manner.

    Steps for enqueue:
        1) Chek the queue is full or not
        2) if full, print overflow and exit
        3) if queue is not full, increment tail and add the element
    
    Steps for dequeue:
        1) Check queue is empty or not
        2) if empty, print underflow and exit
        3) if not empty, print element at the head and increment head
"""
cap = 5
queueList = []
def enqueue(queueEx1, cap, elem):
    if queueIsFull(queueEx1, cap):
        queueEx1.append(elem)
        return queueEx1
    else:
        print("Queue is overflow and exit")
def queueIsFull(queueEx1, cap):
    if len(queueEx1) == cap:
        return False
    return True

def queueIsEmpty(queueEx1):
    if len(queueEx1) == 0:
        return False     
    return True
def dequeue(queueEx1):
    if queueIsEmpty(queueEx1):
        queueEx1.remove(queueEx1[0])
        return queueEx1
    else:
        print("Queue is underflow and exit")
print(enqueue(queueList, cap, 1))
print(enqueue(queueList, cap, 11))
print(enqueue(queueList, cap, 111))
print(queueList)
import pdb;pdb.set_trace()
print(dequeue(queueList))
print(dequeue(queueList))
print("============================")
print(queueList)
print(dequeue(queueList))
print(dequeue(queueList))