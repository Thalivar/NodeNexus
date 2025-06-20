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
        node_value = self._getCurrencyValue(node.getData())

        if data_value < node_value:
            node.setLeft(self._insertRecursive(node.getLeft(), data))
        else:
            node.setRight(self._insertRecursive(node.getRight(), data))

        return node
    
    def _searchRecursive(self, node, data):
        if node is None:
            return False
        
        data_value = self._getCurrencyValue(data)
        node_value = self._getCurrencyValue(node.getData())

        if data_value == node_value:
            return True
        elif data_value < node_value:
            return self._searchRecursive(node.getLeft(), data)
        else:
            return self._searchRecursive(node.getRight(), data)
        
    def _findMin(self, node):
        while node.getLeft() is not None:
            node = node.getLeft()

        return node
    
    def _deleteRecursive(self, node, data):
        if node is None:
            return None
        
        data_value = self._getCurrencyValue(data)
        node_value = self._getCurrencyValue(node.getData())

        if data_value < node_value:
            node.setLeft(self._deleteRecursive(node.getLeft(), data))
        elif data_value > node_value:
            node.setRight(self._deleteRecursive(node.getRight(), data))
        else:

            if node.getLeft() is None:
                return node.getRight()
            elif node.getRight() is None:
                return node.getLeft()
            
            successor = self._findMin(node.getRight())
            node.setData(successor.getData())
            node.setRight(self._deleteRecursive(node.getRight(), successor.getData()))
        
        return node
    
    def _inOrderRecursive(self, node, result):
        if node is not None:
            self._inOrderRecursive(node.getLeft(), result)
            result.append(node.getData())
            self._inOrderRecursive(node.getRight(), result)

    def _preOrderRecursive(self, node, result):
        if node is not None:
            result.append(node.getData())
            self._preOrderRecursive(node.getLeft(), result)
            self._preOrderRecursive(node.getRight(), result)

    def _postOrderRecursive(self, node, result):
        if node is not None:
            self._postOrderRecursive(node.getLeft(), result)
            self._postOrderRecursive(node.getRight(), result)
            result.append(node.getData())

    # == ASCII Art Tree Visualization Methods ===

    def _getTreeHeight(self, node):
        if node is None:
            return 0
        
        return 1 + max(self._getTreeHeight(node.getLeft()),
                       self._getTreeHeight(node.getRight()))
    
    def _collectingNodesByLevel(self, node, level, targetLevel, nodes):
        if level == targetLevel:
            nodes.append(node)
            return
        
        if node is None:
            if level < targetLevel:
                self._collectingNodesByLevel(None, level + 1, targetLevel, nodes)
                self._collectingNodesByLevel(None, level + 1, targetLevel, nodes)

        else:
            if level < targetLevel:
                self._collectingNodesByLevel(node.getLeft(), level + 1, targetLevel, nodes)
                self._collectingNodesByLevel(node.getRight(), level + 1, targetLevel, nodes)

    def _formatCurrencyShort(self, currency):
        if currency is None:
            return "None"
        
        return f"{currency.whole_part}.{currency.fractional_part:02d}"
    
    def _buildCompactTreeLines(self, node, lines, depth, prefix):
        if node is None:
            return
        
        indent = "    " * depth
        currencySTR = self._formatCurrencyShort(node.getData())

        if depth == 0:
            lines.append(f"Root: {currencySTR}")
        else:
            lines.append(f"{indent}{prefix}{currencySTR}")

        # Adds the chil nodes if they exist
        if node.getLeft() is not None or node.getRight() is not None:
            if node.getLeft() is not None:
                self._buildCompactTreeLines(node.getLeft(), lines, depth + 1, "├─L: ")
            else:
                lines.append(f"{indent}    ├─L: (empty)")

            if node.getRight() is not None:
                self._buildCompactTreeLines(node.getRight(), lines, depth + 1, "└─R: ")
            else:
                lines.append(f"{indent}    └─R: (empty)")


    def _drawTree(self, node, lines, x, y):
        if node is None:
            return
        
        # Ensures that we will have enough lines
        while len(lines) <= y:
            lines.append(" " * 80)
        
        # Formats the node value
        nodeSTR = self._formatCurrencyShort(node.getData())

        # This ensures the line is long enough
        while len(lines[y]) < x + len(nodeSTR):
            lines[y] += " "

        # Places the node
        lines[y] = lines[y][:x] + nodeSTR + lines[y][x + len(nodeSTR):]

        # Calculates the positions of the children
        left_offset = 8
        right_offset = 8

        # Draw the left child
        if node.getLeft() is not None:
            left_x = x - left_offset
            left_y = y + 2

            # Draws the connection line
            if len(lines) <= y + 1:
                lines.append(" " * 80)

            # Draws the connection lines
            while len(lines[y + 1]) < x:
                lines[y + 1] += " "

            # Adds the branch ASCII characters
            lines[y + 1] = lines[ y + 1][:x - 2] + "┌─" + lines[y + 1][x:]

            # Will draw the left subtree recursively
            self._drawTree(node.getLeft(), lines, left_x, left_y)
        
        # Draws the right child
        if node.getRight() is not None:
            right_x = x + right_offset
            right_y = y + 2

            # Draws the connection line
            if len(lines) <= y + 1:
                lines.append(" " * 80)
            
            # Will ensure the line is long enough
            while len(lines[y + 1]) < x + len(nodeSTR) + 2:
                lines[y + 1] += " "

            # Will add the ASCCII branch character
            lines[y + 1] = lines[y + 1][:x + len(nodeSTR)] + "─┐" + lines[y + 1][x + len(nodeSTR) + 2:]

            # Will draw the right subtree recursively
            self._drawTree(node.getRight(), lines, right_x, right_y)
        


    def printVisualTree(self, output_file = None):
        if self._root is None:
            message = "The tree is empty."
            print(message)
            if output_file:
                output_file.write(message + "\n")
            return
        
        height = self._getTreeHeight(self._root)
        header = "\n" + "="*35 + "\n" + "Visual Tree Structure".center(35) + "\n" + "="*35
        print(header)

        for level in range(height):
            nodes = []
            self._collectingNodesByLevel(self._root, 0, level, nodes)

            # Creates a level header
            levelHeader = f"\nLevel {level}:"
            print(levelHeader)
            if output_file:
                output_file.write(levelHeader + "\n")

            # Formats all the nodes for this level
            nodeStrings = []
            for node in nodes:
                if node is not None:
                    nodeStrings.append(self._formatCurrencyShort(node.getData()))
                else:
                    nodeStrings.append("(empty)")
            
            # Prints out the nodes with some proper spacing
            if nodeStrings:
                nodeLine = "  " + "    ".join(nodeStrings)
                print(nodeLine)
                if output_file:
                    output_file.write(nodeLine + "\n")

        print("\n" + "="*35)
        if output_file:
            output_file.write("="*35 + "\n")
    
    def printCompactTree(self, output_file = None):
        if self._root is None:
            message = "The tree is empty"
            print(message)
            if output_file:
                output_file.write(message + "\n")
            return
        
        lines = []
        self._buildCompactTreeLines(self._root, lines, 0, "")

        header = "\n" + "=" * 35 + "\n" + "Compact Tree Structure".center(35) + "\n" + "=" * 35
        print(header)
        if output_file:
            output_file.write(header + "\n")

        for line in lines:
            print(line)
            if output_file:
                output_file.write(line + "\n")
        
        print("=" * 35)
        if output_file:
            output_file.write("=" * 35 + "\n")

    def printASCIITree(self, output_file = None):
        if self._root is None:
            message = "The tree is empty"
            print(message)
            if output_file:
                output_file.write(message + "\n")
            return
        
        lines = []
        self._drawTree(self._root, lines, 35, 0)
        
        header = "\n" + "="*35 + "\n" + "ASCII Art Tree".center(35) + "\n" + "="*35 + "\n"
        print(header)
        if output_file:
            output_file.write(header + "\n")

        for line in lines:
            print(line.rstrip())
            if output_file:
                output_file.write(line.rstrip() + "\n")

        print("="*35)
        if output_file:
            output_file.write("="*35 + "\n")

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
        
        self._root = self._deleteRecursive(self._root, data)
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
            result.append(current.getData())

            if current.getLeft() is not None:
                queue.enQueue(current.getLeft())
            if current.getRight() is not None:
                queue.enQueue(current.getRight())
        
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
    
    def isEmpty(self):
        return self._count == 0
    
    def empty(self):
        self._root = None
        self._count = 0

    def printAllTreeFormats(self, output_file = None):
        self.printTree(output_file)
        # self.printVisualTree(output_file)
        # ^ I do not like the result it puts out right now, might fix it in the future
        self.printASCIITree(output_file)
        self.printCompactTree(output_file)