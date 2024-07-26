out = [10, 50, 30, 70, 80, 20, 90, 40]

"""
Traversing over array Sequential and reverse
"""
# Sequential

def traverseSeq(arrList):
    for k in range(len(arrList)):
        print(arrList[k],end=" ")
# Reverse:
def traverseReverse(arrList):
    for val in range(len(out)-1,-1,-1):
        print(out[val], end=" ")

traverseSeq(out)
print("traverseSeq\n")

traverseReverse(out)
print("traverseReverse\n")

"""
Insertion of array in specific index
Let's take an array of 5 integers.

op = [1, 20, 5, 78, 30]

If we need to insert an element 100 at position 2, the execution will be,
"""


def insertElemIndex(arr, pos, elem):
    y =[]
    for j in range(len(op)):
        if pos == j:
            y = y + [elem]
            y = y + [arr[j]]
        else:
            y = y + [arr[j]]
    print(y)
op = [1, 20, 5, 78, 30]

pos = 4
elem = 202
print("Insert element from particular index")
insertElemIndex(op, pos, elem)

# Delete element from particular index

def delElementForIndex(arr, pos):
    val = []
    for k in range(len(arr)):
        if pos == k:
            #import pdb;pdb.set_trace()
            val = val + [-1]
        else:
            val = val + [delOp[k]]
    print(val)
delOp = [1, 20, 5, 78, 30]
pos = 2
print("Delete element from particular index")
delElementForIndex(delOp, pos)

# Searching: Finding the index of element an array

def srcElemRtInd(arr, findElem):
    for i in range(len(srchOp)):
        if srchOp[i] == findElem:
            print(i)
srchOp = [1, 20, 5, 78, 30]
findElem = 78
print(" Return the index of an Element")
srcElemRtInd(srchOp, findElem)