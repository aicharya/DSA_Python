class Person():

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.prod = list(map(lambda x : x, range(self.age)))
        self.mapped = map(lambda x: x, range(self.age))
        
    ln = lambda self, x : x
    
    def details(self):
        print("Hi, I am {0}; and ".format(self.name))
        print("I am " + str(self.age) + " years old.")
        print(self.prod)
        print(self.mapped)
        
        

p1 = Person("Leo", 35)
p1.details()
print(p1.ln(5))
