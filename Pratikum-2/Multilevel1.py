class Animal:
    
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} speaks")

class Bird(Animal):
    
    def __init__(self, name, wingspan):
        super().__init__(name)
        self.wingspan = wingspan
    
    def fly(self):
        print(f"{self.name} Fly with wide wings{self.wingspan}")

class Parrot(Bird):

    def __init__(self, name, wingspan, color):
        super().__init__(name, wingspan)
        self.color = color

    def speak(self):
        print(f"{self.name} is a {self.color} The wings are red")

parrot = Parrot("Cacatuidae", 12, "red")
parrot.speak()
parrot.fly()