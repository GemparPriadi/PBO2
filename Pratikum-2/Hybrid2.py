class Seseorang:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
    def get_info(self):
        print("Nama:", self.name)
        print("Umur:", self.age)
        print("Alamat:", self.address)
# Single Inheritance
class Mahasiswa(Seseorang):
    def __init__(self, name, age, address, student_id):
        super().__init__(name, age, address)
        self.student_id = student_id
    def get_info(self):
        super().get_info()
        print("ID Pelajar:", self.student_id)
# Single Inheritance
class Employee(Seseorang):
    def __init__(self, name, age, address, employee_id, salary):
        super().__init__(name, age, address)
        self.employee_id = employee_id
        self.salary = salary
    def get_info(self):
        super().get_info()
        print("ID Pekerja:", self.employee_id)
        print("Gaji:", self.salary)
# Multiple Inheritance
class Penulis(Employee, Mahasiswa):
    def __init__(self, name, age, address, employee_id, salary, student_id, 
published_books):
        Employee.__init__(self, name, age, address, employee_id, salary)
        Mahasiswa.__init__(self, name, age, address, student_id)
        self.published_books = published_books
    def get_info(self):
        super().get_info()
        print("ID Pelajar:", self.student_id)
        print("Buku Publikasi:", self.published_books)
    def display_info(self):
        super().get_info()
        print(f"Nama: ", self.name)
        print(f"Umur: ", self.age)
        print(f"Alamat: ", self.address)
        print(f"ID Pelajar: ", self.student_id)
        print(f"ID Pekerja: ", self.employee_id)
        print(f"Gaji: ", self.salary)
        print(f"Buku Publikasi: ", self.published_books)
        
PenulisA = Penulis("Gempar Priadi", 20, "Panguragan", 210511036, "$1000.000", 260703, 
"MATEMATIKA PINTAR")
PenulisA.display_info()
