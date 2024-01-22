class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head
        self.length = 1

    def append(self, value):
        newnode = Node(value)
        self.tail.next = newnode
        self.tail = newnode
        self.length += 1

    def prepend(self, value):
        newnode = Node(value)
        newnode.next = self.head
        self.head = newnode
        self.length += 1

    def show(self):
        items = []
        currentnode = self.head
        while currentnode != None:
            items.append(currentnode.value)
            currentnode = currentnode.next
        print(items)

    def getnode(self, index):
        counter = 0
        currentnode = self.head
        while counter != index:
            currentnode = currentnode.next
            counter +=1
        return currentnode


    def insert(self, index, value):
        if index == 0:
            self.prepend(value)
        elif index > self.length:
            self.append(value)
        else:
            newnode = Node(value)
            leader = self.getnode(index - 1)
            nextnode = leader.next
            leader.next = newnode
            newnode.next = nextnode

    def remove(self, index):
        if index <= self.length:
            leader = self.getnode(index - 1)
            removenode = leader.next
            leader.next = removenode.next
        else:
            print("Index out of range")


linkedList = LinkedList(2)
linkedList.show()
linkedList.append(3)
linkedList.show()
linkedList.prepend(1)
linkedList.prepend(4)
linkedList.prepend(5)
linkedList.show()
linkedList.insert(1, 4)
linkedList.show()
linkedList.remove(2)
linkedList.show()
linkedList.insert(99, 11)
linkedList.show()
linkedList.remove(32)
linkedList.show()