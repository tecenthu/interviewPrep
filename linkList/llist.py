class llist:
    def __init__(self, head):
        self.head = head
        self.next = None


# Traversing over 
def traverseLinkList(linkEx1):
    count = True
    while count:
        print(linkEx1.head)
        if linkEx1.next == None:
            count = False
        else:
            temp = linkEx1.next
            linkEx1 = temp
            
ll1 = llist(20)
ll1.next = llist(30)
ll1.next.next = llist(40)
ll1.next.next.next = llist(50)
#import pdb;pdb.set_trace()
# print(vars(ll1))
# print(vars(ll1.next))
#print(vars(ll1.next.next.next))
import pdb;pdb.set_trace()
traverseLinkList(ll1)
#while ll1.next != None:

def searchInLinkList(linkEx1, elem):
    status = True
    counter = 0
    while status:
        #temp = ll1.next
        if linkEx1.head == elem:
            print(f"Elem found at {counter}")
            status = False
        if linkEx1.next == None:
            print("Element Not Found")
            break
        linkEx1 = linkEx1.next
        counter+=1
searchInLinkList(ll1, elem=40)
