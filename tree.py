class Node:
    """
    Class Node
    """
    def __init__(self, value):
        self.left = None
        self.data = value
        # self.code = ''
        self.right = None



class Tree:
    """
    Class tree will provide a tree as well as utility functions.
    """

    def createNode(self, data):
        """
        Utility function to create a node.
        """
        return Node(data)

    def insert(self, node , data):
        """
        Insert function will insert a node into tree.
        Duplicate keys are not allowed.
        """
        #if tree is empty , return a root node
        if node is None:
            return self.createNode(data)
        # if data is smaller than parent , insert it into left side
        if data < node.data:
            node.left = self.insert(node.left, data)
        elif data > node.data:
            node.right = self.insert(node.right, data)

        return node


    def search(self, node, data):
        """
        Search function will search a node into tree.
        """
        # if root is None or root is the search data.
        if node is None or node.data == data:
            return node

        if node.data < data:
            self.codigo += '1'
            self.search(node.right, data)
            return node.data
        else:
            self.codigo += '0'
            self.search(node.left, data)
            return node.data



    def deleteNode(self,node,data):
        """
        Delete function will delete a node into tree.
        Not complete , may need some more scenarion that we can handle
        Now it is handling only leaf.
        """

        # Check if tree is empty.
        if node is None:
            return None

        # searching key into BST.
        if data < node.data:
            node.left = self.deleteNode(node.left, data)
        elif data > node.data:
            node.right = self.deleteNode(node.right, data)
        else: # reach to the node that need to delete from BST.
            if node.left is None and node.right is None:
                del node
            if node.left == None:
                temp = node.right
                del node
                return  temp
            elif node.right == None:
                temp = node.left
                del node
                return temp

        return node






    def traverseInorder(self, root):
        """
        traverse function will print all the node in the tree.
        """
        if root is not None:
            self.traverseInorder(root.left)
            print(root.data)
            self.traverseInorder(root.right)

    def traversePreorder(self, root):
        """
        traverse function will print all the node in the tree.
        """
        if root is not None:
            print(root.data)
            self.traversePreorder(root.left)
            self.traversePreorder(root.right)

    def traversePostorder(self, root):
        """
        traverse function will print all the node in the tree.
        """
        if root is not None:
            self.traversePreorder(root.left)
            self.traversePreorder(root.right)
            print(root.data)


def main():
    root = None
    tree = Tree()
    root = tree.insert(root, 0)
    print(root)
    tree.insert(root, 6)
    tree.insert(root, 5)
    tree.insert(root, 4)
    tree.insert(root, 3)
    tree.insert(root, 2)
    tree.insert(root, 1)

    codigo = ''
    print(tree.search(root, 6))
    print(tree.search(root, 5))
    print(tree.search(root, 4))
    print(tree.search(root, 3))
    print(tree.search(root, 2))
    print(tree.search(root, 1))

    print(tree.codigo)
    # print("Traverse Inorder")
    # tree.traverseInorder(root)

    # print("Traverse Preorder")
    # tree.traversePreorder(root)

    # print("Traverse Postorder")
    # tree.traversePostorder(root)


if __name__ == "__main__":
    main()

