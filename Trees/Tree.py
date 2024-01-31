class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, value):
        newNode = Node(value)
        if self.root is None:
            self.root = newNode
        else:
            currentNode = self.root
            while True:
                if value < currentNode.value:
                    if currentNode.left is None:
                        currentNode.left = newNode
                        return
                    currentNode = currentNode.left
                else:
                    if currentNode.right is None:
                        currentNode.right = newNode
                        return
                    currentNode = currentNode.right

    def lookup(self, value):
        if self.root is None:
            return False
        currentNode = self.root
        while currentNode:
            if value<currentNode.value:
                currentNode = currentNode.left
            elif value > currentNode.value:
                currentNode = currentNode.right
            elif value == currentNode.value:
                return currentNode
        return False


    def traverse(self, node: Node):
        print("left:", node.left, " | value:", node.value, " | right:", node.right)
        tree = Node(node.value)
        tree.left = None if node.left is None else self.traverse(node.left)
        tree.right = None if node.right is None else self.traverse(node.right)
        return tree


bst = BinarySearchTree()
bst.insert(9)
bst.insert(4)
bst.insert(6)
bst.insert(20)
bst.insert(170)
bst.insert(15)
bst.insert(1)
item = bst.lookup(4)
print(print("left:", item.left.value, " | value:", item.value, " | right:", item.right.value))

print(bst.traverse(bst.root))
