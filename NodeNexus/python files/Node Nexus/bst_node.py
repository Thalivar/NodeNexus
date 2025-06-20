class BST_Node:

    def __init__(self, data=None):
        self._data = data
        self._right = None
        self._left = None

    # === Getters ===

    def get_data(self):
        return self._data
    
    def get_right(self):
        return self._right
    
    def get_left(self):
        return self._left
    
    # === Setters ===

    def set_data(self, data):
        self._data = data

    def set_right(self, right_node):
        self._right = right_node

    def set_left(self, left_node):
        self._left = left_node

    def __str__(self):
        return str(self._data) if self._data else "None"