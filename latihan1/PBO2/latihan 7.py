class Celcius:
    @staticmethod
    def to_fahrenheit(celcius):
        return (celcius * 9/5) + 32
    
    @staticmethod
    def to_kelvin(celcius):
        return celcius + 273.15
    
    @staticmethod
    def to_reamur(celcius):
        return celcius * 4/5
    
mycelcius = 80
myfahrenheit = Celcius.to_fahrenheit(mycelcius)
print(myfahrenheit)