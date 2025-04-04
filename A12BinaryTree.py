
class btnode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class binarytree:
    def __init__(self):
        self.root = None

    def insert(self, node):
        new_node = btnode(node)
        if self.root == None:
            self.root = new_node
        else:
            self._recursiveinsert(self.root, new_node)

    def _recursiveinsert(self, curr_node, new_node):
        if new_node.value < curr_node.value:
            if curr_node.left is None:
                curr_node.left = new_node
            else:
                self._recursiveinsert(curr_node.left, new_node)
        if new_node.value >= curr_node.value:
            if curr_node.right is None:
                curr_node.right = new_node
            else:
                self._recursiveinsert(curr_node.right, new_node)
    
    def traversal(self, node):
        if node:
            self.traversal(node.left)
            print(node.value, end=' ')
            self.traversal(node.right)
    
    def search(self, num):
        return self._rec_search(self.root, num)

    def _rec_search(self, curr_node, num):
        if curr_node is None:
            return False
        if num == curr_node.value:
            return True
        elif num < curr_node.value:
            return self._rec_search(curr_node.left, num)
        else:
            return self._rec_search(curr_node.right, num)

    def delete(self, num):
        self.root = self._rec_delete(self.root, num)
    
    def _rec_delete(self, curr_node, num):
        if curr_node is None:
            return curr_node
        if num < curr_node.value:
            curr_node.left = self._rec_delete(curr_node.left, num)
        elif num > curr_node.value:
            curr_node.right = self._rec_delete(curr_node.right, num)
        else:
            if curr_node.left is None and curr_node.right is None:
                return None
            elif curr_node.left is None:
                return curr_node.right
            elif curr_node.right is None:
                return curr_node.left
            else:
                successor = self._find_min(curr_node.right)
                curr_node.value = successor.value
                curr_node.right = self._rec_delete(curr_node.right, successor.value)
        return curr_node

    def _find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

tree = binarytree()

tree.insert(45)
tree.insert(20)
tree.insert(65)
tree.insert(15)
tree.insert(25)
tree.insert(60)
tree.insert(75)
tree.insert(10)
tree.insert(17)

tree.traversal(tree.root)

print(f'\n\nIs 25 in the tree? {tree.search(25)}')
print(f'Is 30 in the tree? {tree.search(30)}')
print(f'Is 60 in the tree? {tree.search(60)}\n')

tree.delete(15)
tree.delete(20)
tree.delete(45)
tree.traversal(tree.root)