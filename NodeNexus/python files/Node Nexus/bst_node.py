class BST_Node:

    def __init__(self, data=None):
        self._data = data
        self._right = None
        self._left = None

    # === Getters ===

    def getData(self):
        return self._data
    
    def getRight(self):
        return self._right
    
    def getLeft(self):
        return self._left
    
    # === Setters ===

    def setData(self, data):
        self._data = data

    def setRight(self, right_node):
        self._right = right_node

    def setLeft(self, left_node):
        self._left = left_node

    def __str__(self):
        return str(self._data) if self._data else "None"