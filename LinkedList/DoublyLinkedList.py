from Node import DoubleLLNode as Node


class DoublyLinkedList:

    def __init__(self, value):
        newnode = Node(value)
        self.head = newnode
        self.tail = self.head
        self.length = 1

    def append(self, value):
        newnode = Node(value)
        newnode.prev = self.tail
        self.tail.next = newnode
        self.tail = newnode
        self.length += 1

    def prepend(self, value):
        newnode = Node(value)
        self.head.prev = newnode
        newnode.next = self.head
        self.head = newnode
        self.length += 1

    def show(self):
        items = []
        currentnode = self.head
        while currentnode != None:
            items.append((currentnode.prev, currentnode.value, currentnode.next))
            currentnode = currentnode.next
        print(items)

    def insert(self, index, value):
        if index == 0:
            self.prepend(value)
        elif index >= self.length:
            self.append(value)
        else:
            newnode = Node(value)
            leadernode = self.getnode(index - 1)
            pointernode = leadernode.next
            leadernode.next = newnode
            newnode.prev = pointernode.prev
            newnode.next = pointernode

    def remove(self, index):
        if index <= self.length - 1:
            leadernode = self.getnode(index - 1)
            removednode = leadernode.next
            nextnode = removednode.next
            leadernode.next = nextnode
            nextnode.prev = removednode.prev
            self.length -= 1

    def getnode(self, index):
        counter = 0
        currentnode = self.head
        while index != counter:
            currentnode = currentnode.next
            counter += 1
        return currentnode


dl = DoublyLinkedList(3)
dl.show()
dl.append(12)
dl.show()
dl.prepend(9)
dl.show()
dl.insert(1, 11)
dl.show()
dl.remove(1)
dl.show()
