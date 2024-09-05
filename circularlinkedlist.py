class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class CLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def InsertStart(self, data):
        NewNode = Node(data)
        if self.head is None:
            self.head = NewNode
            self.tail = NewNode
        else:
            self.tail.next = NewNode
            NewNode.next = self.head
            self.head = NewNode

    def listPrint(self):
        ptr = self.head
        while True:
            if ptr.data == self.tail.data:
                print(ptr.data)
                return
            else:
                print(ptr.data)
                ptr = ptr.next

    def InsertEnd(self, data):
        NewNode = Node(data)
        if self.head is None:
            self.head = NewNode
            self.tail = NewNode
        else:
            self.tail.next = NewNode
            self.tail = NewNode
            self.tail.next = self.head
            # Case for Double circular LL
            # self.head.next = self.tail

    def InBetween(self, middle_node, newdata):
        if middle_node is None:
            print('Mentioned node does not exist')
            return

        NewNode = Node(newdata)
        NewNode.next = middle_node.next
        middle_node.next = NewNode

    def deleteNode(self, location):
        ptr = self.head
        ptr1 = None

        if ptr.data == location:
            ptr = ptr.next
            self.tail.next = ptr.next
            self.head = ptr
            return
        else:
            while ptr.next.data != location:
                ptr = ptr.next
                ptr1 = ptr.next.next
        if ptr.next.data == self.tail.data:
            self.tail = ptr
            self.tail.next = self.head


list1 = CLL()
list1.InsertStart(2)
list1.InsertStart(3)
list1.InsertEnd(4)
list1.InBetween(list1.head.next, 5)
list1.deleteNode(3)
list1.deleteNode(4)
list1.InsertStart(3)
list1.InsertStart(2)
list1.deleteNode(3)
list1.deleteNode(2)
list1.deleteNode(2)

list1.listPrint()
