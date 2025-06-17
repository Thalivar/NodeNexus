class Currency:

    def __init__(self, amount = 0.0):
        
        if isinstance(amount, (int, float)):
            self._whole_part = int(amount)
            self._fractional_part = int((amount - self._whole_part) * 100 + 0.5)

        else:
            self._whole_part = 0
            self._fractional_part = 0

    @property
    def whole_part(self):
        return self._whole_part
    
    @property
    def fractional_part(self):
        return self._fractional_part
    
    def add(self, other):

        if not isinstance(other, Currency):
            raise TypeError("You can only add Currency objects.")
        
        total = (self._whole_part * 100 + self._fractional_part 
                 + other._whole_part * 100 + other.fractional_part)
        
        self._whole_part = total // 100
        self._fractional_part = total % 100

    def subtract(self, other):
        if not isinstance(other, Currency):
            raise TypeError("You can only subtract Currency objects.")
        
        total = (self._whole_part * 100 + self._fractional_part
                  - other.whole_part * 100 - other.fractional_part)

        if total < 0:
            raise ValueError("The subtraction result would be negative.")
        
        self._whole_part = total // 100
        self._fractional_part = total % 100

    def get_currency_name(self):
        raise NotImplementedError("Subclasses must implement get_currency_name")

    def __eq__(self, other):
        if not isinstance(other, Currency):
            return False
        
        return (self._whole_part == other.whole_part 
                and self._fractional_part == other.fractional_part)
    
    def __str__(self):
        return f"{self._whole_part}.{self._fractional_part:02d} {self.get_currency_name()}"
    
class Dollar(Currency):

    def __init__(self, amount=0):
        super().__init__(amount)

    def get_currency_name(self):
        return "$"
    
    def __str__(self):
        return f"$ {self._whole_part}.{self._fractional_part:02d}"