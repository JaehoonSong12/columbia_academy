# oop_explained.sample.py               <- how PVM is recognizing

##### TARGETS (members of a module)
## functions (def): 
#       - encapsulation 
#       - inheritance
#       - account_summary
#       - polymorphism
## classes (class with methods):    
#       - BankAccount       (methods: __init__, deposit, withdraw, get_balance), 
#       - SavingsAccount    (methods: __init__, apply_interest),
# `methods` means `functions enclosed in a class`


# Usage: 
    # # importing syntax #1            <- is more common, but can cause naming conflict
    # from oop_explained.sample import encapsulation
    # encapsulation()            <- don't know which encapsulation to execute
    # encapsulation()

    # # importing syntax style #2         <- is more wordy, but resolves any issues with vague naming
    # import oop_explained.sample
    # oop_explained.sample.encapsulation()
    # encapsulation()



# OOP #1, Encapsulation
# Creating a new data type.
# in computers, what are the primitive data types?
# - integers, strings, floats

# What was the concept of Abstraction?
# - Making things seem easier and less complicated.
#
# `Abstraction` is a core principle for `Procedural (functions-oriented)` programming Paradigm.
# Abstraction is possible since functions (API, procedurals) hide all the detailes in there!
# 
# Real World Example:
# In a room, there are two students, Jaehoon and Taiyun, you are going to make a program 
# that simulates what is going to happen in the room.
# Assume these are going to happen. 
# < Procedurals >
# 1. Jaehoon is 180 cm, 82 kg, and black-haired
# 2. Taiyun is black haired, is 170 cm, 75 kg
# 3. Jaehoon "says" "Hi Taiyun"
# 4. Taiyun "says" "Hi Jaehoon"
# 5. Jaehoon "reports" all his data (height, weight, and hair-color)
# 6. Taiyun "reports" all his data (height, weight, and hair-color)
#
# Define attributes for Jaehoon
jaehoon_name = "Jaehoon"
jaehoon_height = 180  # in cm
jaehoon_weight = 82  # in kg
jaehoon_hair_color = "black"

# Define attributes for Taiyun
taiyun_name = "Taiyun"
taiyun_height = 170  # in cm
taiyun_weight = 75  # in kg
taiyun_hair_color = "black"

# Actions in the room
print(f'{jaehoon_name} says: "Hi Taiyun"')
print(f'{taiyun_name} says: "Hi Jaehoon"')

# Jaehoon reports his data
print(f"{jaehoon_name} reports: Height: {jaehoon_height} cm, Weight: {jaehoon_weight} kg, Hair color: {jaehoon_hair_color}")

# Taiyun reports his data
print(f"{taiyun_name} reports: Height: {taiyun_height} cm, Weight: {taiyun_weight} kg, Hair color: {taiyun_hair_color}")

######### This is awful! We should do a lot of labor every time we have more people!



# < Object-orietned Approach >
# assume we have way more people, we need to be productive, like industrial revolution.
# Then we have to encapsulate all the procedurals into our "blueprint (factory)" so factories 
# do simple and repetitive work for us.
class Person:
    def __init__(self, name, height, weight, hair_color):
        self.name = name
        self.height = height
        self.weight = weight
        self.hair_color = hair_color

    def say(self, message):
        print(f'{self.name} says: "{message}"')

    def report(self):
        print(f"{self.name} reports: Height: {self.height} cm, Weight: {self.weight} kg, Hair color: {self.hair_color}")


# Create five people using the blueprint (factory)
jaehoon = Person(name="Jaehoon", height=180, weight=82, hair_color="black")
taiyun = Person(name="Taiyun", height=170, weight=75, hair_color="black")
sora = Person(name="Sora", height=165, weight=60, hair_color="brown")
minji = Person(name="Minji", height=172, weight=68, hair_color="blonde")
yuna = Person(name="Yuna", height=160, weight=55, hair_color="red")

# Put all people into a list for easy processing
people = [jaehoon, taiyun, sora, minji, yuna]

# Simulate their interactions
for person in people:
    person.say(f"Hi everyone, I am {person.name}!")

for person in people:
    person.report()







# in the real world, can we represent everything with "integers, strings, floats"?
# 
class BankAccount: 
    """
    A class representing a bank account.

    Attributes:
        account_holder (str): Name of the account holder.
        balance (float): Current balance in the account.
    """
    def __init__(self, account_holder, initial_balance=0.0):
        """
        Initializes a new BankAccount object.

        Args:
            account_holder (str): The name of the account holder.
            initial_balance (float): Initial deposit amount (default is 0.0).
        """
        self.account_holder = account_holder  # Public attribute
        self.__balance = initial_balance     # Private attribute (encapsulation)

    def deposit(self, amount):
        """
        Deposit money into the account.

        Args:
            amount (float): Amount to deposit (must be positive).
        """
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount:.2f}. New balance is ${self.__balance:.2f}.")
        else:
            print("Deposit amount must be positive!")

    def withdraw(self, amount):
        """
        Withdraw money from the account.

        Args:
            amount (float): Amount to withdraw.

        Returns:
            bool: True if withdrawal is successful, False otherwise.
        """
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance is ${self.__balance:.2f}.")
            return True
        elif amount > self.__balance:
            print("Insufficient balance!")
            return False
        else:
            print("Withdrawal amount must be positive!")
            return False

    def get_balance(self):
        """
        Get the current account balance.

        Returns:
            float: The current balance.
        """
        return self.__balance

def encapsulation():
    print("=== Bank Account System ===")
    account1 = BankAccount("Alice", 1000.0)
    account2 = BankAccount("Bob", 500.0)

    # Use methods of the objects
    account1.deposit(200)
    account1.withdraw(500)
    print(f"Alice's current balance: ${account1.get_balance():.2f}")

    account2.withdraw(600)  # This will fail due to insufficient balance
    print(f"Bob's current balance: ${account2.get_balance():.2f}")













# OOP #2, Inheritance
class SavingsAccount(BankAccount):
    """
    A subclass of BankAccount representing a savings account.
    """
    def __init__(self, account_holder, initial_balance=0.0, interest_rate=0.01):
        """
        Initialize a SavingsAccount object.

        Args:
            account_holder (str): The name of the account holder.
            initial_balance (float): Initial deposit amount (default is 0.0).
            interest_rate (float): Annual interest rate (default is 1%).
        """
        super().__init__(account_holder, initial_balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        """
        Apply annual interest to the account balance.
        """
        interest = self.get_balance() * self.interest_rate
        self.deposit(interest)
        print(f"Applied interest of ${interest:.2f} at a rate of {self.interest_rate*100:.2f}%.")

def inheritance():
    print("\n=== Savings Account System ===")
    savings = SavingsAccount("Charlie", 1000.0, 0.05)  # 5% interest rate
    savings.apply_interest()
    print(f"Charlie's current balance: ${savings.get_balance():.2f}")














# OOP #3, Polymorphism
def account_summary(account):
    """
    Display a summary of the account. Works for any BankAccount or subclass.

    Args:
        account (BankAccount): The account to summarize.
    """
    print(f"Account Holder: {account.account_holder}")
    print(f"Account Balance: ${account.get_balance():.2f}")

def polymorphism():
    print("=== Bank Account System ===")
    account1 = BankAccount("Alice", 1000.0)
    account2 = BankAccount("Bob", 500.0)
    print("\n=== Savings Account System ===")
    savings = SavingsAccount("Charlie", 1000.0, 0.05)  # 5% interest rate
    savings.apply_interest()
    print(f"Charlie's current balance: ${savings.get_balance():.2f}")
    print("\n=== Account Summary ===")
    account_summary(account1)  # Works for BankAccount
    account_summary(savings)   # Works for SavingsAccount (polymorphism)