class Node:
    def __init__(self,val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,val):
        new_node = Node(val)
        #if empty add value to head else add to tail
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while(current.next):
                current = current.next
            current.next = new_node

    def printNode(self):
        current = self.head
        while(current):
            print(current.val)
            current = current.next


linkedList = LinkedList()
linkedList.append(12)
linkedList.append(17)
linkedList.append(43)
linkedList.append(54)

linkedList.printNode()