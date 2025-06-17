from linknode import LinkNode

class SingleLinkedList:

    def __init__(self):
        self._count = 0
        self._start = None
        self._end = None

    def addCurrency(self, currency, index):

        if index < 0 or index > self._count:
            raise IndexError("Index is out of bounds")
        
        new_node = LinkNode(currency)

        if index == 0:
            new_node.next = self._start
            self._start = new_node

            if self._count == 0:
                self._end = new_node

        elif index == self._count:
            self._end.next = new_node
            self._end = new_node

        else:
            prev = self._start

            for _ in range(index - 1):
                prev = prev.next
            
            new_node.next = prev.next
            prev.next = new_node
        
        self._count += 1
    
    def removeCurrency(self, param):
        if isinstance(param, int):
            index = param

            if index < 0 or index >= self._count:
                raise IndexError("Index is out of bounds")
            
            prev, current = None, self._start

            for _ in range(index):
                prev = current
                current = current.next
            
            if prev is None:
                self._start = current.next
            
            else:
                prev.next = current.next
            
            if current == self._end:
                self._end = prev
            
            self._count -= 1
            return current.data
        
        else:
            currency = param
            prev, current = None, self._start
            index = 0

            while current:
                if current.data == currency:
                    if prev is None:
                        self._start = current.next
                    
                    else:
                        prev.next = current.next
                    
                    if current == self._end:
                        self._end = prev
                    
                    self._count -= 1
                    return current.data
                
                prev = current
                current = current.next
                index += 1
            
            return None
        
    def findCurrency(self, currency):
        current, index = self._start, 0

        while current:
            if current.data == currency:
                return index
            
            current = current.next
            index += 1
        return -1
    
    def getCurrency(self, index):
        if index < 0 or index >= self._count:
            raise IndexError("Index is out of bounds")
        
        current = self._start

        for _ in range(index):
            current = current.next
        
        return current.data
    
    def stringifyList(self):
        result, current = "", self._start

        while current:
            result += str(current.data) + "\t"
            current = current.next

        return result.strip()

    def isListEmpty(self):
        return self._count == 0

    def countCurrency(self):
        return self._count

    def emptyList(self):
        self._start = None
        self._end = None
        self._count = 0    
    