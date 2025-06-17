from bst_node import BST_Node
from currency import Dollar
from queue import Queue

class BST:

    def __init__(self):
        self._root = None
        self._count = 0

    def _getCurrencyValue(self, currency):
        return currency.whole_part * 100 + currency.fractional_part
    
    def _insertRecursive(self, node, data):
        if node is None:
            return BST_Node(data)
        
        data_value = self._getCurrencyValue(data)
        node_value = self._getCurrencyValue(node.get_data())

        if data_value < node_value:
            node.set_left(self._insertRecursive(node.get_left(), data))
        else:
            node.set_right(self._insertRecursive(node.get_right(), data))

        return node
    
    def _searchRecursive(self, node, data):
        if node is None:
            return False
        
        data_value = self._getCurrencyValue(data)
        node_value = self._getCurrencyValue(node.get_data())

        if data_value == node_value:
            return True
        elif data_value < node_value:
            return self._searchRecursive(node.get_left(), data)
        else:
            return self._searchRecursive(node.get_right(), data)
        
    def _findMin(self, node):
        while node.get_left() is not None:
            node = node.get_left()

        return node
    
    def _deleteRecursive(self, node, data):
        if node is None:
            return None
        
        data_value = self._getCurrencyValue(data)
        node_value = self._getCurrencyValue(node.get_data())

        if data_value < node_value:
            node.set_left(self._deleteRecusrive(node.get_left(), data))
        elif data_value > node_value:
            node.set_right(self._deleteRecusrive(node.get_right(), data))
        else:

            if node.get_left() is None:
                return node.get_right()
            elif node.get_right() is None:
                return node.get_left()
            
            successor = self._findMin(node.get_right())
            node.set_data(successor.get_data())
            node.set_right(self._deleteRecusrive(node.get_right(), successor.get_data()))
        
        return node
    
    def _inOrderRecursive(self, node, result):
        if node is not None:
            self._inOrderRecursive(node.get_left(), result)
            result.append(node.get_data())
            self._inOrderRecursive(node.get_right(), result)

    def _preOrderRecursive(self, node, result):
        if node is not None:
            result.append(node.get_data())
            self._preOrderRecursive(node.get_left(), result)
            self._preOrderRecursive(node.get_right(), result)

    def _postOrderRecursive(self, node, result):
        if node is not None:
            self._postOrderRecursive(node.get_left(), result)
            self._postOrderRecursive(node.get_right(), result)
            result.append(node.get_data())
    
    def insert(self, data):
        if self.search(data):
            return False
        
        self._root = self._insertRecursive(self._root, data)
        self._count += 1
        return True

    def search(self, data):
        return self._searchRecursive(self._root, data)
    
    def delete(self, data):
        if not self.search(data):
            return False
        
        self._root = self._deleteRecusrive(self._root, data)
        self._count -= 1
        return True
    
    def breadthFirstTraversal(self):
        if self._root is None:
            return []
        
        result = []
        queue = Queue()
        queue.enQueue(self._root)

        while not queue.isListEmpty():
            current = queue.deQueue()
            result.append(current.get_data())

            if current.get_left() is not None:
                queue.enQueue(current.get_left())
            if current.get_right() is not None:
                queue.enQueue(current.get_right())
        
        return result
    
    def inOrderTraversal(self):
        result = []
        self._inOrderRecursive(self._root, result)
        
        return result
    
    def preOrderTraversal(self):
        result = []
        self._preOrderRecursive(self._root, result)

        return result
    
    def postOrderTraversal(self):
        result = []
        self._postOrderRecursive(self._root, result)

        return result
    
    def printTree(self, output_file = None):
        traversals = {
            "Breadth-First": self.breadthFirstTraversal(),
            "In-Order": self.inOrderTraversal(),
            "Pre-Order": self.preOrderTraversal(),
            "Post-Order": self.postOrderTraversal()
        }

        for name, data in traversals.items():
            output = f"\n{name} Traversal: \n"

            if data:
                output += "\t".join(str(item) for item in data)
            else:
                output += "The tree is empty"

            print(output)

            if output_file:
                output_file.write(output + "\n")
    
    def count(self):
        return self._count
    
    def is_empty(self):
        return self._count == 0
    
    def empty(self):
        self._root = None
        self._count = 0