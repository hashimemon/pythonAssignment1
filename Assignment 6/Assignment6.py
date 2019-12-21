print("Q1. Define Object Oriented Programming Language?")
print("Ans: Object-oriented programming (OOP) is a programming language model in which programs are organized around data, or objects. An object can be defined as a data field that has unique attributes and behavior. Examples of an object can range from physical entities, such as a human being that is described by properties like name and address")
print("\n")
print("Q2. List down the Benefits of OOP?")
print("Ans: 1. Modularity for easier troubleshooting Example: When working with object-oriented programming languages, you know exactly where to look. “Oh, the car object broke down? The problem must be in the Car class!” You don’t have to muck through anything else. \n 2. Reuse of code through inheritance Example: if you want to make a change to all Car objects, regardless of type? Simply make a change to your Car class, and all car objects will simply inherit the new code \n 3. Flexibility through polymorphism \n 4. Effective problem solving")
print("\n")
print("Q3. Differentiate between function and method")
print("Ans: A function is a piece of code that is called by name. It can be passed data to operate on (i.e. the parameters) and can optionally return data (the return value). All data that is passed to a function is explicitly passed. A method is a piece of code that is called by a name that is associated with an object.")
print("\n")
print("Q4. Define the following terms:")
print("Ans: Class : In object-oriented programming, a class is a blueprint for creating objects (a particular data structure), providing initial values for state (member variables or attributes), and implementations of behavior (member functions or methods). The user-defined objects are created using the class keyword. \n Object : An object is nothing but a self-contained component which consists of methods and properties to make a particular type of data useful. Object determines the behavior of the class. \n Attribute : In Object-oriented programming(OOP), classes and objects have attributes. Attributes are data stored inside a class or instance and represent the state or quality of the class or instance.One can think of attributes as noun or adjective, while methods are the verb of the class. \n Behavior : A class's behavior determines how an instance of that class operates; for example, how it will 'react' if asked to do something by another class or object or if its internal state changes. Behavior is the only way objects can do anything to themselves or have anything done to them.")

print("\n")

print("Q.5 Write a code in python in which create a class named it Car which have 5 attributes such like (model, color and name etc.) and 3 methods. And create 5 object instance from that class.")

class Car():
    # Init method
    def __init__(self, name, model, color, company, transmission):
        self.name = name
        self.model = model
        self.color = color
        self.company = company
        self.transmission = transmission
        
    # show_properties method
    def show_properties(self):
        print("Car Properties")
        print(f"Name         : {self.name}")
        print(f"Model        : {self.model}")
        print(f"Color        : {self.color}")
        print(f"Company      : {self.company}")
        print(f"Transmission : {self.transmission} \n")
        
    
    # update_name method
    def update_name(self, newname):
        self.name = newname
    
    # update_color method
    def update_color(self, newcolor):
        self.color = newcolor


        
# Objects

car1 = Car("Civic", 2019, "Black", "Honda", "Auto")
car2 = Car("Coure", 2009, "Brown", "Diahatsu", "Manual")
car3 = Car("Corolla", 2016, "Black", "Toyota", "Auto")
car4 = Car("Mehran", 2017, "Grey", "Suzuki", "Manual")
car5 = Car("City", 2018, "White", "Honda", "Auto")

# Calling methods
car1.show_properties()
car2.show_properties()
car3.show_properties()
car4.show_properties()
car5.show_properties()
        
    
# Changing name
 # before Changing
print("Before Changing : ",car1.name)
car1.update_name("Pajero")
print("After Changing : ",car1.name)
