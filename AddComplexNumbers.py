class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __str__(self):
        return str(self.real) + f'+{str(self.imaginary)}i'

    def __add__(self, other):
        real = self.real + other.real
        imaginary = self.imaginary + other.imaginary
        return Complex(real, imaginary)

obj = Complex(10, 20)
obj1 = Complex(5, 6)
print(obj+obj1)


# string formatting
name = 'Garima'
lastname = "Agarwal"
output = "My name is Garima"

print("My name is ", name)
print(str.format("My name is {} {}", name, lastname))
print("My name is %s %s" % (name, lastname))
print(f"My name is {name} {lastname}, I am an Engineer")





