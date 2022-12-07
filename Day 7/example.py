class BinaryNode:
    def __init__(self, key):
        self.leftNode = None
        self.rightNode = None
        self.value = key
def postOrder(rootnode):
    if rootnode:
        postOrder(rootnode.leftNode)
        postOrder(rootnode.rightNode)
        print(rootnode.value)

rootnode = BinaryNode(6)
rootnode.leftNode = BinaryNode(1)
rootnode.rightNode = BinaryNode(4)
rootnode.leftNode.leftNode = BinaryNode(2)
rootnode.leftNode.rightNode = BinaryNode(3)
rootnode.leftNode.rightNode = BinaryNode(5)
print("\nPostorder traversal of binary tree is")
postOrder(rootnode)