def calculate_area(radius):return 3.14159*radius*radius

def print_areas():
    radii = [1, 2, 3, 4, 5]
    for r in radii:print("Area of circle with radius", r, "is", calculate_area(r))

class SampleClass:
    def __init__(self, name):
        self.name=name

    def greet(self):print("Hello, " + self.name) 
unused_variable = 42

def example_func():
    for i in range(10):print(i, end=' ') 
    x = [1,2,3,4,5] 
    y = [i*i for i in x] 
    print(y)

print_areas()

sc = SampleClass("World")
sc.greet()

def long_line_function():
    print("This is a very long line that will likely exceed the maximum line length limit set by most linters, which is typically around 80 or 100 characters depending on the linter configuration. Additionally, this long line also lacks proper punctuation and spacing, making it even more challenging to read and understand, further illustrating the importance of keeping lines within a reasonable length for better readability and maintainability.")

def another_example():
    a,b,c = 1,2,3 
    if(a+b==c):print("a + b equals c") 
