class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class DLL:
    def __init__(self):
        self.head = None

    def append(self, newval):
        NewNode = Node(newval)
        NewNode.next = None
        if self.head is None:
            NewNode.prev = None
            self.head = NewNode
            return

        last = self.head
        while (last.next is not None):
            last = last.next
        last.next = NewNode
        NewNode.prev = last
        return

    # print items in linkedlist
    def listprint(self):
        output = self.head
        while output is not None:
            print(output.data)
            output = output.next

    # Add item in linkedlist at start
    def AtStart(self, newdata):
        NewNode = Node(newdata)
        NewNode.next = self.head
        if self.head is not None:
            self.head.prev = Node

        self.head = NewNode

    # Add in between
    def inBetween(self, newdata, location):
        NewNode = Node(newdata)
        ptr1 = self.head
        ptr2 = None
        while True:
            if ptr1.data == location:
                ptr2 = ptr1.next
                ptr1.next = NewNode
                NewNode.prev = ptr1
                NewNode.next = ptr2
                ptr2.prev = NewNode
                return
            else:
                ptr1 = ptr1.next

    def delEnd(self):
        ptr = self.head
        while ptr is not None:
            if ptr.next is None:
                ptr = ptr.prev
                ptr.next = None
                return
            else:
                ptr = ptr.next

    def delStart(self):
        ptr = self.head
        ptr = ptr.next
        ptr.prev = None
        self.head = self.head.next

    def delBetween(self, location):
        ptr1 = self.head
        ptr2 = None
        while True:
            if ptr1.next.data == location:
                ptr2 = ptr1.next.next
                ptr1.next = ptr2
                ptr2.prev = ptr1
                return
            else:
                ptr1 = ptr1.next


list1 = DLL()
list1.append(23)
list1.append(24)
list1.append(25)
list1.AtStart(26)
list1.inBetween(30, 26)
list1.delEnd()
list1.delStart()
list1.delBetween(23)
list1.listprint()
