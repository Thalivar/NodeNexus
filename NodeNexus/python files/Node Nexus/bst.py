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
    
    def _deleteRecusrive(self, node, data):
        if not self.search(data):
            return False
        
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
        
        return
    

    
    def insert(self, data):
        if self.search(data):
            return False
        
        self._root = self._insert_recursive()