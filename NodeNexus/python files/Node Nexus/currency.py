class Currency:

    def __init__(self, amount = 0.0):
        
        if isinstance(amount, (int, float)):
            self._wholePart = int(amount)
            self._fractionalPart = int((amount - self._wholePart) * 100 + 0.5)

        else:
            self._wholePart = 0
            self._fractionalPart = 0

    @property
    def whole_part(self):
        return self._wholePart
    
    @property
    def fractional_part(self):
        return self._fractionalPart
    
    def add(self, other):

        if not isinstance(other, Currency):
            raise TypeError("You can only add Currency objects.")
        
        total = (self._wholePart * 100 + self._fractionalPart 
                 + other._wholePart * 100 + other._fractionalPart)
        
        self._wholePart = total // 100
        self._fractionalPart = total % 100

    def subtract(self, other):
        if not isinstance(other, Currency):
            raise TypeError("You can only subtract Currency objects.")
        
        total = (self._wholePart * 100 + self._fractionalPart
                  - other._wholePart * 100 - other.fractional_part)

        if total < 0:
            raise ValueError("The subtraction result would be negative.")
        
        self._wholePart = total // 100
        self._fractionalPart = total % 100

    def getCurrencyName(self):
        raise NotImplementedError("Subclasses must implement get_currency_name")

    def __eq__(self, other):
        if not isinstance(other, Currency):
            return False
        
        return (self._wholePart == other.whole_part 
                and self._fractionalPart == other.fractional_part)
    
    def __str__(self):
        return f"{self._wholePart}.{self._fractionalPart:02d} {self.get_currency_name()}"
    
class Dollar(Currency):

    def __init__(self, amount=0):
        super().__init__(amount)

    def get_currency_name(self):
        return "$"
    
    def __str__(self):
        return f"$ {self._wholePart}.{self._fractionalPart:02d}"