class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SLL:
    def __init__(self):
        self.head = None

    # print items in linkedlist
    def listprint(self):
        output = self.head
        while output is not None:
            print(output.data)
            output = output.next

    # Add item in linkedlist at end
    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        if self.head is None:
            self.head = NewNode

        tail = self.head
        while (tail.next):
            tail = tail.next

        tail.next = NewNode

    # Add item in linkedlist at start
    def AtStart(self, newdata):
        NewNode = Node(newdata)
        NewNode.next = self.head
        self.head = NewNode

    # Add item in linkedlist in between
    def InBetween(self, middle_node, newdata):
        if middle_node is None:
            print('Mentioned node does not exist')
            return

        NewNode = Node(newdata)
        NewNode.next = middle_node.next
        middle_node.next = NewNode

    # Delete item in linkedlist
    def DeleteNode(self, removedata):
        headval = self.head
        if headval is not None:
            if headval.data == removedata:
                self.head = headval.next
                headval = None
                return

        while (headval is not None):
            if headval.data == removedata:
                break

            prev = headval
            headval = headval.next

        if (headval == None):
            return
        prev.next = headval.next
        headval = None

    # Get total items in linkedlist
    def getCount(self):
        tmp = self.head
        count = 0

        while (tmp):
            count += 1
            tmp = tmp.next

        return count

    # Remove duplicates from unordered LL
    def remove_duplicates(self):
        ptr1 = ptr2 = dup = None
        ptr1 = self.head

        while (ptr1 != None and ptr1.next != None):
            ptr2 = ptr1
            # This loop is needed for unordered.
            while (ptr2.next != None):
                if (ptr1.data == ptr2.next.data):
                    dup = ptr2.next
                    ptr2.next = ptr2.next.next
                else:
                    ptr2 = ptr2.next
            ptr1 = ptr1.next

    # Remove duplicates from sorted LL
    def remove_sorted_duplicates(self):
        temp = self.head
        if temp is None:
            return
        while temp.next is not None:
            if temp.data == temp.next.data:
                new = temp.next.next
                temp.next = None
                temp.next = new
            else:
                temp = temp.next

        return self.head


list1 = SLL()
list1.head = Node('Mon')

e2 = Node('Tues')
e3 = Node('Wed')
list1.head.next = e2
e2.next = e3
list1.AtStart('Sun')
list1.AtStart('Mon')
list1.AtEnd('Thu')
list1.AtStart('Sat')

list1.InBetween(list1.head, 'Sun')
list1.DeleteNode('Mon')
list1.AtStart('Sun')
list1.AtStart('Mon')
list1.AtEnd('Tue')
list1.AtEnd('Wed')


count = list1.getCount()
print(count)
list1.remove_duplicates()
count = list1.getCount()
print(count)
list1.listprint()

list2 = SLL()
list2.head = Node(10)
list2.AtEnd(20)
list2.AtEnd(20)
list2.AtEnd(30)
list2.AtEnd(30)
list2.AtEnd(40)
count = list2.getCount()
print(count)
list2.listprint()


list2.remove_sorted_duplicates()
count = list2.getCount()
print(count)
list2.listprint()
