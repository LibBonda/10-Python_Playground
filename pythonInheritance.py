#Create a class named Person, with firstname and lastname properties, and a printname method:

class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname 
        
    def printname(self):
        print(self.firstname +'' + self.lastname)
        
#Use the Person class to create an object, and then execute the printname method:
x = Person('John ', 'Smith')

x.printname()

#To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class:

# class Student(Person):
#     pass                #Use the pass keyword when you do not want to add any other properties or methods to the class.
#The __init__() function is called automatically every time the class is being used to create a new object. When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.
   

#Python also has a super() function that will make the child class inherit all the methods and properties from its parent:
class Student(Person):
    def __init__(self, firstname, lastname):
        super().__init__(firstname, lastname)
        self.birthday = '1990-01-01'
        self.graduationYear = '2020'
        
y = Student('Jane',  ' Doe')
y.printname()
print(y.birthday)
print(y.graduationYear)