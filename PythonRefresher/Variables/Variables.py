import sys

"""
Variables
"""
# Variables are containers for storing data values with memory addresses.
# Variables are symbolic names for memory locations that store data
#  Variables are memory allocations managed by the OS memory manager
# Variables are register/RAM addresses containing binary data
first_name = "Eric"
print(first_name)
first_name = "Melissa"
print(first_name)


'''
Variables
'''

class TaxCalculator:
    def __init__(self):
        self.cost = 0.0
        self.tax_percent = 0.0
    
    def calculate_total(self):
        self.cost = float(input("Enter the cost:"))
        self.tax_percent = float(input("Enter the tax percentage: "))
        Price = self.cost + (self.cost * self.tax_percent/100)
        print(Price)
        return Price

# Usage
calculator = TaxCalculator()
calculator.calculate_total()

class BankApplication:
    def __init__(self):
        self.balance = 0.0
        self.name = ""

    def deposit(self, name, amount):
        self.name = name
        self.balance += amount
        print(f"Deposited: {amount}")
        return self.balance

    def withdraw(self, name, amount):
        self.name = name
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Withdrew: {amount}")
        return self.balance

    def transfer(self, sender_name, receiver_account, amount):
        self.name = sender_name
        if amount > self.balance:
            print("Insufficient funds for transfer")
            return False
        else:
            self.balance -= amount
            receiver_account.balance += amount
            print(f"Transferred: {amount} from {sender_name} to {receiver_account.name}")
            return True

    def get_balance(self, name):
        print(f"Current balance of {name}: {self.balance}")
        return self.balance

# Usage
if __name__=="__main__":
    name = input("Enter your name: ")
    amount = float(input("Enter amount to deposit: "))
    withdraw_amount = float(input("Enter amount to withdraw: "))

    bank_app = BankApplication()
    bank_app.deposit(name, amount)
    bank_app.withdraw(name, withdraw_amount)
    bank_app.get_balance(name)
    
    # Money transfer example
    receiver_name = input("Enter receiver's name: ")
    transfer_amount = float(input("Enter amount to transfer: "))
    
    receiver_account = BankApplication()
    receiver_account.name = receiver_name
    
    bank_app.transfer(name, receiver_account, transfer_amount)
    bank_app.get_balance(name)
    receiver_account.get_balance(receiver_name)


# Variable ID and Memory Concepts Examples

# 1. Variable ID - Shows memory address of variables
print("\n=== Variable ID Examples ===")
x = 100
y = 100
z = 200

print(f"x = {x}, id(x) = {id(x)}")
print(f"y = {y}, id(y) = {id(y)}")
print(f"z = {z}, id(z) = {id(z)}")
print(f"x and y have same id: {id(x) == id(y)}")  # True for small integers

# 2. String Interning/String Pool
print("\n=== String Pool Examples ===")
str1 = "hello"
str2 = "hello"
str3 = "hello world"
str4 = "hello world"

print(f"str1 = '{str1}', id = {id(str1)}")
print(f"str2 = '{str2}', id = {id(str2)}")
print(f"str1 and str2 same id: {id(str1) == id(str2)}")  # True - string interning

print(f"str3 = '{str3}', id = {id(str3)}")
print(f"str4 = '{str4}', id = {id(str4)}")
print(f"str3 and str4 same id: {id(str3) == id(str4)}")

# 3. is vs == operator
print("\n=== 'is' vs '==' Examples ===")
a = [1, 2, 3] # List object
b = [1, 2, 3] # Different List object
c = a # Here the object reference is the same as a

print(f"a == b: {a == b}")  # True - same content
print(f"a is b: {a is b}")  # False - different objects
print(f"a is c: {a is c}")  # True - same object reference

# 4. Mutable vs Immutable Variables
print("\n=== Mutable vs Immutable Examples ===")
# Immutable (int, str, tuple)
num1 = 42
print(f"Before: num1 = {num1}, id = {id(num1)}")
num1 = 43
print(f"After: num1 = {num1}, id = {id(num1)}")  # Different ID

# Mutable (list, dict, set)
list1 = [1, 2, 3]
print(f"Before: list1 = {list1}, id = {id(list1)}")
list1.append(4)
print(f"After: list1 = {list1}, id = {id(list1)}")  # Same ID

# 5. Variable Reference Count
print("\n=== Reference Count Examples ===")

data = [1, 2, 3, 4, 5]
print(f"Reference count for data: {sys.getrefcount(data)}")

data_ref = data
print(f"Reference count after assignment: {sys.getrefcount(data)}")

del data_ref
print(f"Reference count after deletion: {sys.getrefcount(data)}")

# 6. Global vs Local Variables
print("\n=== Global vs Local Variable Scope ===")
global_var = "I am global"

def scope_example():
    local_var = "I am local"
    global global_var
    print(f"Inside function - global_var: {global_var}")
    print(f"Inside function - local_var: {local_var}")
    print(f"global_var id inside function: {id(global_var)}")

scope_example()
print(f"Outside function - global_var: {global_var}")
print(f"global_var id outside function: {id(global_var)}")

# 7. Variable Types and Memory
print("\n=== Variable Types and Memory ===")
integer_var = 100
float_var = 100.0
string_var = "100"
list_var = [100]
dict_var = {"key": 100}

print(f"integer_var: type={type(integer_var)}, size={sys.getsizeof(integer_var)} bytes")
print(f"float_var: type={type(float_var)}, size={sys.getsizeof(float_var)} bytes")
print(f"string_var: type={type(string_var)}, size={sys.getsizeof(string_var)} bytes")
print(f"list_var: type={type(list_var)}, size={sys.getsizeof(list_var)} bytes")
print(f"dict_var: type={type(dict_var)}, size={sys.getsizeof(dict_var)} bytes")

first_num=10
second_num=2
print(f"First number: {first_num} with object id:{id(first_num)}, Second number: {second_num} with object id:{id(second_num)}")
