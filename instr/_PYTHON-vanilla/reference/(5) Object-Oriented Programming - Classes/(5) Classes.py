## Object-Oriented Programming


# Class Definition
class Superclass:  # (!) Class name must starts with an uppercase letter
    
    # Initializer Method (Special)
    def __init__(self, data_1, data_2):           
        self.__attribute_1 = data_1 # (!) Two underscores in the front of identifier means private
        self.__attribute_2 = data_2
                             
    # Initializer Method Rule:
    # 1. Immediately after an object is created, the initializer method executes
    # 2. self parameter is automatically assigned the object that was just created
    # 3. (!) Initializer method is public even though it has two underscores in the front


    # Mutator Method / Accessor Method
    def set_attribute_1(self, data):    # Mutator Method (Setter)
        self.__attribute_1 = data

    def set_attribute_2(self, data):
        self.__attribute_2 = data

    def get_attribute_1(self):          # Accessor Method (Getter)
        return self.__attribute_1

    def get_attribute_2(self):
        return self.__attribute_2

    # self Parameter: 
    # 1. A method is called
    # 2. Python automatically passes a reference to the calling object into the method's first parameter
    # 3. self parameter will reference the calling object


    # State Method (Special)
    def __str__(self):
        string = ''
        string += '\n1st Data: ' + self.__attribute_1
        string += '\n2nd Data: ' + self.__attribute_2
        return string
    
    # State Method Rule:
    # 1. We do not directly call the state method to get the string contains the object's state
    # 2. it is called when we pass an object to the built-in print Function, then it returns the string
    # 3. it is called when we pass an object to the built-in str Function, then it returns the string
    # 4. (!) State method is public even though it has two underscores in the front


# Object-Oriented Programming Properties:
# 1. Abstraction (Encapsulation with Data Hiding)
# 2. Reusability (Multiple Instances)
# 3. Inheritance ("is a" Relationship)
# 4. Polymorphism (Override)


class Subclass(Superclass): # (!) Subclass (derived class, specialized) inherits attributes and methods from Superclass (base class, general)

    # Initializer Method
    def __init__(self, data_1, data_2, data_3):           
        Superclass.__init__(self, data_1, data_2)
        self.__attribute_3 = data_3


    # Mutator Method
    def set_attribute_3(self, data):
        self.__attribute_3 = data


    # Accessor Method
    def get_attribute_3(self):
        return self.__attribute_3

    # State Method (Special)
    def __str__(self):
        string = Superclass.__str__(self)
        string += '\n3rd Data: ' + self.__attribute_3
        return string

x = 'hi'
def main():
    print(x)
    # Object (Instance) Definition
    instance_1 = Superclass('Default Data 1', 'Default Data 2')
    instance_2 = Superclass('Default Data 1', 'Default Data 2')
    instance_3 = Subclass('Default Data 1', 'Default Data 2', 'Default Data 3')

    instance_1.set_attribute_1('Hi, There')
    instance_1.set_attribute_2('This is object-oriented programming')
    instance_3.set_attribute_1('Hi, There')
    instance_3.set_attribute_2('This is object-oriented programming')
    
    print(instance_1)
    print(instance_2)
    print(instance_3)
    
    show_attributes(Superclass('object itself can be', 'passed anywhere'))
    show_attributes(instance_3)


def show_attributes(instance):
    print()
    
    # isinstance Function
    if isinstance(instance, Subclass):                          # returns true if arg1 is a instance (element) of the class arg2
        print('Attribute #1: ' + instance.get_attribute_1())
        print('Attribute #2: ' + instance.get_attribute_2())
        print('Attribute #3: ' + instance.get_attribute_3())
    elif isinstance(instance, Superclass):                      # returns true if arg1 is a instance (element) of the class arg2
        print('Attribute #1: ' + instance.get_attribute_1())
        print('Attribute #2: ' + instance.get_attribute_2())
    else:
        print('This is not either the instance of Superclass or Subclass')

main()
