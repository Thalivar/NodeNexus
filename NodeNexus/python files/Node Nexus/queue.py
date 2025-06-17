from single_linked_list import SingleLinkedList

class Queue(SingleLinkedList):

    def __init__(self):
        super().__init__()

        self.__addCurrency = self.addCurrency
        self.__removeCurrency = self.removeCurrency
        self.addCurrency = None
        self.removeCurrency = None

    def enQueue(self, currency):
        self.__addCurrency(currency, self._count)

    def deQueue(self):
        return self.__removeCurrency
    
    def peekFront(self):
        if self.isListEmpty():
            raise IndexError("You cannont peak into a empty queue")
        
        return self.getCurrency(0)
    
    def peekRear(self):
        if self.isListEmpty():
            return None
        
        return self.getCurrency(self._count - 1)
    
    def stringifyQueue(self):
        return self.stringifyList()
    
    def emptyQueue(self):
        self.emptyList()