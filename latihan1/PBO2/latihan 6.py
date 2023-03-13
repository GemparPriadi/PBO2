class kalkulator:
    @staticmethod
    def add(x, y):
        return x + y
    
    @staticmethod
    def subtract(x, y):
        return x - y
    
    @staticmethod
    def multiply(x, y):
        return x * y
    
    @staticmethod
    def divide(x, y):
        if y == 0:
            raise ValueError('Tidak dapat dibagi nol.')
        return x / y
    
# Memanggil metode statis add() dan subtrack() di dalam class match
print(kalkulator.add(10, 7))         # Output: 17
print(kalkulator.subtract(27, 7))    # Output: 20

# Memanggil metode statis multiply() dan divide() di dalam class match
print(kalkulator.multiply(7, 2))     # Output: 14
print(kalkulator.divide(10, 2))      # Output: 5