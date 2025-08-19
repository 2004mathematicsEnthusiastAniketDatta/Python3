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

import dis
import time
import sys
import keyword
import this
from typing import Final
import gc
import weakref
import os
from dataclasses import dataclass
import threading
from contextlib import contextmanager
from typing import Union, Optional, Dict, Any, List
from abc import ABC, abstractmethod
from collections import namedtuple
import logging
from functools import wraps
from decimal import Decimal
from enum import Enum, IntEnum, Flag, IntFlag
from dataclasses import dataclass, field
from collections import deque, defaultdict, Counter, OrderedDict, ChainMap
from typing import List, Dict, Tuple, Optional, Union, Any, Callable
from typing import TypeVar, Generic
import hashlib

# Compilers and Interpreters

# BASIC DEFINITIONS
# Compiler: Translates the entire program into machine code or bytecode before execution
# Interpreter: Translates and executes code line by line at runtime

# LANGUAGE LEVELS
# Low-level languages: Assembly languages, closer to machine code
# High-level languages: Closer to human languages, easier to read and write (Python, Java, C++)
# Machine code: Binary code consisting of 0s and 1s that computers understand directly

# LANGUAGE CLASSIFICATION
# C/C++: Compiled languages - entire code is compiled to machine code before execution
# Python: Hybrid approach - compiles to bytecode (.pyc files), then interprets bytecode
# Ruby: Interpreted language - parses and executes directly (though modern implementations may vary)

# EXECUTION FILES
# C/C++: .exe (Windows), .out or no extension (Linux/Mac)
# Python: .pyc files (bytecode) stored in __pycache__ directory

# HISTORICAL EVOLUTION
# 1990s: Clear compiler/interpreter divide
# 2000s: JIT compilation emerged (Java HotSpot, .NET)
# 2010s: Modern interpreters use sophisticated optimization
# Today: Hybrid approaches dominate

# PERFORMANCE IMPLICATIONS
# Compilation: Slower build time, faster execution
# Interpretation: Faster development cycle, slower execution
# JIT: Best of both worlds for long-running applications

# DEVELOPMENT ENVIRONMENTS
# IDE: Integrated Development Environment for running programs
# VS Code: Multi-language IDE
# IDLE: Simple IDE for Python
# Google Colab: Cloud-based Jupyter notebook environment

print("Hello, World!")

# COMPARISON: C++ vs Python

# 1. COMPILATION MODEL
# C++: Compiled to machine code before execution
# Python: Compiled to bytecode, then interpreted by Python Virtual Machine

# 2. SYNTAX
# C++: Verbose syntax with semicolons and curly braces
# Python: Clean, readable syntax with indentation-based structure

# 3. MEMORY MANAGEMENT
# C++: Manual memory management (new/delete, malloc/free)
# Python: Automatic garbage collection

# 4. PERFORMANCE
# C++: Faster execution due to direct machine code compilation
# Python: Slower execution due to interpretation overhead

# 5. VARIABLE DECLARATION
# C++: Static typing - must declare variable types (int a = 10;)
# Python: Dynamic typing - variables can hold any type (a = 10)

# 6. DEVELOPMENT SPEED
# C++: Longer development time due to complexity
# Python: Faster development due to simplicity

# 7. USE CASES
# C++: System programming, game development, embedded systems
# Python: Web development, data science, automation, AI/ML

# 8. LEARNING CURVE
# C++: Steeper learning curve
# Python: Beginner-friendly

# 9. LIBRARIES AND ECOSYSTEM
# C++: Rich libraries for system-level programming and graphics
# Python: Extensive libraries for web development, data analysis, and machine learning

# 10. SETUP REQUIREMENTS
# C++: Requires header files and libraries for basic operations
# Python: No imports needed for basic operations like printing

# COMPILER PROCESS (Behind the Scenes)

# 1. LEXICAL ANALYSIS (Tokenization)
#    - Source code broken into tokens (keywords, identifiers, operators, literals)
#    - Example: "int x = 5;" → [INT, IDENTIFIER(x), ASSIGN, LITERAL(5), SEMICOLON]

# 2. SYNTAX ANALYSIS (Parsing)
#    - Tokens organized into Abstract Syntax Tree (AST)
#    - Checks grammar rules compliance
#    - Creates hierarchical code structure

# 3. SEMANTIC ANALYSIS
#    - Type checking and variable declaration verification
#    - Scope resolution
#    - Ensures variables are declared before use

# 4. INTERMEDIATE CODE GENERATION
#    - Converts AST to platform-independent intermediate representation (IR)
#    - Three-address code or similar formats

# 5. CODE OPTIMIZATION
#    - Constant folding, dead code elimination
#    - Loop optimization, register allocation
#    - Improves performance without changing functionality

# 6. TARGET CODE GENERATION
#    - Converts optimized IR to machine code
#    - Platform-specific instructions (x86, ARM, etc.)

# INTERPRETER PROCESS (Behind the Scenes)

# 1. LEXICAL ANALYSIS (Real-time)
#    - Tokenizes source code line by line
#    - No separate compilation phase

# 2. SYNTAX ANALYSIS (On-the-fly)
#    - Parses tokens immediately
#    - Builds temporary AST nodes

# 3. DIRECT EXECUTION
#    - Executes AST nodes immediately
#    - No intermediate code generation
#    - Maintains execution environment

# COMPILATION PIPELINE
# Source Code → Preprocessor → Compiler → Assembler → Linker → Executable

# ASSEMBLY LANGUAGE EXAMPLE
# C code: int x = 5;
# Assembly: mov eax, 5        ; Load 5 into register
#          mov [x], eax       ; Store register value to memory

# MACHINE CODE LEVEL
# Assembly converted to binary instructions
# Example: mov eax, 5 → B8 05 00 00 00 (hexadecimal)

# MEMORY LAYOUT DURING EXECUTION
# Stack: Local variables, function parameters
# Heap: Dynamic memory allocation
# Data: Global and static variables
# Code: Executable instructions

# INTERPRETER EXECUTION MODEL
# 1. Fetch instruction from source
# 2. Decode instruction meaning
# 3. Execute instruction directly
# 4. Update program state
# 5. Move to next instruction

# PYTHON'S HYBRID APPROACH
# 1. Source code (.py) → Bytecode (.pyc)
# 2. Python Virtual Machine (PVM) interprets bytecode
# 3. Bytecode is platform-independent
# 4. Optional JIT compilation for performance

# Python bytecode example:
# Python code: x = 5
# Bytecode: LOAD_CONST 5, STORE_NAME x

# PYTHON TRANSLATION PROCESS
# 1. Python source code is compiled to bytecode (.pyc files)
# 2. .pyc files stored in __pycache__ directory
# 3. Bytecode executed by Python interpreter line by line
# 4. .pyc files enable faster execution by avoiding recompilation
# 5. Bytecode is platform-independent but Python version specific

# ADVANTAGES AND DISADVANTAGES

# COMPILED LANGUAGES (C/C++)
# Advantages:
# - Faster execution speed
# - Better performance for resource-intensive tasks
# - No runtime dependencies
# - Early error detection

# Disadvantages:
# - Longer development cycle
# - Platform-specific executables
# - More complex memory management
# - Less flexibility during runtime

# INTERPRETED LANGUAGES (Python)
# Advantages:
# - Faster development and testing
# - Interactive development environment
# - Platform independence
# - Dynamic typing flexibility

# Disadvantages:
# - Slower execution speed
# - Runtime error discovery
# - Dependency on interpreter
# - Source code exposure

# MODERN COMPILER OPTIMIZATIONS
# 1. Inline function expansion
# 2. Loop unrolling
# 3. Dead code elimination
# 4. Constant propagation
# 5. Register allocation
# 6. Instruction scheduling

# JUST-IN-TIME (JIT) COMPILATION
# Combines compilation and interpretation benefits
# Examples: Java HotSpot, C# .NET, PyPy for Python
# Optimizes frequently executed code paths
# Adaptive optimization based on runtime behavior

# CROSS-COMPILATION
# Compiling code on one platform for execution on another
# Example: Compiling on Windows for Linux deployment
# Requires target platform libraries and headers

# DEBUGGING DIFFERENCES
# Compiled languages: Use debuggers like GDB, Visual Studio debugger
# Interpreted languages: Built-in debugging, print statements, interactive shells

# PRACTICAL EXAMPLES

# Example 1: Simple variable assignment
x = 10
print(f"Value of x: {x}")

# Example 2: Function definition and call
def greet(name):
    return f"Hello, {name}!"

message = greet("World")
print(message)

# Example 3: Loop demonstration
for i in range(5):
    print(f"Iteration: {i}")

# Example 4: Conditional statement
age = 25
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

# Example 5: List operations
numbers = [1, 2, 3, 4, 5]
squared = [x**2 for x in numbers]
print(f"Original: {numbers}")
print(f"Squared: {squared}")

# COMPILATION COMMANDS (Reference)
# C++: g++ -o program program.cpp
# Python: python program.py (no compilation needed)
# Java: javac Program.java && java Program

# PYTHON BYTECODE INSPECTION

def sample_function():
    x = 10
    y = 20
    return x + y

# Uncomment to see bytecode
# dis.dis(sample_function)

# PERFORMANCE COMPARISON EXAMPLE

def timing_example():
    start_time = time.time()
    # Simple calculation
    result = sum(range(1000000))
    end_time = time.time()
    print(f"Calculation result: {result}")
    print(f"Time taken: {end_time - start_time:.6f} seconds")

timing_example()

# MEMORY MANAGEMENT EXAMPLE

# Check memory usage of different data types
print(f"Integer size: {sys.getsizeof(42)} bytes")
print(f"String size: {sys.getsizeof('Hello')} bytes")
print(f"List size: {sys.getsizeof([1, 2, 3])} bytes")

# EXCEPTION HANDLING
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
except Exception as e:
    print(f"An error occurred: {e}")

# FILE OPERATIONS
try:
    with open('example.txt', 'w') as file:
        file.write("This is a test file.\n")
        file.write("Demonstrating file operations.\n")
    
    with open('example.txt', 'r') as file:
        content = file.read()
        print("File content:")
        print(content)
except FileNotFoundError:
    print("File not found!")
except IOError:
    print("Error reading/writing file!")

# OBJECT-ORIENTED PROGRAMMING EXAMPLE
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old."

# Create and use object
student = Student("Alice", 20)
print(student.introduce())

# LAMBDA FUNCTIONS
square = lambda x: x**2
print(f"Square of 5: {square(5)}")

# Filter even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {evens}")

# FINAL SUMMARY
print("\n" + "="*50)
print("COMPILATION vs INTERPRETATION SUMMARY")
print("="*50)
print("✓ Compilers translate entire programs before execution")
print("✓ Interpreters execute code line by line")
print("✓ Modern languages often use hybrid approaches")
print("✓ Choice depends on use case, performance needs, and development speed")
print("✓ Python uses bytecode compilation + interpretation")
print("="*50)
# In Interpreters , if there is an error in any line of the program , the lines before the error will be executed and the lines after the error will not be executed
# In compiler based languages, errors are caught at compile time and the program does not run until all errors are fixed.

# PYTHON SYNTAX, INDENTATION AND COMMENTS

# PYTHON SYNTAX FUNDAMENTALS
# Python syntax refers to the rules that define how Python programs are written
# Python is known for its clean, readable syntax that emphasizes code readability

# BASIC SYNTAX RULES
# 1. Python is case-sensitive (variable != Variable)
# 2. No semicolons required at end of statements
# 3. No curly braces for code blocks
# 4. Uses indentation to define code structure

# INDENTATION IN PYTHON
print("\nPYTHON INDENTATION:")
print("="*30)

# 1. INDENTATION IMPORTANCE
# - Python uses indentation to define code blocks
# - Standard indentation is 4 spaces (PEP 8 recommendation)
# - Consistent indentation is mandatory
# - Mixing tabs and spaces causes IndentationError

# 2. INDENTATION EXAMPLES

# Correct indentation with if statement
age = 18
if age >= 18:
    print("You are an adult")
    print("You can vote")
else:
    print("You are a minor")
    print("You cannot vote")

# Correct indentation with loops
for i in range(3):
    print(f"Number: {i}")
    if i == 2:
        print("Last number!")

# Nested indentation
for i in range(2):
    print(f"Outer loop: {i}")
    for j in range(2):
        print(f"  Inner loop: {j}")
        if j == 1:
            print("    Nested condition")

# Function indentation
def calculate_area(length, width):
    area = length * width
    return area

result = calculate_area(5, 3)
print(f"Area: {result}")

# Class indentation
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)

# 3. INDENTATION ERRORS
# IndentationError: Expected an indented block
# IndentationError: Unindent does not match any outer indentation level

# COMMENTS IN PYTHON
print("\nPYTHON COMMENTS:")
print("="*20)

# 1. SINGLE-LINE COMMENTS
# This is a single-line comment
# Comments start with the hash symbol (#)
# They are ignored by the Python interpreter

x = 5  # This is an inline comment
y = 10  # Another inline comment

# 2. MULTI-LINE COMMENTS
# Python doesn't have a specific multi-line comment syntax
# Use multiple single-line comments for multi-line comments
# Like this example
# Each line needs a # symbol

# 3. DOCSTRINGS (Documentation Strings)
# Triple quotes for multi-line strings that serve as documentation

def example_function():
    """
    This is a docstring.
    It provides documentation for the function.
    It can span multiple lines.
    """
    return "Hello, World!"

# Docstring for classes
class ExampleClass:
    """
    This is a class docstring.
    It describes what the class does.
    """
    
    def example_method(self):
        """
        This is a method docstring.
        It explains what the method does.
        """
        pass

# 4. COMMENT BEST PRACTICES
# - Use comments to explain WHY, not WHAT
# - Keep comments concise and relevant
# - Update comments when code changes
# - Avoid obvious comments

# Good comment - explains WHY
# price = base_price * 1.08  # Add 8% sales tax

# Bad comment - explains obvious WHAT
# price = base_price * 1.08  # Multiply base_price by 1.08

# PYTHON SYNTAX FEATURES
print("\nPYTHON SYNTAX FEATURES:")
print("="*25)

# 1. NO SEMICOLONS REQUIRED
print("Hello")
print("World")

# 2. MULTIPLE STATEMENTS ON ONE LINE (not recommended)
a = 1; b = 2; c = 3

# 3. LINE CONTINUATION
# Using backslash for long lines
long_string = "This is a very long string that " \
              "spans multiple lines using backslash"

# Using parentheses for line continuation (preferred)
result = (1 + 2 + 3 + 4 + 5 +
          6 + 7 + 8 + 9 + 10)

# 4. STATEMENT GROUPING
# Python uses indentation instead of braces
if True:
    print("This is inside the if block")
    print("This is also inside the if block")
print("This is outside the if block")

# 5. VARIABLES AND NAMING CONVENTIONS
# Variable names are case-sensitive
name = "Alice"
Name = "Bob"  # Different variable
AGE = 25

# Valid variable names
user_name = "john_doe"
userName = "johnDoe"  # camelCase (less common in Python)
_private_var = "private"
var2 = "second variable"

# 6. PYTHON KEYWORDS
# Reserved words that cannot be used as variable names
# Examples: if, else, elif, for, while, def, class, import, etc.

# COMMON SYNTAX PATTERNS
print("\nCOMMON SYNTAX PATTERNS:")
print("="*25)

# 1. CONDITIONAL STATEMENTS
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

print(f"Score: {score}, Grade: {grade}")

# 2. LOOPS
# For loop
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(f"I like {fruit}")

# While loop
count = 0
while count < 3:
    print(f"Count: {count}")
    count += 1

# 3. FUNCTIONS
def greet_user(name, greeting="Hello"):
    """
    Greets a user with a custom message.
    
    Args:
        name (str): The name of the user
        greeting (str): The greeting message (default: "Hello")
    
    Returns:
        str: The formatted greeting
    """
    return f"{greeting}, {name}!"

# Function call
message = greet_user("Alice")
print(message)

# 4. LIST COMPREHENSIONS
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
even_squares = [x**2 for x in numbers if x % 2 == 0]

print(f"Numbers: {numbers}")
print(f"Squares: {squares}")
print(f"Even squares: {even_squares}")

# INDENTATION BEST PRACTICES
print("\nINDENTATION BEST PRACTICES:")
print("="*30)

# 1. Use 4 spaces for indentation (PEP 8 standard)
# 2. Be consistent throughout your code
# 3. Configure your editor to show indentation
# 4. Use spaces, not tabs (or configure tab to insert spaces)

# Example of proper indentation hierarchy
def process_data(data):
    for item in data:
        if item > 0:
            print(f"Positive: {item}")
            if item > 100:
                print("Large number!")
        else:
            print(f"Non-positive: {item}")

# Test the function
test_data = [5, -2, 150, 0, 25]
process_data(test_data)

# SYNTAX ERROR EXAMPLES
print("\nCOMMON SYNTAX ERRORS:")
print("="*25)

# These would cause errors if uncommented:
# if True  # SyntaxError: invalid syntax (missing colon)
# print("Hello"  # SyntaxError: '(' was never closed
# if True:
# print("Wrong indentation")  # IndentationError

# COMMENT TYPES SUMMARY
print("\nCOMMENT TYPES SUMMARY:")
print("="*25)

# Single-line comment
x = 5  # Inline comment

"""
Multi-line string used as comment
(though technically not a comment)
"""

def documented_function():
    """This is a docstring - proper documentation"""
    pass

# TODO: This is a todo comment
# FIXME: This marks something that needs fixing
# NOTE: This is an important note

print("Python syntax, indentation, and comments covered!")

# CASE-SENSITIVITY IN PYTHON
print("\nCASE-SENSITIVITY IN PYTHON:")
print("="*30)

# Python is case-sensitive language
# This means that uppercase and lowercase letters are treated as different characters

# CASE-SENSITIVITY EXAMPLES
name = "Alice"
Name = "Bob"
NAME = "Charlie"

print(f"name: {name}")
print(f"Name: {Name}")
print(f"NAME: {NAME}")

# All three variables are different due to case-sensitivity
print(f"name == Name: {name == Name}")
print(f"name == NAME: {name == NAME}")

# Function names are also case-sensitive
def myFunction():
    return "lowercase function"

def MyFunction():
    return "capitalized function"

def MYFUNCTION():
    return "uppercase function"

print(f"myFunction(): {myFunction()}")
print(f"MyFunction(): {MyFunction()}")
print(f"MYFUNCTION(): {MYFUNCTION()}")

# Keywords are case-sensitive
# 'if' is a keyword, but 'If' and 'IF' are not
if True:
    print("This works because 'if' is lowercase")

# If = "This is a valid variable name"  # 'If' is not a keyword
# IF = "This is also valid"  # 'IF' is not a keyword

# VARIABLE NAMING RULES
print("\nVARIABLE NAMING RULES:")
print("="*25)

# 1. BASIC RULES
# - Must start with a letter (a-z, A-Z) or underscore (_)
# - Cannot start with a number
# - Can contain letters, numbers, and underscores
# - Cannot contain spaces or special characters
# - Cannot be a Python keyword

# Valid variable names
valid_name = "John"
_private_var = "private"
userName = "user123"
age2 = 25
my_variable_name = "long name"
PI = 3.14159
isValid = True
counter_1 = 0

print("Valid variable names created successfully")

# 2. INVALID VARIABLE NAMES (would cause SyntaxError)
# 2name = "invalid"        # Cannot start with number
# my-variable = "invalid"  # Cannot contain hyphen
# my variable = "invalid"  # Cannot contain space
# class = "invalid"        # Cannot use keywords
# @variable = "invalid"    # Cannot use special characters
# 123abc = "invalid"       # Cannot start with number

# 3. NAMING CONVENTIONS (PEP 8)
print("\nNAMING CONVENTIONS (PEP 8):")
print("="*30)

# Variables and functions: lowercase with underscores (snake_case)
first_name = "John"
last_name = "Doe"
user_age = 30

def calculate_total_price(base_price, tax_rate):
    return base_price * (1 + tax_rate)

# Constants: uppercase with underscores
MAX_SIZE = 100
PI_VALUE = 3.14159
DEFAULT_TIMEOUT = 30

# Classes: CapitalizedWords (PascalCase)
class StudentRecord:
    def __init__(self, name):
        self.name = name

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

# Private variables: single leading underscore
class MyClass:
    def __init__(self):
        self.public_var = "public"
        self._private_var = "private"
        self.__very_private = "very private"

# 4. DESCRIPTIVE NAMING
print("\nDESCRIPTIVE NAMING:")
print("="*20)

# Good: Descriptive names
student_count = 25
total_price = 199.99
is_logged_in = True
user_email = "user@example.com"

# Bad: Non-descriptive names
# n = 25
# tp = 199.99
# flag = True
# data = "user@example.com"

# 5. SPECIAL NAMING PATTERNS
print("\nSPECIAL NAMING PATTERNS:")
print("="*25)

# Single underscore prefix: internal use
_internal_variable = "internal"

# Double underscore prefix: name mangling
class Example:
    def __init__(self):
        self.__private_attribute = "private"

# Double underscore prefix and suffix: magic methods
class CustomClass:
    def __init__(self):
        self.value = 0
    
    def __str__(self):
        return f"CustomClass with value: {self.value}"
    
    def __len__(self):
        return self.value

# 6. CASE STYLE EXAMPLES
print("\nCASE STYLE EXAMPLES:")
print("="*22)

# snake_case (Python standard)
user_name = "john_doe"
total_amount = 100.50
is_active = True

# camelCase (less common in Python)
userName = "john_doe"
totalAmount = 100.50
isActive = True

# PascalCase (for classes)
class UserAccount:
    pass

class ShoppingCart:
    pass

# SCREAMING_SNAKE_CASE (for constants)
MAX_ATTEMPTS = 3
DEFAULT_ENCODING = "utf-8"
API_BASE_URL = "https://api.example.com"

# 7. KEYWORD CONFLICTS
print("\nKEYWORD CONFLICTS:")
print("="*20)

# Python keywords that cannot be used as variable names
print(f"Python keywords: {keyword.kwlist}")

# Avoiding keyword conflicts
# Use trailing underscore for variables that would conflict with keywords
class_ = "Python Programming"  # instead of 'class'
type_ = "integer"              # instead of 'type'
list_ = [1, 2, 3]             # instead of 'list'

# 8. VARIABLE NAMING EXAMPLES BY CONTEXT
print("\nVARIABLE NAMING BY CONTEXT:")
print("="*30)

# Boolean variables: use is_, has_, can_, should_
is_valid = True
has_permission = False
can_edit = True
should_save = False

# Counters and indices
item_count = 0
user_index = 1
page_number = 5

# Collections
student_list = ["Alice", "Bob", "Charlie"]
user_dict = {"name": "John", "age": 30}
grade_set = {85, 90, 78, 92}

# Functions: use verbs
def get_user_name():
    return "John"

def calculate_average(numbers):
    return sum(numbers) / len(numbers)

def validate_email(email):
    return "@" in email

# 9. COMMON NAMING MISTAKES
print("\nCOMMON NAMING MISTAKES:")
print("="*25)

# Avoid single character names (except for loops)
# Good
for index in range(10):
    print(f"Index: {index}")

# Acceptable for short loops
for i in range(5):
    for j in range(5):
        print(f"({i}, {j})")

# Avoid abbreviations
# Good
student_count = 25
# Bad: std_cnt = 25

# Avoid misleading names
# Good
user_list = ["Alice", "Bob"]
# Bad: user_string = ["Alice", "Bob"]  # It's actually a list

# 10. PRACTICAL EXAMPLES
print("\nPRACTICAL EXAMPLES:")
print("="*20)

# File processing
input_file_path = "data.txt"
output_file_path = "results.txt"
line_count = 0

# Database operations
user_id = 12345
connection_string = "localhost:5432"
query_result = []

# Mathematical calculations
circle_radius = 5.0
circle_area = PI_VALUE * circle_radius ** 2
rectangle_width = 10
rectangle_height = 20

# Web development
request_method = "GET"
response_status = 200
session_timeout = 3600

# print("Case-sensitivity and variable naming rules covered!")
# Python Language Fundamentals: Compilation, Interpretation, Syntax, and Naming Conventions
# This module provides comprehensive coverage of Python's fundamental concepts including:
# COMPILATION AND INTERPRETATION:
# - Detailed comparison between compiled and interpreted languages
# - Python's hybrid approach: source code → bytecode → interpretation
# - Performance implications and trade-offs
# - Modern compiler optimizations and JIT compilation
# SYNTAX AND STRUCTURE:
# - Python's clean, readable syntax emphasizing indentation-based code blocks
# - Proper indentation practices (4 spaces, PEP 8 compliance)
# - Comment types: single-line (#), multi-line (multiple #), and docstrings (""")
# - Statement grouping and line continuation techniques
# VARIABLE NAMING AND CASE SENSITIVITY:
# - Python's case-sensitive nature with practical examples
# - Comprehensive variable naming rules and restrictions
# - PEP 8 naming conventions:
#     * snake_case for variables and functions
#     * PascalCase for classes
#     * SCREAMING_SNAKE_CASE for constants
#     * _private_var for internal use
#     * __name_mangling for class attributes
# BEST PRACTICES:
# - Descriptive variable naming over abbreviations
# - Proper use of boolean variable prefixes (is_, has_, can_, should_)
# - Avoiding Python keyword conflicts with trailing underscores
# - Context-appropriate naming for collections, functions, and data types
# PRACTICAL EXAMPLES:
# - Memory management and performance measurement
# - File operations and exception handling
# - Object-oriented programming demonstrations
# - Lambda functions and list comprehensions
# - Bytecode inspection and debugging techniques
# DEVELOPMENT INSIGHTS:
# - Evolution from clear compiler/interpreter divide to modern hybrid approaches
# - Performance characteristics of different execution models
# - Development environment considerations (IDE, debugging tools)
# - Cross-platform compatibility and deployment strategies
# This module serves as a foundational reference for understanding Python's execution model,
# proper coding practices, and professional development standards.
# Author: Educational Resource
# Purpose: Comprehensive Python fundamentals tutorial
# Audience: Beginner to intermediate Python developers

# FUNCTIONS IN PYTHON
print("\n" + "="*60)
print("FUNCTIONS IN PYTHON - COMPREHENSIVE GUIDE")
print("="*60)

# FUNCTION DEFINITION AND SYNTAX
print("\nFUNCTION DEFINITION AND SYNTAX:")
print("="*35)

# Basic function syntax
def function_name(parameters):
    """
    Optional docstring
    """
    # Function body
    # return value  # Optional return statement

# Simple function example
def greet():
    """Simple function with no parameters"""
    return "Hello, World!"

result = greet()
print(f"Simple function result: {result}")

# Function with parameters
def greet_person(name):
    """Function with single parameter"""
    return f"Hello, {name}!"

greeting = greet_person("Alice")
print(f"Parameterized function: {greeting}")

# Function with multiple parameters
def calculate_rectangle_area(length, width):
    """Function with multiple parameters"""
    area = length * width
    return area

area = calculate_rectangle_area(10, 5)
print(f"Rectangle area: {area}")

# FUNCTION PARAMETERS AND ARGUMENTS
print("\nFUNCTION PARAMETERS AND ARGUMENTS:")
print("="*38)

# 1. DEFAULT PARAMETERS
def greet_with_title(name, title="Mr."):
    """Function with default parameter"""
    return f"Hello, {title} {name}!"

print(greet_with_title("Smith"))           # Uses default title
print(greet_with_title("Johnson", "Dr."))  # Overrides default title

# 2. KEYWORD ARGUMENTS
def create_profile(name, age, city="Unknown", country="Unknown"):
    """Function demonstrating keyword arguments"""
    return f"Name: {name}, Age: {age}, City: {city}, Country: {country}"

# Positional arguments
print(create_profile("John", 30))

# Mixed positional and keyword arguments
print(create_profile("Jane", 25, city="New York"))

# All keyword arguments
print(create_profile(name="Bob", age=35, city="London", country="UK"))

# 3. VARIABLE-LENGTH ARGUMENTS (*args)
def sum_numbers(*args):
    """Function accepting variable number of arguments"""
    total = 0
    for num in args:
        total += num
    return total

print(f"Sum of 1, 2, 3: {sum_numbers(1, 2, 3)}")
print(f"Sum of 1, 2, 3, 4, 5: {sum_numbers(1, 2, 3, 4, 5)}")

# 4. KEYWORD VARIABLE-LENGTH ARGUMENTS (**kwargs)
def create_user(**kwargs):
    """Function accepting variable keyword arguments"""
    user_info = "User Information:\n"
    for key, value in kwargs.items():
        user_info += f"  {key}: {value}\n"
    return user_info

print(create_user(name="Alice", age=28, email="alice@example.com"))
print(create_user(name="Bob", city="Paris", occupation="Engineer"))

# 5. COMBINING DIFFERENT PARAMETER TYPES
def complex_function(required_param, default_param="default", *args, **kwargs):
    """Function combining all parameter types"""
    result = f"Required: {required_param}\n"
    result += f"Default: {default_param}\n"
    result += f"Args: {args}\n"
    result += f"Kwargs: {kwargs}\n"
    return result

print(complex_function("value1", "value2", "extra1", "extra2", key1="val1", key2="val2"))

# FUNCTION RETURN VALUES
print("\nFUNCTION RETURN VALUES:")
print("="*25)

# 1. SINGLE RETURN VALUE
def square(number):
    """Returns single value"""
    return number ** 2

print(f"Square of 5: {square(5)}")

# 2. MULTIPLE RETURN VALUES
def get_name_parts(full_name):
    """Returns multiple values as tuple"""
    parts = full_name.split()
    first_name = parts[0]
    last_name = parts[-1]
    return first_name, last_name

first, last = get_name_parts("John Doe Smith")
print(f"First: {first}, Last: {last}")

# 3. RETURN DIFFERENT DATA TYPES
def analyze_number(num):
    """Returns dictionary with number analysis"""
    return {
        'value': num,
        'is_positive': num > 0,
        'is_even': num % 2 == 0,
        'absolute': abs(num)
    }

analysis = analyze_number(-6)
print(f"Number analysis: {analysis}")

# 4. EARLY RETURN
def validate_age(age):
    """Function with early return"""
    if age < 0:
        return "Invalid age: cannot be negative"
    if age > 150:
        return "Invalid age: too old"
    if age < 18:
        return "Minor"
    return "Adult"

print(f"Age validation: {validate_age(25)}")
print(f"Age validation: {validate_age(-5)}")

# FUNCTION SCOPE AND VARIABLES
print("\nFUNCTION SCOPE AND VARIABLES:")
print("="*33)

# Global variable
global_var = "I am global"

def scope_demo():
    """Demonstrates variable scope"""
    local_var = "I am local"
    print(f"Inside function - Global: {global_var}")
    print(f"Inside function - Local: {local_var}")

scope_demo()
print(f"Outside function - Global: {global_var}")
# print(f"Outside function - Local: {local_var}")  # This would cause NameError

# Global keyword
counter = 0

def increment_counter():
    """Modifies global variable"""
    global counter
    counter += 1
    return counter

print(f"Counter before: {counter}")
increment_counter()
print(f"Counter after: {counter}")

# Nonlocal keyword
def outer_function():
    """Demonstrates nonlocal keyword"""
    outer_var = "outer"
    
    def inner_function():
        nonlocal outer_var
        outer_var = "modified by inner"
        return outer_var
    
    print(f"Before inner call: {outer_var}")
    result = inner_function()
    print(f"After inner call: {outer_var}")
    return result

outer_function()

# LAMBDA FUNCTIONS
print("\nLAMBDA FUNCTIONS:")
print("="*18)

# Basic lambda function
square_lambda = lambda x: x ** 2
print(f"Lambda square of 4: {square_lambda(4)}")

# Lambda with multiple parameters
add_lambda = lambda x, y: x + y
print(f"Lambda addition: {add_lambda(3, 5)}")

# Lambda with conditional
max_lambda = lambda x, y: x if x > y else y
print(f"Lambda max: {max_lambda(10, 7)}")

# Using lambda with built-in functions
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {evens}")

# Map squares
squares = list(map(lambda x: x ** 2, numbers))
print(f"Squares: {squares}")

# Sort by custom criteria
students = [('Alice', 85), ('Bob', 90), ('Charlie', 78)]
students_sorted = sorted(students, key=lambda x: x[1], reverse=True)
print(f"Students sorted by grade: {students_sorted}")

# HIGHER-ORDER FUNCTIONS
print("\nHIGHER-ORDER FUNCTIONS:")
print("="*25)

# Function as parameter
def apply_operation(numbers, operation):
    """Higher-order function that applies operation to numbers"""
    return [operation(num) for num in numbers]

def double(x):
    return x * 2

def triple(x):
    return x * 3

numbers = [1, 2, 3, 4, 5]
print(f"Original: {numbers}")
print(f"Doubled: {apply_operation(numbers, double)}")
print(f"Tripled: {apply_operation(numbers, triple)}")

# Function returning function
def create_multiplier(factor):
    """Returns a function that multiplies by factor"""
    def multiplier(x):
        return x * factor
    return multiplier

multiply_by_3 = create_multiplier(3)
multiply_by_5 = create_multiplier(5)

print(f"3 * 4 = {multiply_by_3(4)}")
print(f"5 * 4 = {multiply_by_5(4)}")

# RECURSIVE FUNCTIONS
print("\nRECURSIVE FUNCTIONS:")
print("="*20)

# Factorial calculation
def factorial(n):
    """Calculates factorial using recursion"""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(f"Factorial of 5: {factorial(5)}")

# CLASSES AND CASE SENSITIVITY IN PYTHON
print("\nCLASSES AND CASE SENSITIVITY IN PYTHON:")
print("="*42)

# CLASS DEFINITION AND NAMING CONVENTIONS
print("\nCLASS DEFINITION AND NAMING CONVENTIONS:")
print("="*42)

# 1. BASIC CLASS DEFINITION
# Class names should use PascalCase (CapitalizedWords)
class Student:
    """A class representing a student"""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old"

# Creating instances
student1 = Student("Alice", 20)
student2 = Student("Bob", 22)

print(f"Student 1: {student1.introduce()}")
print(f"Student 2: {student2.introduce()}")

# 2. CLASS NAMING CASE SENSITIVITY
# Each of these is a different class due to case sensitivity
class Person:
    def __init__(self, name):
        self.name = name
        self.type = "Person"

class person:  # Different class (lowercase)
    def __init__(self, name):
        self.name = name
        self.type = "person (lowercase)"

class PERSON:  # Different class (uppercase)
    def __init__(self, name):
        self.name = name
        self.type = "PERSON (uppercase)"

# Creating instances of different classes
person1 = Person("John")
person2 = person("Jane")
person3 = PERSON("Jack")

print(f"Person class: {person1.type}")
print(f"person class: {person2.type}")
print(f"PERSON class: {person3.type}")

# 3. ATTRIBUTE CASE SENSITIVITY
class CaseSensitiveExample:
    def __init__(self):
        self.name = "lowercase attribute"
        self.Name = "capitalized attribute"
        self.NAME = "uppercase attribute"
        self._private = "private attribute"
        self.__very_private = "name-mangled attribute"

example = CaseSensitiveExample()
print(f"name: {example.name}")
print(f"Name: {example.Name}")
print(f"NAME: {example.NAME}")
print(f"_private: {example._private}")

# 4. METHOD CASE SENSITIVITY
class MethodExample:
    def getName(self):
        return "camelCase method"
    
    def get_name(self):
        return "snake_case method"
    
    def GETNAME(self):
        return "UPPERCASE method"

method_obj = MethodExample()
print(f"getName(): {method_obj.getName()}")
print(f"get_name(): {method_obj.get_name()}")
print(f"GETNAME(): {method_obj.GETNAME()}")

# 5. PROPER CLASS NAMING (PEP 8)
class BankAccount:
    """Proper class name using PascalCase"""
    
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False
    
    def get_balance(self):
        return self.balance

# Example usage
account = BankAccount("12345", 1000)
account.deposit(500)
account.withdraw(200)
print(f"Account balance: ${account.get_balance()}")

# 6. INHERITANCE AND CASE SENSITIVITY
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# Different case would create different classes
class animal:  # Different from Animal
    def __init__(self, name):
        self.name = name
        self.species = "generic animal"

dog = Dog("Buddy")
cat = Cat("Whiskers")
generic_animal = animal("Generic")

print(f"Dog: {dog.speak()}")
print(f"Cat: {cat.speak()}")
print(f"Generic: {generic_animal.species}")

# 7. CLASS VARIABLES VS INSTANCE VARIABLES
class Counter:
    # Class variable (shared by all instances)
    total_count = 0
    
    def __init__(self, name):
        self.name = name  # Instance variable
        Counter.total_count += 1  # Access class variable
    
    def get_count(self):
        return Counter.total_count

counter1 = Counter("First")
counter2 = Counter("Second")
counter3 = Counter("Third")

print(f"Total counters created: {Counter.total_count}")
print(f"Counter1 sees: {counter1.get_count()}")
print(f"Counter2 sees: {counter2.get_count()}")

# 8. PRIVATE AND PROTECTED ATTRIBUTES
class PrivacyExample:
    def __init__(self):
        self.public = "Everyone can access"
        self._protected = "Convention: internal use"
        self.__private = "Name mangling applied"
    
    def get_private(self):
        return self.__private
    
    def _internal_method(self):
        return "Internal method"

privacy_obj = PrivacyExample()
print(f"Public: {privacy_obj.public}")
print(f"Protected: {privacy_obj._protected}")
print(f"Private (through method): {privacy_obj.get_private()}")
# print(f"Private direct: {privacy_obj.__private}")  # This would cause AttributeError

# 9. STATIC METHODS AND CLASS METHODS
class MathUtils:
    PI = 3.14159
    
    @staticmethod
    def add(a, b):
        """Static method - doesn't access class or instance"""
        return a + b
    
    @classmethod
    def get_pi(cls):
        """Class method - accesses class attributes"""
        return cls.PI
    
    def instance_method(self):
        """Instance method - accesses instance attributes"""
        return "Instance method called"

# Static method can be called without creating instance
print(f"Static method: {MathUtils.add(5, 3)}")
print(f"Class method: {MathUtils.get_pi()}")

# Instance method requires object
math_obj = MathUtils()
print(f"Instance method: {math_obj.instance_method()}")

# 10. PROPERTY DECORATORS
class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius
    
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = (value - 32) * 5/9

temp = Temperature(25)
print(f"Temperature: {temp.celsius}°C = {temp.fahrenheit}°F")

temp.fahrenheit = 100
print(f"After setting Fahrenheit: {temp.celsius}°C = {temp.fahrenheit}°F")

# 11. SPECIAL METHODS (MAGIC METHODS)
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        return f"'{self.title}' by {self.author}"
    
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.pages})"
    
    def __len__(self):
        return self.pages
    
    def __eq__(self, other):
        if isinstance(other, Book):
            return self.title == other.title and self.author == other.author
        return False

book1 = Book("1984", "George Orwell", 328)
book2 = Book("Animal Farm", "George Orwell", 112)

print(f"Book string: {str(book1)}")
print(f"Book repr: {repr(book1)}")
print(f"Book length: {len(book1)} pages")
print(f"Books equal: {book1 == book2}")

# 12. CASE SENSITIVITY IN ATTRIBUTE ACCESS
class AttributeExample:
    def __init__(self):
        self.data = "lowercase"
        self.Data = "capitalized"
        self.DATA = "uppercase"

attr_obj = AttributeExample()

# All these access different attributes
print(f"attr_obj.data: {attr_obj.data}")
print(f"attr_obj.Data: {attr_obj.Data}")
print(f"attr_obj.DATA: {attr_obj.DATA}")

# Dynamic attribute access is also case-sensitive
print(f"getattr(attr_obj, 'data'): {getattr(attr_obj, 'data')}")
print(f"getattr(attr_obj, 'Data'): {getattr(attr_obj, 'Data')}")

# 13. INHERITANCE HIERARCHY EXAMPLE
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def start(self):
        return f"{self.brand} {self.model} is starting"

class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)
        self.doors = doors
    
    def drive(self):
        return f"Driving the {self.brand} {self.model}"

class ElectricCar(Car):
    def __init__(self, brand, model, doors, battery_capacity):
        super().__init__(brand, model, doors)
        self.battery_capacity = battery_capacity
    
    def charge(self):
        return f"Charging the {self.brand} {self.model}"

# Creating instances
tesla = ElectricCar("Tesla", "Model 3", 4, "75kWh")
print(f"Electric car: {tesla.start()}")
print(f"Electric car: {tesla.drive()}")
print(f"Electric car: {tesla.charge()}")

# 14. MULTIPLE INHERITANCE
class Flyable:
    def fly(self):
        return "Flying through the air"

class Swimmable:
    def swim(self):
        return "Swimming in water"

class Duck(Animal, Flyable, Swimmable):
    def __init__(self, name):
        Animal.__init__(self, name)
    
    def speak(self):
        return f"{self.name} says Quack!"

duck = Duck("Donald")
print(f"Duck: {duck.speak()}")
print(f"Duck: {duck.fly()}")
print(f"Duck: {duck.swim()}")

print("\nCLASS NAMING BEST PRACTICES:")
print("="*32)
print("✓ Use PascalCase for class names (MyClass)")
print("✓ Use snake_case for method and attribute names (my_method)")
print("✓ Use SCREAMING_SNAKE_CASE for constants (MAX_SIZE)")
print("✓ Use single underscore for protected attributes (_protected)")
print("✓ Use double underscore for private attributes (__private)")
print("✓ Remember Python is case-sensitive - Name ≠ name ≠ NAME")

# INDENTATION NOTES AND EXAMPLES
print("\n" + "="*60)
print("INDENTATION: RIGHT vs WRONG EXAMPLES")
print("="*60)

# RIGHT INDENTATION EXAMPLES
print("\nRIGHT INDENTATION EXAMPLES:")
print("="*30)

# Correct if-else indentation (4 spaces)
age = 20
if age >= 18:  # Correct: if statement at base level
    print("You are an adult")  # Correct: 4 spaces indentation
    if age >= 65:  # Correct: nested if with same indentation as parent block
        print("You are a senior citizen")  # Correct: 8 spaces for nested block
    else:  # Correct: else aligned with corresponding if
        print("You are not a senior citizen")  # Correct: 8 spaces indentation
else:  # Correct: else aligned with original if
    print("You are a minor")  # Correct: 4 spaces indentation

# Correct function indentation
def calculate_grade(score):  # Correct: function definition at base level
    """Calculate letter grade based on score"""  # Correct: docstring with 4 spaces
    if score >= 90:  # Correct: 4 spaces indentation
        return "A"  # Correct: 8 spaces for nested block
    elif score >= 80:  # Correct: elif aligned with if
        return "B"  # Correct: 8 spaces indentation
    elif score >= 70:  # Correct: elif aligned with if
        return "C"  # Correct: 8 spaces indentation
    else:  # Correct: else aligned with if
        return "F"  # Correct: 8 spaces indentation

# Correct loop indentation
for i in range(5):  # Correct: for loop at base level
    print(f"Iteration {i}")  # Correct: 4 spaces indentation
    if i % 2 == 0:  # Correct: nested if with 4 spaces
        print("Even number")  # Correct: 8 spaces for nested block
    else:  # Correct: else aligned with if
        print("Odd number")  # Correct: 8 spaces indentation

# Correct class indentation
class RightIndentationExample:  # Correct: class definition at base level
    """Example class with proper indentation"""  # Correct: docstring with 4 spaces
    
    def __init__(self, name):  # Correct: method with 4 spaces indentation
        self.name = name  # Correct: 8 spaces for method body
    
    def greet(self):  # Correct: method with 4 spaces indentation
        if self.name:  # Correct: if statement with 8 spaces
            return f"Hello, {self.name}!"  # Correct: 12 spaces for nested block
        else:  # Correct: else aligned with if
            return "Hello, stranger!"  # Correct: 12 spaces indentation

# WRONG INDENTATION EXAMPLES (COMMENTED TO AVOID ERRORS)
print("\nWRONG INDENTATION EXAMPLES (COMMENTED):")
print("="*45)

# Wrong indentation examples (commented out to prevent errors)
print("# WRONG: Inconsistent indentation")
print("# if True:")
print("#   print('2 spaces')  # Wrong: should be 4 spaces")
print("#     print('4 spaces')  # Wrong: inconsistent with parent")

print("\n# WRONG: Missing indentation")
print("# if True:")
print("# print('No indentation')  # Wrong: IndentationError")

print("\n# WRONG: Unnecessary indentation")
print("#     print('Indented for no reason')  # Wrong: unexpected indent")

print("\n# WRONG: Function with wrong indentation")
print("# def my_function():")
print("#   return 'value'  # Wrong: should be 4 spaces, not 2")

print("\n# WRONG: Class with inconsistent indentation")
print("# class MyClass:")
print("#   def __init__(self):")
print("#     pass  # Wrong: should be 8 spaces, not 6")

print("\n# WRONG: Mixed tabs and spaces")
print("# if True:")
print("#     print('spaces')  # 4 spaces")
print("# 	print('tab')      # 1 tab - causes IndentationError")

# INDENTATION BEST PRACTICES
print("\nINDENTATION BEST PRACTICES:")
print("="*30)
print("✓ Use 4 spaces for each indentation level (PEP 8)")
print("✓ Never mix tabs and spaces")
print("✓ Be consistent throughout your code")
print("✓ Configure your editor to show whitespace")
print("✓ Use spaces, not tabs (or configure tabs to insert spaces)")
print("✓ Align continuation lines properly")
print("✓ Use hanging indents for long function calls")

# COMMON INDENTATION ERRORS
print("\nCOMMON INDENTATION ERRORS:")
print("="*30)
print("• IndentationError: expected an indented block")
print("• IndentationError: unindent does not match any outer indentation level")
print("• IndentationError: unexpected indent")
print("• TabError: inconsistent use of tabs and spaces in indentation")

# INDENTATION IN DIFFERENT CONTEXTS
print("\nINDENTATION IN DIFFERENT CONTEXTS:")
print("="*35)

# Multi-line statements with proper indentation
long_variable_name = (
    "This is a very long string that needs to be broken " +
    "across multiple lines for better readability"
)

# Function with multiple parameters
def function_with_many_parameters(
    parameter1,
    parameter2,
    parameter3,
    parameter4
):
    """Function with proper parameter indentation"""
    return parameter1 + parameter2 + parameter3 + parameter4

# Dictionary with proper indentation
student_data = {
    'name': 'John Doe',
    'age': 20,
    'grades': {
        'math': 85,
        'science': 92,
        'english': 78
    },
    'active': True
}

# List with proper indentation
long_list = [
    'item1',
    'item2',
    'item3',
    'item4',
    'item5'
]

print("All indentation examples completed successfully!")

# WHY INDENTATION IN PYTHON?
print("\n" + "="*60)
print("WHY INDENTATION IN PYTHON? - DETAILED EXPLANATION")
print("="*60)

# 1. READABILITY AND VISUAL STRUCTURE
print("\n1. READABILITY AND VISUAL STRUCTURE:")
print("="*40)
print("Python uses indentation to make code more readable and visually structured")
print("Unlike languages that use braces {}, Python's indentation makes the code hierarchy clear")

# Example showing visual hierarchy
def demonstrate_hierarchy():
    """Shows how indentation creates visual hierarchy"""
    print("Function level")
    
    if True:
        print("    If block level")
        
        for i in range(2):
            print("        Loop level")
            
            if i == 1:
                print("            Nested if level")

demonstrate_hierarchy()

# 2. ENFORCED CODE STRUCTURE
print("\n2. ENFORCED CODE STRUCTURE:")
print("="*32)
print("Indentation forces developers to write properly structured code")
print("This prevents common errors like mismatched braces or blocks")

# Example showing enforced structure
def proper_structure_example():
    """Demonstrates enforced structure"""
    numbers = [1, 2, 3, 4, 5]
    
    for number in numbers:
        if number % 2 == 0:
            print(f"{number} is even")
        else:
            print(f"{number} is odd")
    
    print("Loop completed")

proper_structure_example()

# 3. REDUCED SYNTAX CLUTTER
print("\n3. REDUCED SYNTAX CLUTTER:")
print("="*30)
print("No need for braces {} or semicolons ;")
print("Cleaner, more readable code")

# Compare with other languages (conceptually)
print("\n# What Python looks like:")
print("if condition:")
print("    do_something()")
print("    do_another_thing()")

print("\n# What C-style languages look like:")
print("if (condition) {")
print("    do_something();")
print("    do_another_thing();")
print("}")

# 4. CONSISTENCY ACROSS TEAMS
print("\n4. CONSISTENCY ACROSS TEAMS:")
print("="*32)
print("Indentation rules force consistent formatting across different developers")
print("Everyone's code looks similar, improving maintainability")

# Example of consistent formatting
class ConsistentExample:
    """All Python code follows the same indentation pattern"""
    
    def __init__(self, name):
        self.name = name
    
    def process_data(self, data):
        results = []
        
        for item in data:
            if self.validate_item(item):
                processed = self.transform_item(item)
                results.append(processed)
        
        return results
    
    def validate_item(self, item):
        return item is not None and len(str(item)) > 0
    
    def transform_item(self, item):
        return str(item).upper()

# 5. PYTHON'S PHILOSOPHY
print("\n5. PYTHON'S PHILOSOPHY:")
print("="*25)
print("Python follows 'The Zen of Python' principles:")
print("- Beautiful is better than ugly")
print("- Simple is better than complex")
print("- Readability counts")
print("Indentation supports these principles")

# Import this to see the full Zen of Python

# 6. USE CASES FOR INDENTATION
print("\n6. USE CASES FOR INDENTATION:")
print("="*32)

# Use Case 1: Control Flow Structures
print("\nUse Case 1: Control Flow Structures")
print("-" * 35)

def grade_evaluation(score):
    """Demonstrates indentation in control flow"""
    if score >= 90:
        grade = "A"
        print(f"Excellent work! Grade: {grade}")
        if score >= 95:
            print("Outstanding performance!")
    elif score >= 80:
        grade = "B"
        print(f"Good work! Grade: {grade}")
    elif score >= 70:
        grade = "C"
        print(f"Satisfactory. Grade: {grade}")
    else:
        grade = "F"
        print(f"Needs improvement. Grade: {grade}")
    
    return grade

# Test the function
test_scores = [95, 85, 75, 65]
for score in test_scores:
    print(f"Score {score}: {grade_evaluation(score)}")

# Use Case 2: Function Definitions
print("\nUse Case 2: Function Definitions")
print("-" * 32)

def calculate_compound_interest(principal, rate, time, n=1):
    """
    Calculate compound interest
    Shows proper indentation in function body
    """
    # Formula: A = P(1 + r/n)^(nt)
    amount = principal * (1 + rate/n) ** (n * time)
    interest = amount - principal
    
    print(f"Principal: ${principal}")
    print(f"Rate: {rate*100}%")
    print(f"Time: {time} years")
    print(f"Compound frequency: {n} times per year")
    print(f"Final amount: ${amount:.2f}")
    print(f"Interest earned: ${interest:.2f}")
    
    return amount, interest

# Test compound interest calculation
amount, interest = calculate_compound_interest(1000, 0.05, 3, 12)

# Use Case 3: Class Definitions
print("\nUse Case 3: Class Definitions")
print("-" * 30)

class BankAccount:
    """Demonstrates indentation in class definition"""
    
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance
        self.transaction_history = []
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited: ${amount}")
            print(f"Deposited ${amount}. New balance: ${self.balance}")
            return True
        else:
            print("Invalid deposit amount")
            return False
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew: ${amount}")
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
            return True
        else:
            print("Invalid withdrawal amount or insufficient funds")
            return False
    
    def get_statement(self):
        print(f"\nAccount Statement for {self.account_holder}")
        print("-" * 40)
        print(f"Current Balance: ${self.balance}")
        print("Transaction History:")
        
        for transaction in self.transaction_history:
            print(f"  {transaction}")
        
        if not self.transaction_history:
            print("  No transactions yet")

# Test the bank account
account = BankAccount("John Doe", 1000)
account.deposit(500)
account.withdraw(200)
account.get_statement()

# Use Case 4: Exception Handling
print("\nUse Case 4: Exception Handling")
print("-" * 31)

def safe_division(a, b):
    """Demonstrates indentation in exception handling"""
    try:
        result = a / b
        print(f"Division successful: {a} / {b} = {result}")
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
        return None
    except TypeError:
        print("Error: Invalid data types for division")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None
    finally:
        print("Division operation completed")

# Test exception handling
test_cases = [(10, 2), (10, 0), (10, "invalid"), (10, 5)]
for a, b in test_cases:
    print(f"\nTesting {a} / {b}:")
    safe_division(a, b)

# Use Case 5: List Comprehensions and Generators
print("\nUse Case 5: List Comprehensions and Generators")
print("-" * 44)

def demonstrate_comprehensions():
    """Shows indentation in complex comprehensions"""
    numbers = range(1, 11)
    
    # Multi-line list comprehension
    squares_of_evens = [
        x**2 
        for x in numbers 
        if x % 2 == 0
    ]
    
    # Multi-line dictionary comprehension
    number_properties = {
        x: {
            'square': x**2,
            'cube': x**3,
            'is_even': x % 2 == 0
        }
        for x in numbers
        if x <= 5
    }
    
    print(f"Squares of even numbers: {squares_of_evens}")
    print(f"Number properties: {number_properties}")

demonstrate_comprehensions()

# Use Case 6: Context Managers
print("\nUse Case 6: Context Managers")
print("-" * 28)

def file_processing_example():
    """Demonstrates indentation with context managers"""
    filename = "example_data.txt"
    
    # Writing to file
    try:
        with open(filename, 'w') as file:
            file.write("Line 1: Hello World\n")
            file.write("Line 2: Python Programming\n")
            file.write("Line 3: Indentation is important\n")
            
            for i in range(3):
                file.write(f"Line {i+4}: Generated line {i+1}\n")
        
        print(f"Successfully wrote to {filename}")
    except IOError as e:
        print(f"Error writing to file: {e}")
    
    # Reading from file
    try:
        with open(filename, 'r') as file:
            print(f"\nContents of {filename}:")
            print("-" * 30)
            
            for line_number, line in enumerate(file, 1):
                if line_number <= 3:
                    print(f"Important: {line.strip()}")
                else:
                    print(f"Generated: {line.strip()}")
    except IOError as e:
        print(f"Error reading file: {e}")

file_processing_example()

# Use Case 7: Decorators
print("\nUse Case 7: Decorators")
print("-" * 20)

def timing_decorator(func):
    """Decorator showing proper indentation"""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        
        try:
            result = func(*args, **kwargs)
            end_time = time.time()
            print(f"Function {func.__name__} took {end_time - start_time:.4f} seconds")
            return result
        except Exception as e:
            print(f"Error in {func.__name__}: {e}")
            raise
    
    return wrapper

@timing_decorator
def complex_calculation(n):
    """Function with decorator showing indentation"""
    total = 0
    for i in range(n):
        for j in range(i):
            total += i * j
    return total

# Test decorated function
result = complex_calculation(100)
print(f"Calculation result: {result}")

# 7. INDENTATION BENEFITS SUMMARY
print("\n7. INDENTATION BENEFITS SUMMARY:")
print("="*35)
print("✓ Forces consistent code structure")
print("✓ Improves code readability")
print("✓ Reduces syntax clutter")
print("✓ Prevents common formatting errors")
print("✓ Makes code hierarchy visually clear")
print("✓ Enforces team coding standards")
print("✓ Aligns with Python's philosophy")
print("✓ Eliminates debates about brace placement")

# 8. COMMON INDENTATION PATTERNS
print("\n8. COMMON INDENTATION PATTERNS:")
print("="*34)

# Pattern 1: Nested conditions
def nested_conditions_example(user_type, age, has_license):
    """Shows proper indentation for nested conditions"""
    if user_type == "driver":
        if age >= 16:
            if has_license:
                print("Can drive")
            else:
                print("Need license")
        else:
            print("Too young to drive")
    elif user_type == "passenger":
        print("Can be a passenger")
    else:
        print("Unknown user type")

# Pattern 2: Multiple loops
def multiple_loops_example():
    """Shows proper indentation for multiple loops"""
    matrix = []
    
    for i in range(3):
        row = []
        for j in range(3):
            value = i * 3 + j + 1
            row.append(value)
        matrix.append(row)
    
    print("Generated matrix:")
    for row in matrix:
        for value in row:
            print(f"{value:2d}", end=" ")
        print()  # New line after each row

multiple_loops_example()

# Pattern 3: Complex data structures
def complex_data_structure():
    """Shows indentation with complex data structures"""
    company_data = {
        'departments': {
            'engineering': {
                'employees': [
                    {'name': 'Alice', 'role': 'Senior Developer'},
                    {'name': 'Bob', 'role': 'Junior Developer'}
                ],
                'budget': 500000
            },
            'marketing': {
                'employees': [
                    {'name': 'Charlie', 'role': 'Marketing Manager'},
                    {'name': 'Diana', 'role': 'Content Creator'}
                ],
                'budget': 300000
            }
        }
    }
    
    # Process the data with proper indentation
    for dept_name, dept_info in company_data['departments'].items():
        print(f"\nDepartment: {dept_name.title()}")
        print(f"Budget: ${dept_info['budget']:,}")
        print("Employees:")
        
        for employee in dept_info['employees']:
            print(f"  - {employee['name']}: {employee['role']}")

complex_data_structure()

print("\n" + "="*60)
print("INDENTATION: THE FOUNDATION OF PYTHON'S ELEGANCE")
print("="*60)
print("Indentation in Python is not just a style choice - it's a fundamental")
print("part of the language that promotes clean, readable, and maintainable code.")
print("It enforces good programming practices and makes Python code universally")
print("recognizable and consistent across different developers and projects.")
print("="*60)

# REPL: Read Evaluate Print Loop
print("\nREPL: Read Evaluate Print Loop\n")
# Programming environment that allows user to  input code , evaluate this and see the results in real-time.
# Basic REPL is a useful tool for developers for testing , debugging and experimenting and learning code.
# REPL is popular  in languages like Javascript, Python and Ruby. This are useful for both beginners and experienced developers.
# Reads your input , Evaluate this, Prints the result , and waits for the next input i.e. does the same thing in the loop.
# This is ideal for quick test , debugging and for learning interactively.
# Open the terminal and type `python` or `python3` to start the REPL.
# REPL prompt will come (>>>) appears, indicating that this is ready for interacting input command.
# To exit the REPL , type exit() or quit() or press Ctrl + D (on Linux) or Ctrl + Z (on Windows).
# company_data is a dictionary containing department information.
# Each department (like 'engineering' or 'marketing') has its own dictionary with a list of employees and a budget.
# The function loops through each department, printing its name, budget, and a list of employees with their roles.
# Key points:

# Indentation is crucial for readability, especially with nested loops and data structures.
# The use of .title() and formatted strings (f"...") makes the output user-friendly.
# This function, when called, will print a nicely formatted summary of each department and its employees.
# Example output:

# Gotcha:
# If you forget to call the function (complex_data_structure()), nothing will be printed. Also, be careful with indentation—Python relies on it to define code blocks.

# Let me know if you want to see how to call this function or modify the data!



# INTERNAL STRUCTURE AND WORKING OF REPL

print("\nINTERNAL STRUCTURE AND WORKING OF REPL:")
print("="*45)

# The REPL (Read-Eval-Print Loop) is an interactive programming environment.
# It allows users to enter code, which is then executed immediately, and the result is displayed.

# The internal workflow of a REPL consists of the following steps:

# 1. READ:
#    - The REPL waits for user input.
#    - It reads a line or block of code entered by the user.

# 2. EVALUATE:
#    - The input code is parsed and compiled into bytecode.
#    - The Python interpreter evaluates (executes) the code.
#    - If the input is an expression, its value is computed.
#    - If the input is a statement (like assignment or function definition), it is executed.

# 3. PRINT:
#    - The result of the evaluation (if any) is printed to the screen.
#    - For expressions, the result is shown.
#    - For statements, nothing is printed unless there is output.

# 4. LOOP:
#    - The REPL returns to the prompt and waits for the next input.
#    - This cycle continues until the user exits.

# Example of a REPL loop (conceptual pseudocode):
# while True:
#     try:
#         user_input = input(">>> ")
#         result = eval(user_input)
#         if result is not None:
#             print(result)
#     except Exception as e:
#         print(f"Error: {e}")

# In reality, the Python REPL is more sophisticated:
# - It distinguishes between expressions and statements.
# - It maintains an execution environment (namespace) across commands.
# - It handles multi-line input (e.g., function definitions, loops).
# - It provides helpful error messages and supports features like tab completion.

# The REPL is implemented in Python's interactive shell (code module) and is also used in tools like IPython and Jupyter.

print("REPL enables interactive programming by reading, evaluating, and printing results in a continuous loop.")

# Variables in Python
# A variable is a symbolic name for a memory location where data is stored.
#       e.g.: CSE_marks = 95
#             DA_marks =  88
# To keep the memory address handy , we require a variable (give this a name) to represent the memory location where the data is stored.
# Variable is actually synonymous to the name given as a reference to the memory location.
#       e.g.: CSE_marks = 95
#             DA marks =  88
# Like in this example the value 95 is assigned to the variable named "CSE_marks" where "CSE_marks" represents the reference to a certain memory address
#  for example:" 0x7f8c3c2d1a60".
# Now if we print: 
CSE_marks = 95
print(CSE_marks) #--> 95   Simply prints the value at the memory location , making this easier to access CSE_marks anywhere  in the code .

#  This allows programmers to store and manipulate data values efficiently
#  total_marks = CSE_marks + DA_marks
DA_marks = 88
total_marks = CSE_marks + DA_marks
print(total_marks)  #--> 183
# This allows programmers to store and manipulate data values efficiently
# This allows programmers to store and manipulate data values
# Unlike Statically typed languages like C or Java, Python is dynamically typed.C/C++ , so we don't need to declare variable explicitly.
# In Python, variables are created when you assign a value to them, and they can change type dynamically.
# e.g: int CSE_marks = 95;  // C/C++ - Statically typed
#      CSE_marks = "A+";    // C/C++ - Error: type mismatch
#      CSE_marks = 95.5;    // C/C++ - Error : type mismatch
# In Python, you can do this:
CSE_marks = 95  # Initially an integer
print(CSE_marks)  #--> 95
CSE_marks = "A+"  # Now a string
print(CSE_marks)  #--> A+
CSE_marks = 95.5  # Now a float
print(CSE_marks)  #--> 95.5
# CSE_marks = True  # Now a boolean
# type(var_name) -> this will return the data type of the variable
print(type(CSE_marks))  #--> <class 'float'>  (after the last
if(type(CSE_marks) == float):
     new_CSE_marks = CSE_marks - 5.5
     print(f"New CSE marks after deduction: {new_CSE_marks}")  #--> New CSE marks after deduction: 90.0
else:
     pass

# Variables can hold data of various types like numbers, strings , booleans, lists, dictionaries, tuples etc.
# The type keyword (actually the type() function in Python) is important in backend development for several reasons:
# 1. Dynamic Type Checking: Backend code often processes data from various sources (APIs, databases, user input). Using type() helps verify and validate data types at runtime, preventing errors.
# 2. Serialization/Deserialization: When converting data to/from JSON, XML, or other formats, knowing the type ensures correct parsing and formatting.
# 3. Data Validation: Frameworks (like Django, Flask) use type checks to enforce schema constraints and prevent invalid data from entering the system.
# 4. Debugging: type() helps developers quickly inspect variables and diagnose issues during development or in logs.
# 5. Polymorphism and Dynamic Behavior: In object-oriented backends, type() can be used to implement logic that depends on the class/type of an object.

# Example: Type checking in a backend API handler
def process_user_input(data):
    if type(data) is dict:
        # Process as a dictionary (e.g., JSON payload)
        print("Received a dictionary:", data)
    elif type(data) is list:
        # Process as a list (e.g., batch input)
        print("Received a list:", data)
    else:
        print("Unsupported data type:", type(data))

# Simulate backend input
process_user_input({"username": "alice", "age": 30})
process_user_input(["alice", "bob", "charlie"])
process_user_input("just a string")

# Variables naming conventions:
# 1. Use descriptive names: Choose names that clearly indicate the purpose of the variable.
#   e.g., `user_age`, `total_price`, `is_active`
# 2. Use snake_case: In Python, it's common to use lowercase letters with underscores to separate words.
#   e.g., `user_age`, `total_price`, `is_active`
# 3. Avoid single-letter names: Unless in a small scope (like loop counters), avoid single-letter names like `x`, `y`, or `z`.
#   e.g., `user_age` instead of `a`, `b`, or `c`
# 4. Use meaningful abbreviations: If a variable name is too long, use clear abbreviations.
#   e.g., `num_items` instead of `number_of_items`
# 5. Avoid reserved keywords: Don't use Python's reserved keywords (like `if`, `for`, `while`,
# `class`, etc.) as variable names.
#   e.g., `user_age` instead of `if`, `for`, or `while`
# 6. Use consistent naming: Stick to a consistent naming style throughout your codebase
#   e.g., if you use `snake_case`, use it consistently for all variable names
# 7. Use plural names for collections: If a variable holds multiple items, use a plural name.
#   e.g., `user_list` for a list of users, `items` for a collection of items
# 8. Use prefixes for boolean variables: Use prefixes like `is_`, `has_`, or `can_` to indicate boolean variables.
#   e.g., `is_active`, `has_permission`, `can_edit`
# 9. Avoid using numbers in variable names: Unless necessary, avoid using numbers in variable names as they can be confusing.
#   e.g., `user_age` instead of `user_age1`, `user_age2`
# 10. Use context-specific names: If a variable is used in a specific context, include that context in the name.
#    e.g., `db_connection` for a database connection, `api_response` for an API response
# 11. Use constants for fixed values: If a variable holds a fixed value that doesn't change, use uppercase letters with underscores.
#    e.g., `MAX_RETRIES`, `DEFAULT_TIMEOUT`
# 12. Avoid using global variables: Global variables can lead to confusion and bugs. Use local variables or class attributes instead.
#  e.g., use `self.user_age` in a class instead of a global variable `user_age`
# 13. Use comments for clarity: If a variable name is not self-explanatory, add a comment to explain its purpose.
#    e.g., `user_age = 30  # Age of the user in years`
# 14. Use type hints (Python 3.5+): Type hints can help clarify the expected type of a variable.
#    e.g., `user_age: int = 30`, `user_list: List[str] = ["alice", "bob"]`
# 15. Avoid using special characters: Stick to alphanumeric characters and underscores in variable names.
#    e.g., `user_age` instead of `user-age` or `user@age`
# 16. Use meaningful names for temporary variables: Even temporary variables should have descriptive names.
#    e.g., `temp_user_age`  instead of `temp1`, `temp2`
# 17. Use context managers for resource management: When dealing with resources like files or database connections, use context managers to ensure proper cleanup.
#    e.g., `with open("file.txt") as file:`, `with db.connect() as connection:`
# 18. Use type annotations for function parameters and return types:
#    Type annotations can help clarify the expected types of function parameters and return values.
#    e.g., `def calculate_total(price: float, quantity: int) -> float:`, `def get_user_info(user_id: int) -> Dict[str, Any]:`   
# 19. Use underscores for readability: If a variable name is long, use underscores to separate words for better readability.
#    e.g., `user_profile_picture_url` instead of `userprofilepictureurl`
# 20. Use singular names for single items: If a variable holds a single item, use a singular name.
#    e.g., `user_name` for a single user's name, `item_price`
# 21. Use descriptive names for functions: Function names should clearly indicate their purpose.
#    e.g., `calculate_total_price()`, `fetch_user_data()`, `send_email_notification()`
# 22. Avoid using magic numbers: Instead of using hard-coded numbers, use named constants to improve clarity.
#    e.g., `MAX_RETRIES = 5`
# IMPLEMENTING CONSTANTS IN PYTHON

print("\nIMPLEMENTING CONSTANTS IN PYTHON:")
print("="*32)

# Python does not have built-in constant types like some languages (e.g., 'const' in C/C++).
# By convention, constants are defined using ALL_UPPERCASE variable names.
# from typing import Final
# Example of constants
PI = 3.14159
MAX_CONNECTIONS = 10
DEFAULT_TIMEOUT = 30

print(f"PI: {PI}")
print(f"MAX_CONNECTIONS: {MAX_CONNECTIONS}")
print(f"DEFAULT_TIMEOUT: {DEFAULT_TIMEOUT}")

# Constants are not truly immutable in Python, but using uppercase names signals to other developers not to change them.

# For stricter enforcement, you can use a class or module to encapsulate constants.
class _Constants:
    PI = 3.14159
    MAX_CONNECTIONS = 10
    DEFAULT_TIMEOUT = 30

# Usage:
print(f"Constants.PI: {_Constants.PI}")

# For advanced use, you can use typing.Final (Python 3.8+) to indicate a variable should not be reassigned.

API_KEY: Final = "my-secret-api-key"
print(f"API_KEY: {API_KEY}")
if API_KEY != "my-secret-api-key":
    raise ValueError("Invalid API_KEY: API_KEY does not match the expected value.")

# Attempting to reassign a Final variable will not cause a runtime error, but type checkers (like mypy) will warn you.

# Summary:
# - Use ALL_UPPERCASE names for constants.
# - Optionally use typing.Final for static analysis.
# - Remember: Python does not enforce immutability at runtime.

name: Final = "John Doe"
print(f"Name: {name}")
if name != "John Doe":
    raise ValueError("Invalid name: Name does not match the expected value.")
# Do not reassign a Final variable to avoid static analysis warnings
# name = "Jane Doe"  # This will not raise an error, but mypy will warn you.
# print(f"Updated Name: {name}")  #--> Updated Name: Jane Doe

# To make memory access more secure in Python:
# - Use encapsulation: make attributes private (prefix with __) or protected (_).
# - Avoid exposing sensitive data directly.
# - Use properties to control access and validation.
# - For critical data, consider encryption before storing in memory.
# - Limit the scope of variables and avoid using global variables for sensitive info.
# - Use type hints and Final to prevent accidental reassignment.

# Example: Restricting variable assignment to float values using property

class FloatOnly:
    def __init__(self, value: float):
        self._value = None
        self.value = value  # Will trigger the setter

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, float):
            raise TypeError("Value must be a float")
        self._value = new_value

# Usage example:
try:
    f = FloatOnly(3.14)
    print(f"Float value: {f.value}")
    f.value = 2.71  # OK
    print(f"Updated float value: {f.value}")
    f.value = "not a float"  # Raises TypeError
except TypeError as e:
    print(f"Error: {e}")

# Variables are case-sensitive in Python, meaning `variable`, `Variable`, and `VARIABLE` are considered different identifiers.

name00:Final="venky"
name01:Final="RBR"
name02:Final="Jay"
print(f"Name 00: {name00}")
print(f"Name 01: {name01}")
print(f"Name 02: {name02}")
# the identity of the objects are different
print(f"Memory address of name00: {hex(id(name00))}")
print(f"Memory address of name01: {hex(id(name01))}")
print(f"Memory address of name02: {hex(id(name02))}")
name03:Final="venky"
print(f"Name 03: {name03}")
# the identity of the objects with the same string are same
print(f"Memory address of name03: {hex(id(name03))}")
# VARIABLE IDENTITY AND MEMORY MANAGEMENT IN PYTHON
print("\nVARIABLE IDENTITY AND MEMORY MANAGEMENT:")
print("="*45)

# Python's string interning optimization
# Small strings and integers are cached by Python for memory efficiency
# This is why name00 and name03 have the same memory address

# Demonstrating object identity with different data types
print("\nOBJECT IDENTITY COMPARISON:")
print("="*28)

# Integer identity - Python caches small integers (-5 to 256)
a = 100
b = 100
print(f"a = {a}, b = {b}")
print(f"a is b: {a is b}")  # True - same object
print(f"id(a): {hex(id(a))}, id(b): {hex(id(b))}")

# Large integers are not cached
c = 1000
d = 1000
print(f"c = {c}, d = {d}")
print(f"c is d: {c is d}")  # False - different objects
print(f"id(c): {hex(id(c))}, id(d): {hex(id(d))}")

# String identity - immutable strings with same content may be interned
str1 = "hello"
str2 = "hello"
print(f"str1 = '{str1}', str2 = '{str2}'")
print(f"str1 is str2: {str1 is str2}")  # True - same object
print(f"id(str1): {hex(id(str1))}, id(str2): {hex(id(str2))}")

# Lists are mutable - always different objects
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(f"list1 = {list1}, list2 = {list2}")
print(f"list1 is list2: {list1 is list2}")  # False - different objects
print(f"list1 == list2: {list1 == list2}")  # True - same content
print(f"id(list1): {hex(id(list1))}, id(list2): {hex(id(list2))}")

# MEMORY OPTIMIZATION TECHNIQUES
print("\nMEMORY OPTIMIZATION TECHNIQUES:")
print("="*32)

# 1. Using __slots__ to reduce memory overhead
class OptimizedClass:
    __slots__ = ['name', 'age', 'email']
    
    def __init__(self, name: str, age: int, email: str):
        self.name = name
        self.age = age
        self.email = email

class RegularClass:
    def __init__(self, name: str, age: int, email: str):
        self.name = name
        self.age = age
        self.email = email

# Memory usage comparison
optimized = OptimizedClass("John", 30, "john@example.com")
regular = RegularClass("John", 30, "john@example.com")

print(f"Optimized class memory: {sys.getsizeof(optimized)} bytes")
print(f"Regular class memory: {sys.getsizeof(regular)} bytes")

# 2. Generator expressions for memory-efficient iteration
def memory_efficient_processing():
    """Demonstrates memory-efficient data processing"""
    # Memory-intensive approach (loads all data into memory)
    large_list = [x**2 for x in range(10000)]
    print(f"List memory usage: {sys.getsizeof(large_list)} bytes")
    
    # Memory-efficient approach (generates values on demand)
    large_generator = (x**2 for x in range(10000))
    print(f"Generator memory usage: {sys.getsizeof(large_generator)} bytes")
    
    # Process first 5 values from generator
    first_five = [next(large_generator) for _ in range(5)]
    print(f"First 5 squares: {first_five}")

memory_efficient_processing()

# VARIABLE LIFETIME AND SCOPE MANAGEMENT
print("\nVARIABLE LIFETIME AND SCOPE MANAGEMENT:")
print("="*42)

# Reference counting and garbage collection

class ResourceManager:
    """Demonstrates proper resource management"""
    
    def __init__(self, resource_name: str):
        self.resource_name = resource_name
        self.is_active = True
        print(f"Resource '{resource_name}' created")
    
    def __del__(self):
        print(f"Resource '{self.resource_name}' destroyed")
    
    def close(self):
        self.is_active = False
        print(f"Resource '{self.resource_name}' closed")

# Demonstrate reference counting
def demonstrate_reference_counting():
    """Shows how Python manages object references"""
    # Create object
    resource = ResourceManager("DB_Connection")
    print(f"Reference count: {sys.getrefcount(resource)}")
    
    # Create additional reference
    resource_ref = resource
    print(f"Reference count after alias: {sys.getrefcount(resource)}")
    
    # Remove reference
    del resource_ref
    print(f"Reference count after deletion: {sys.getrefcount(resource)}")
    
    # Object will be destroyed when function exits
    return resource

# Weak references for avoiding circular references
class Parent:
    def __init__(self, name: str):
        self.name = name
        self.children = []
    
    def add_child(self, child):
        self.children.append(child)
        child.parent = weakref.ref(self)  # Weak reference to avoid circular dependency

class Child:
    def __init__(self, name: str):
        self.name = name
        self.parent = None
    
    def get_parent(self):
        if self.parent is not None:
            return self.parent()  # Dereference weak reference
        return None

# ENTERPRISE-GRADE VARIABLE MANAGEMENT
print("\nENTERPISE-GRADE VARIABLE MANAGEMENT:")
print("="*39)

# 1. Configuration management with environment variables

@dataclass
class DatabaseConfig:
    """Type-safe configuration management"""
    host: str
    port: int
    username: str
    password: str
    database: str
    
    @classmethod
    def from_env(cls) -> 'DatabaseConfig':
        """Load configuration from environment variables"""
        return cls(
            host=os.getenv('DB_HOST', 'localhost'),
            port=int(os.getenv('DB_PORT', '5432')),
            username=os.getenv('DB_USERNAME', 'postgres'),
            password=os.getenv('DB_PASSWORD', ''),
            database=os.getenv('DB_NAME', 'myapp')
        )

# 2. Thread-safe variable access

class ThreadSafeCounter:
    """Thread-safe counter implementation"""
    
    def __init__(self):
        self._value = 0
        self._lock = threading.Lock()
    
    def increment(self):
        with self._lock:
            self._value += 1
    
    def decrement(self):
        with self._lock:
            self._value -= 1
    
    @property
    def value(self):
        with self._lock:
            return self._value

# 3. Context manager for resource cleanup
@contextmanager
def managed_resource(resource_name: str):
    """Context manager for automatic resource cleanup"""
    resource = ResourceManager(resource_name)
    try:
        yield resource
    finally:
        resource.close()

# Usage example
with managed_resource("API_Connection") as resource:
    print(f"Using {resource.resource_name}")
    # Resource automatically cleaned up

# 4. Singleton pattern for global state management
class DatabaseConnection:
    """Singleton database connection"""
    _instance = None
    _lock = threading.Lock()
    
    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._initialized = False
        return cls._instance
    
    def __init__(self):
        if not self._initialized:
            self.connection_string = "postgresql://localhost:5432/myapp"
            self.is_connected = False
            self._initialized = True
    
    def connect(self):
        if not self.is_connected:
            print(f"Connecting to {self.connection_string}")
            self.is_connected = True
    
    def disconnect(self):
        if self.is_connected:
            print("Disconnecting from database")
            self.is_connected = False

# Test singleton behavior
db1 = DatabaseConnection()
db2 = DatabaseConnection()
print(f"Same instance: {db1 is db2}")  # True

# ADVANCED VARIABLE PATTERNS FOR BACKEND SYSTEMS
print("\nADVANCED VARIABLE PATTERNS FOR BACKEND SYSTEMS:")
print("="*48)

# 1. Factory pattern for dynamic object creation
class LoggerFactory:
    """Factory for creating different types of loggers"""
    
    _loggers = {}
    
    @classmethod
    def get_logger(cls, logger_type: str, config: dict):
        """Get or create logger instance"""
        if logger_type not in cls._loggers:
            if logger_type == 'file':
                cls._loggers[logger_type] = FileLogger(config)
            elif logger_type == 'console':
                cls._loggers[logger_type] = ConsoleLogger(config)
            elif logger_type == 'network':
                cls._loggers[logger_type] = NetworkLogger(config)
            else:
                raise ValueError(f"Unknown logger type: {logger_type}")
        
        return cls._loggers[logger_type]

class FileLogger:
    def __init__(self, config: dict):
        self.filename = config.get('filename', 'app.log')
        self.level = config.get('level', 'INFO')
    
    def log(self, message: str):
        print(f"[FILE:{self.level}] {message}")

class ConsoleLogger:
    def __init__(self, config: dict):
        self.level = config.get('level', 'INFO')
    
    def log(self, message: str):
        print(f"[CONSOLE:{self.level}] {message}")

class NetworkLogger:
    def __init__(self, config: dict):
        self.endpoint = config.get('endpoint', 'localhost:8080')
        self.level = config.get('level', 'INFO')
    
    def log(self, message: str):
        print(f"[NETWORK:{self.level}] {message} -> {self.endpoint}")

# 2. Dependency injection pattern
class ServiceContainer:
    """Simple dependency injection container"""
    
    def __init__(self):
        self._services = {}
        self._singletons = {}
    
    def register(self, service_name: str, factory, singleton: bool = False):
        """Register a service factory"""
        self._services[service_name] = {
            'factory': factory,
            'singleton': singleton
        }
    
    def get(self, service_name: str):
        """Get service instance"""
        if service_name not in self._services:
            raise ValueError(f"Service '{service_name}' not registered")
        
        service_config = self._services[service_name]
        
        if service_config['singleton']:
            if service_name not in self._singletons:
                self._singletons[service_name] = service_config['factory']()
            return self._singletons[service_name]
        else:
            return service_config['factory']()

# Setup dependency injection
container = ServiceContainer()
container.register('logger', lambda: LoggerFactory.get_logger('console', {'level': 'DEBUG'}), singleton=True)
container.register('db', lambda: DatabaseConnection(), singleton=True)

# Usage
logger = container.get('logger')
db = container.get('db')

# 3. Observer pattern for event-driven systems
class EventEmitter:
    """Event emitter for decoupled communication"""
    
    def __init__(self):
        self._listeners = {}
    
    def on(self, event: str, callback):
        """Register event listener"""
        if event not in self._listeners:
            self._listeners[event] = []
        self._listeners[event].append(callback)
    
    def emit(self, event: str, data=None):
        """Emit event to all listeners"""
        if event in self._listeners:
            for callback in self._listeners[event]:
                callback(data)

# Event-driven user service
class UserService:
    def __init__(self, event_emitter: EventEmitter):
        self.event_emitter = event_emitter
        self.users = {}
    
    def create_user(self, user_id: str, user_data: dict):
        self.users[user_id] = user_data
        self.event_emitter.emit('user_created', {'user_id': user_id, 'data': user_data})
    
    def update_user(self, user_id: str, user_data: dict):
        if user_id in self.users:
            self.users[user_id].update(user_data)
            self.event_emitter.emit('user_updated', {'user_id': user_id, 'data': user_data})

# Email service listening to user events
class EmailService:
    def __init__(self, event_emitter: EventEmitter):
        event_emitter.on('user_created', self.send_welcome_email)
        event_emitter.on('user_updated', self.send_update_notification)
    
    def send_welcome_email(self, event_data):
        user_id = event_data['user_id']
        print(f"Sending welcome email to user {user_id}")
    
    def send_update_notification(self, event_data):
        user_id = event_data['user_id']
        print(f"Sending update notification to user {user_id}")

# Wire up services
events = EventEmitter()
user_service = UserService(events)
email_service = EmailService(events)

# Test event-driven architecture
user_service.create_user('user123', {'name': 'John Doe', 'email': 'john@example.com'})
user_service.update_user('user123', {'last_login': '2023-12-01'})

# PRODUCTION-READY VARIABLE VALIDATION
print("\nPRODUCTION-READY VARIABLE VALIDATION:")
print("="*37)


class Validator(ABC):
    """Abstract base class for validators"""
    
    @abstractmethod
    def validate(self, value: Any) -> bool:
        pass
    
    @abstractmethod
    def get_error_message(self) -> str:
        pass

class TypeValidator(Validator):
    def __init__(self, expected_type: type):
        self.expected_type = expected_type
    
    def validate(self, value: Any) -> bool:
        return isinstance(value, self.expected_type)
    
    def get_error_message(self) -> str:
        return f"Expected type {self.expected_type.__name__}"

class RangeValidator(Validator):
    def __init__(self, min_value: Union[int, float], max_value: Union[int, float]):
        self.min_value = min_value
        self.max_value = max_value
    
    def validate(self, value: Any) -> bool:
        try:
            return self.min_value <= value <= self.max_value
        except TypeError:
            return False
    
    def get_error_message(self) -> str:
        return f"Value must be between {self.min_value} and {self.max_value}"

class ValidatedVariable:
    """Variable with built-in validation"""
    
    def __init__(self, initial_value: Any, validators: List[Validator]):
        self.validators = validators
        self._value = None
        self.value = initial_value  # Trigger validation
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, new_value):
        for validator in self.validators:
            if not validator.validate(new_value):
                raise ValueError(f"Validation failed: {validator.get_error_message()}")
        self._value = new_value

# Usage examples
try:
    # Create validated integer in range
    age = ValidatedVariable(25, [
        TypeValidator(int),
        RangeValidator(0, 150)
    ])
    
    print(f"Age: {age.value}")
    
    # This will raise an error
    age.value = 200
    
except ValueError as e:
    print(f"Validation error: {e}")

# MEMORY PROFILING AND OPTIMIZATION
print("\nMEMORY PROFILING AND OPTIMIZATION:")
print("="*34)

def analyze_memory_usage():
    """Analyze memory usage of different data structures"""
    
    # Dictionary vs named tuple vs dataclass memory usage
    
    # Regular dictionary
    dict_data = {'name': 'John', 'age': 30, 'email': 'john@example.com'}
    
    # Named tuple
    Person = namedtuple('Person', ['name', 'age', 'email'])
    tuple_data = Person('John', 30, 'john@example.com')
    
    # Dataclass
    @dataclass
    class PersonData:
        name: str
        age: int
        email: str
    
    dataclass_data = PersonData('John', 30, 'john@example.com')
    
    print(f"Dictionary memory: {sys.getsizeof(dict_data)} bytes")
    print(f"Named tuple memory: {sys.getsizeof(tuple_data)} bytes")
    print(f"Dataclass memory: {sys.getsizeof(dataclass_data)} bytes")

analyze_memory_usage()

# ENTERPRISE ERROR HANDLING AND LOGGING
print("\nENTERPRISE ERROR HANDLING AND LOGGING:")
print("="*39)


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

def log_function_calls(func):
    """Decorator to log function calls and handle errors"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger = logging.getLogger(func.__module__)
        logger.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        
        try:
            result = func(*args, **kwargs)
            logger.info(f"{func.__name__} completed successfully")
            return result
        except Exception as e:
            logger.error(f"{func.__name__} failed with error: {e}")
            raise
    
    return wrapper

@log_function_calls
def divide_numbers(a: float, b: float) -> float:
    """Divide two numbers with error handling"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# Test error handling
try:
    result = divide_numbers(10, 2)
    print(f"Division result: {result}")
    
    # This will trigger error logging
    result = divide_numbers(10, 0)
except ValueError as e:
    print(f"Caught error: {e}")

# SUMMARY AND BEST PRACTICES
print("\n" + "="*60)
print("BACKEND DEVELOPMENT BEST PRACTICES - SUMMARY")
print("="*60)
print("✓ Use type hints for better code documentation and IDE support")
print("✓ Implement proper error handling with contextual logging")
print("✓ Use design patterns (Factory, Singleton, Observer) for scalable architecture")
print("✓ Implement dependency injection for testable and maintainable code")
print("✓ Use context managers for resource management")
print("✓ Implement proper validation for all user inputs")
print("✓ Use weak references to avoid circular dependencies")
print("✓ Optimize memory usage with generators and __slots__")
print("✓ Implement thread-safe operations for concurrent environments")
print("✓ Use configuration management for environment-specific settings")
print("✓ Implement proper monitoring and observability")
print("✓ Follow SOLID principles for maintainable code architecture")
print("="*60)

# FINAL ENTERPRISE-GRADE EXAMPLE
print("\nFINAL ENTERPRISE-GRADE EXAMPLE:")
print("="*32)

class ApplicationContext:
    """Enterprise application context with full lifecycle management"""
    
    def __init__(self):
        self.services = ServiceContainer()
        self.event_emitter = EventEmitter()
        self.config = DatabaseConfig.from_env()
        self._setup_services()
    
    def _setup_services(self):
        """Initialize all application services"""
        # Register core services
        self.services.register('config', lambda: self.config, singleton=True)
        self.services.register('events', lambda: self.event_emitter, singleton=True)
        self.services.register('logger', lambda: LoggerFactory.get_logger('console', {'level': 'INFO'}), singleton=True)
        
        # Register business services
        self.services.register('user_service', lambda: UserService(self.event_emitter), singleton=True)
        self.services.register('email_service', lambda: EmailService(self.event_emitter), singleton=True)
    
    def get_service(self, service_name: str):
        """Get service from container"""
        return self.services.get(service_name)
    
    def shutdown(self):
        """Graceful application shutdown"""
        logger = self.get_service('logger')
        logger.log("Application shutting down...")
        
        # Cleanup resources
        if hasattr(self, '_db_connection'):
            self._db_connection.disconnect()

# Example usage of enterprise-grade application
if __name__ == "__main__":
    app = ApplicationContext()
    
    # Get services
    user_service = app.get_service('user_service')
    logger = app.get_service('logger')
    
    # Use services
    logger.log("Application started")
    user_service.create_user('enterprise_user', {
        'name': 'Enterprise User',
        'email': 'enterprise@company.com',
        'role': 'admin'
    })
    
    # Graceful shutdown
    app.shutdown()

# Variables in Python assigned using the "variable_name" syntax
# Multiple assignments : Python allows multiple variables to be assigned in a single line.
x, y, z = 1, 2, 3
print(f"x: {x}, y: {y}, z: {z}")  #--> x: 1, y: 2, z: 3


# PYTHON DATA TYPES - COMPREHENSIVE DEEP DIVE
print("\n" + "="*60)
print("PYTHON DATA TYPES - COMPREHENSIVE DEEP DIVE")
print("="*60)

# Python has several built-in data types. Let's explore each one in detail.

# 1. NUMERIC TYPES
print("\n1. NUMERIC TYPES:")
print("="*18)

# Integer (int)
print("\nINTEGER (int):")
print("-" * 14)
integer_var = 42
negative_int = -100
large_int = 1234567890123456789
print(f"Integer: {integer_var}, Type: {type(integer_var)}")
print(f"Negative: {negative_int}, Type: {type(negative_int)}")
print(f"Large integer: {large_int}, Type: {type(large_int)}")

# Integer operations
print("\nInteger operations:")
a, b = 15, 4
print(f"a = {a}, b = {b}")
print(f"Addition: {a} + {b} = {a + b}")
print(f"Subtraction: {a} - {b} = {a - b}")
print(f"Multiplication: {a} * {b} = {a * b}")
print(f"Division: {a} / {b} = {a / b}")  # Returns float
print(f"Floor division: {a} // {b} = {a // b}")  # Returns int
print(f"Modulus: {a} % {b} = {a % b}")
print(f"Exponentiation: {a} ** {b} = {a ** b}")

# Float (float)
print("\nFLOAT (float):")
print("-" * 14)
float_var = 3.14159
scientific_notation = 1.23e-4
infinity = float('inf')
negative_infinity = float('-inf')
not_a_number = float('nan')

print(f"Float: {float_var}, Type: {type(float_var)}")
print(f"Scientific notation: {scientific_notation}, Type: {type(scientific_notation)}")
print(f"Infinity: {infinity}, Type: {type(infinity)}")
print(f"Negative infinity: {negative_infinity}")
print(f"Not a number: {not_a_number}")

# Float precision and operations
print("\nFloat precision issues:")
result = 0.1 + 0.2
print(f"0.1 + 0.2 = {result}")
print(f"Is 0.1 + 0.2 == 0.3? {result == 0.3}")

# Working with decimal for precise calculations
decimal_result = Decimal('0.1') + Decimal('0.2')
print(f"Using Decimal: {decimal_result}")
print(f"Is Decimal result == 0.3? {decimal_result == Decimal('0.3')}")

# Complex numbers (complex)
print("\nCOMPLEX (complex):")
print("-" * 16)
complex_var = 3 + 4j
complex_from_function = complex(2, 5)
print(f"Complex number: {complex_var}, Type: {type(complex_var)}")
print(f"Complex from function: {complex_from_function}")
print(f"Real part: {complex_var.real}")
print(f"Imaginary part: {complex_var.imag}")
print(f"Conjugate: {complex_var.conjugate()}")
print(f"Absolute value: {abs(complex_var)}")

# 2. SEQUENCE TYPES
print("\n2. SEQUENCE TYPES:")
print("="*18)

# String (str)
print("\nSTRING (str):")
print("-" * 13)
string_var = "Hello, World!"
multiline_string = """This is a
multiline string
with multiple lines"""
raw_string = r"This is a raw string with \n and \t"
f_string = f"The value is {integer_var}"

print(f"String: {string_var}, Type: {type(string_var)}")
print(f"Length: {len(string_var)}")
print(f"Multiline string: {repr(multiline_string)}")
print(f"Raw string: {raw_string}")
print(f"F-string: {f_string}")

# String operations
print("\nString operations:")
text = "Python Programming"
print(f"Original: {text}")
print(f"Uppercase: {text.upper()}")
print(f"Lowercase: {text.lower()}")
print(f"Title case: {text.title()}")
print(f"Replace: {text.replace('Python', 'Java')}")
print(f"Split: {text.split()}")
print(f"Find 'gram': {text.find('gram')}")
print(f"Count 'r': {text.count('r')}")

# String indexing and slicing
print("\nString indexing and slicing:")
print(f"First character: {text[0]}")
print(f"Last character: {text[-1]}")
print(f"First 6 characters: {text[:6]}")
print(f"Last 11 characters: {text[7:]}")
print(f"Every 2nd character: {text[::2]}")
print(f"Reversed: {text[::-1]}")

# List (list)
print("\nLIST (list):")
print("-" * 12)
list_var = [1, 2, 3, 4, 5]
mixed_list = [1, "hello", 3.14, True, [1, 2, 3]]
empty_list = []

print(f"List: {list_var}, Type: {type(list_var)}")
print(f"Mixed list: {mixed_list}")
print(f"Empty list: {empty_list}")

# List operations
print("\nList operations:")
fruits = ["apple", "banana", "orange"]
print(f"Original list: {fruits}")

# Adding elements
fruits.append("grape")
print(f"After append: {fruits}")

fruits.insert(1, "mango")
print(f"After insert: {fruits}")

fruits.extend(["kiwi", "pineapple"])
print(f"After extend: {fruits}")

# Removing elements
removed = fruits.pop()
print(f"After pop: {fruits}, Removed: {removed}")

fruits.remove("banana")
print(f"After remove: {fruits}")

# List methods
print(f"Index of 'orange': {fruits.index('orange')}")
print(f"Count of 'apple': {fruits.count('apple')}")

# List comprehension
squares = [x**2 for x in range(1, 6)]
print(f"Squares: {squares}")

even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
print(f"Even squares: {even_squares}")

# Tuple (tuple)
print("\nTUPLE (tuple):")
print("-" * 13)
tuple_var = (1, 2, 3, 4, 5)
mixed_tuple = (1, "hello", 3.14, True)
single_element_tuple = (42,)  # Note the comma
empty_tuple = ()

print(f"Tuple: {tuple_var}, Type: {type(tuple_var)}")
print(f"Mixed tuple: {mixed_tuple}")
print(f"Single element tuple: {single_element_tuple}")
print(f"Empty tuple: {empty_tuple}")

# Tuple operations
print("\nTuple operations:")
coordinates = (10, 20)
print(f"Coordinates: {coordinates}")
print(f"X coordinate: {coordinates[0]}")
print(f"Y coordinate: {coordinates[1]}")

# Tuple unpacking
x, y = coordinates
print(f"Unpacked: x={x}, y={y}")

# Named tuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
print(f"Named tuple: {p}")
print(f"X coordinate: {p.x}")
print(f"Y coordinate: {p.y}")

# Range (range)
print("\nRANGE (range):")
print("-" * 13)
range_var = range(10)
range_with_start = range(2, 10)
range_with_step = range(0, 20, 2)

print(f"Range: {range_var}, Type: {type(range_var)}")
print(f"Range list: {list(range_var)}")
print(f"Range with start: {list(range_with_start)}")
print(f"Range with step: {list(range_with_step)}")

# 3. MAPPING TYPE
print("\n3. MAPPING TYPE:")
print("="*16)

# Dictionary (dict)
print("\nDICTIONARY (dict):")
print("-" * 17)
dict_var = {"name": "Alice", "age": 30, "city": "New York"}
mixed_dict = {1: "one", "two": 2, 3.0: "three"}
empty_dict = {}

print(f"Dictionary: {dict_var}, Type: {type(dict_var)}")
print(f"Mixed dictionary: {mixed_dict}")
print(f"Empty dictionary: {empty_dict}")

# Dictionary operations
print("\nDictionary operations:")
student = {"name": "John", "age": 20, "grade": "A"}
print(f"Original: {student}")

# Accessing values
print(f"Name: {student['name']}")
print(f"Age: {student.get('age', 'Not found')}")
print(f"GPA: {student.get('gpa', 'Not found')}")

# Adding/updating values
student["gpa"] = 3.8
student["age"] = 21
print(f"After updates: {student}")

# Dictionary methods
print(f"Keys: {list(student.keys())}")
print(f"Values: {list(student.values())}")
print(f"Items: {list(student.items())}")

# Dictionary comprehension
squares_dict = {x: x**2 for x in range(1, 6)}
print(f"Squares dictionary: {squares_dict}")

# 4. SET TYPES
print("\n4. SET TYPES:")
print("="*12)

# Set (set)
print("\nSET (set):")
print("-" * 10)
set_var = {1, 2, 3, 4, 5}
mixed_set = {1, "hello", 3.14, True}
empty_set = set()  # Note: {} creates an empty dict, not set

print(f"Set: {set_var}, Type: {type(set_var)}")
print(f"Mixed set: {mixed_set}")
print(f"Empty set: {empty_set}")

# Set operations
print("\nSet operations:")
fruits_set = {"apple", "banana", "orange"}
print(f"Original set: {fruits_set}")

# Adding elements
fruits_set.add("grape")
print(f"After add: {fruits_set}")

fruits_set.update(["kiwi", "pineapple"])
print(f"After update: {fruits_set}")

# Set operations
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

print(f"Set A: {set_a}")
print(f"Set B: {set_b}")
print(f"Union: {set_a | set_b}")
print(f"Intersection: {set_a & set_b}")
print(f"Difference: {set_a - set_b}")
print(f"Symmetric difference: {set_a ^ set_b}")

# Frozenset (frozenset)
print("\nFROZENSET (frozenset):")
print("-" * 19)
frozenset_var = frozenset([1, 2, 3, 4, 5])
print(f"Frozenset: {frozenset_var}, Type: {type(frozenset_var)}")

# 5. BOOLEAN TYPE
print("\n5. BOOLEAN TYPE:")
print("="*15)

# Boolean (bool)
print("\nBOOLEAN (bool):")
print("-" * 14)
bool_true = True
bool_false = False
bool_from_int = bool(1)
bool_from_string = bool("hello")
bool_from_empty = bool("")

print(f"True: {bool_true}, Type: {type(bool_true)}")
print(f"False: {bool_false}, Type: {type(bool_false)}")
print(f"bool(1): {bool_from_int}")
print(f"bool('hello'): {bool_from_string}")
print(f"bool(''): {bool_from_empty}")

# Boolean operations
print("\nBoolean operations:")
print(f"True and False: {True and False}")
print(f"True or False: {True or False}")
print(f"not True: {not True}")
print(f"not False: {not False}")

# Truthiness in Python
print("\nTruthiness in Python:")
values = [0, 1, "", "hello", [], [1, 2, 3], {}, {"key": "value"}, None]
for val in values:
    print(f"bool({repr(val)}): {bool(val)}")

# 6. NONE TYPE
print("\n6. NONE TYPE:")
print("="*12)

# None (NoneType)
print("\nNONE (NoneType):")
print("-" * 15)
none_var = None
print(f"None: {none_var}, Type: {type(none_var)}")

# Using None
def function_with_optional_param(param=None):
    if param is None:
        return "No parameter provided"
    return f"Parameter: {param}"

print(f"Function call: {function_with_optional_param()}")
print(f"Function call with param: {function_with_optional_param('Hello')}")

# 7. BINARY TYPES
print("\n7. BINARY TYPES:")
print("="*15)

# Bytes (bytes)
print("\nBYTES (bytes):")
print("-" * 13)
bytes_var = b"Hello, World!"
bytes_from_list = bytes([65, 66, 67, 68])
bytes_from_string = "Hello".encode('utf-8')

print(f"Bytes: {bytes_var}, Type: {type(bytes_var)}")
print(f"Bytes from list: {bytes_from_list}")
print(f"Bytes from string: {bytes_from_string}")

# Bytearray (bytearray)
print("\nBYTEARRAY (bytearray):")
print("-" * 19)
bytearray_var = bytearray(b"Hello")
print(f"Bytearray: {bytearray_var}, Type: {type(bytearray_var)}")

# Modify bytearray
bytearray_var[0] = 74  # ASCII for 'J'
print(f"Modified bytearray: {bytearray_var}")

# Memoryview (memoryview)
print("\nMEMORYVIEW (memoryview):")
print("-" * 21)
data = bytearray(b"Hello World")
mv = memoryview(data)
print(f"Memoryview: {mv}, Type: {type(mv)}")
print(f"Memoryview slice: {mv[0:5]}")

# 8. TYPE CONVERSION AND CHECKING
print("\n8. TYPE CONVERSION AND CHECKING:")
print("="*35)

# Type conversion examples
print("\nType conversion examples:")
# To integer
print(f"int('42'): {int('42')}")
print(f"int(3.14): {int(3.14)}")
print(f"int(True): {int(True)}")

# To float
print(f"float('3.14'): {float('3.14')}")
print(f"float(42): {float(42)}")

# To string
print(f"str(42): {str(42)}")
print(f"str(3.14): {str(3.14)}")
print(f"str(True): {str(True)}")

# To list
print(f"list('hello'): {list('hello')}")
print(f"list((1, 2, 3)): {list((1, 2, 3))}")

# To tuple
print(f"tuple([1, 2, 3]): {tuple([1, 2, 3])}")
print(f"tuple('hello'): {tuple('hello')}")

# To set
print(f"set([1, 2, 2, 3]): {set([1, 2, 2, 3])}")

# Type checking
print("\nType checking:")
value = 42
print(f"type(value): {type(value)}")
print(f"isinstance(value, int): {isinstance(value, int)}")
print(f"isinstance(value, (int, float)): {isinstance(value, (int, float))}")

# 9. MUTABLE VS IMMUTABLE TYPES
print("\n9. MUTABLE VS IMMUTABLE TYPES:")
print("="*33)

print("\nImmutable types (cannot be changed after creation):")
print("- int, float, complex, str, tuple, frozenset, bytes")

print("\nMutable types (can be changed after creation):")
print("- list, dict, set, bytearray")

# Demonstrating mutability
print("\nDemonstrating mutability:")

# Immutable example
original_string = "Hello"
print(f"Original string: {original_string}")
modified_string = original_string + " World"
print(f"Modified string: {modified_string}")
print(f"Original unchanged: {original_string}")

# Mutable example
original_list = [1, 2, 3]
print(f"Original list: {original_list}")
original_list.append(4)
print(f"Modified list: {original_list}")

# 10. ADVANCED DATA TYPES
print("\n10. ADVANCED DATA TYPES:")
print("="*23)

# Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

class Status(IntEnum):
    PENDING = 1
    APPROVED = 2
    REJECTED = 3

print(f"Color enum: {Color.RED}")
print(f"Status enum: {Status.PENDING}")
print(f"Status value: {Status.PENDING.value}")

# Dataclass

@dataclass
class Person:
    name: str
    age: int
    email: str = field(default="")
    hobbies: list = field(default_factory=list)
    
    def __post_init__(self):
        if self.age < 0:
            raise ValueError("Age cannot be negative")

person = Person("Alice", 30, "alice@example.com", ["reading", "coding"])
print(f"Person: {person}")

# Collections module types

# Deque
deque_var = deque([1, 2, 3])
deque_var.appendleft(0)
deque_var.append(4)
print(f"Deque: {deque_var}")

# DefaultDict
dd = defaultdict(list)
dd['key1'].append(1)
dd['key2'].append(2)
print(f"DefaultDict: {dict(dd)}")

# Counter
counter = Counter(['a', 'b', 'c', 'a', 'b', 'a'])
print(f"Counter: {counter}")
# print(f"Most common: {counter.most_common(2)}")

# OrderedDict (less relevant in Python 3.7+)
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(f"OrderedDict: {od}")

# ChainMap
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
cm = ChainMap(dict1, dict2)
print(f"ChainMap: {cm}")
print(f"ChainMap['b']: {cm['b']}")  # First occurrence

# 11. TYPE HINTS AND ANNOTATIONS
print("\n11. TYPE HINTS AND ANNOTATIONS:")
print("="*32)


# Function with type hints
def process_data(
    items: List[int], 
    multiplier: float = 1.0, 
    metadata: Optional[Dict[str, Any]] = None
) -> List[float]:
    """Process a list of integers and return floats."""
    if metadata is None:
        metadata = {}
    
    return [item * multiplier for item in items]

# Using the function
result = process_data([1, 2, 3, 4], 2.5)
print(f"Processed data: {result}")

# Type aliases
Vector = List[float]
Matrix = List[Vector]

def multiply_matrix(matrix: Matrix, scalar: float) -> Matrix:
    """Multiply a matrix by a scalar."""
    return [[element * scalar for element in row] for row in matrix]

# Generic types

T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self) -> None:
        self._items: List[T] = []
    
    def push(self, item: T) -> None:
        self._items.append(item)
    
    def pop(self) -> T:
        return self._items.pop()
    
    def is_empty(self) -> bool:
        return len(self._items) == 0

# Using generic stack
int_stack = Stack[int]()
int_stack.push(1)
int_stack.push(2)
print(f"Popped from int stack: {int_stack.pop()}")

# 12. MEMORY USAGE AND PERFORMANCE
print("\n12. MEMORY USAGE AND PERFORMANCE:")
print("="*34)


# Memory usage of different types
data_types = [
    42,
    3.14,
    "Hello",
    [1, 2, 3],
    (1, 2, 3),
    {1, 2, 3},
    {"a": 1, "b": 2},
    True,
    None,
    b"bytes"
]

print("Memory usage of different types:")
for item in data_types:
    print(f"{str(item)[:20]:20} {type(item).__name__:10} {sys.getsizeof(item):5} bytes")

# Performance comparison

def time_operation(operation, iterations=1000000):
    start = time.time()
    for _ in range(iterations):
        operation()
    end = time.time()
    return end - start

# List vs tuple performance
list_creation = lambda: [1, 2, 3, 4, 5]
tuple_creation = lambda: (1, 2, 3, 4, 5)

print(f"\nPerformance comparison (1M iterations):")
print(f"List creation: {time_operation(list_creation):.4f} seconds")
print(f"Tuple creation: {time_operation(tuple_creation):.4f} seconds")

# 13. BEST PRACTICES AND GOTCHAS
print("\n13. BEST PRACTICES AND GOTCHAS:")
print("="*33)

print("\nBest practices:")
print("✓ Use appropriate data types for your use case")
print("✓ Prefer immutable types when possible")
print("✓ Use type hints for better code documentation")
print("✓ Be aware of mutable default arguments")
print("✓ Use collections module for specialized data structures")
print("✓ Consider memory usage for large datasets")

print("\nCommon gotchas:")
print("• Mutable default arguments")
print("• Shallow vs deep copying")
print("• Integer identity for small numbers")
print("• Float precision issues")
print("• List modification during iteration")

# Demonstrating mutable default argument gotcha
def bad_function(items=[]):  # Don't do this!
    items.append(1)
    return items

def good_function(items=None):  # Do this instead
    if items is None:
        items = []
    items.append(1)
    return items

print(f"\nBad function first call: {bad_function()}")
print(f"Bad function second call: {bad_function()}")  # Same list!

print(f"Good function first call: {good_function()}")
print(f"Good function second call: {good_function()}")  # Different lists

# 14. PRACTICAL EXAMPLES
print("\n14. PRACTICAL EXAMPLES:")
print("="*21)

# Example 1: Data processing pipeline
def process_student_data(students_data):
    """Process student data through various transformations."""
    # Convert to proper data structure
    students = []
    for student in students_data:
        students.append({
            'name': student[0],
            'age': int(student[1]),
            'grades': [float(g) for g in student[2]]
        })
    
    # Calculate statistics
    for student in students:
        student['average'] = sum(student['grades']) / len(student['grades'])
        student['grade_letter'] = 'A' if student['average'] >= 90 else 'B' if student['average'] >= 80 else 'C'
    
    return students

# Sample data
raw_data = [
    ('Alice', '20', ['95', '87', '92']),
    ('Bob', '21', ['78', '85', '88']),
    ('Charlie', '19', ['92', '94', '89'])
]

processed_students = process_student_data(raw_data)
for student in processed_students:
    print(f"{student['name']}: {student['average']:.1f} ({student['grade_letter']})")

# Example 2: Configuration management
class Config:
    """Configuration management with type validation."""
    
    def __init__(self):
        self._config = {}
        self._types = {}
    
    def set(self, key: str, value: Any, expected_type: type = None):
        if expected_type and not isinstance(value, expected_type):
            raise TypeError(f"Expected {expected_type.__name__}, got {type(value).__name__}")
        self._config[key] = value
        if expected_type:
            self._types[key] = expected_type
    
    def get(self, key: str, default: Any = None):
        return self._config.get(key, default)
    
    def validate(self):
        for key, expected_type in self._types.items():
            if key in self._config:
                if not isinstance(self._config[key], expected_type):
                    raise TypeError(f"Config key '{key}' should be {expected_type.__name__}")

# Using the config
config = Config()
config.set('host', 'localhost', str)
config.set('port', 8080, int)
config.set('debug', True, bool)
config.set('timeout', 30.0, float)

print(f"\nConfiguration:")
print(f"Host: {config.get('host')}")
print(f"Port: {config.get('port')}")
print(f"Debug: {config.get('debug')}")
print(f"Timeout: {config.get('timeout')}")

# 15. SUMMARY
print("\n15. SUMMARY:")
print("="*12)
print("Python provides a rich set of built-in data types:")
print("• Numeric: int, float, complex")
print("• Sequence: str, list, tuple, range")
print("• Mapping: dict")
print("• Set: set, frozenset")
print("• Boolean: bool")
print("• Binary: bytes, bytearray, memoryview")
print("• None: NoneType")
print("")
print("Key characteristics:")
print("• Dynamic typing - variables can change type")
print("• Strong typing - operations are type-checked")
print("• Mutable vs immutable types")
print("• Rich set of built-in methods and operations")
print("• Extensive standard library for specialized types")
print("bytes, bytearray, and memoryview for binary data handling")
# MODERN BACKEND IMPLEMENTATIONS OF BYTES, BYTEARRAY, AND MEMORYVIEW
print("\n" + "="*70)
print("MODERN BACKEND IMPLEMENTATIONS OF BYTES, BYTEARRAY, AND MEMORYVIEW")
print("="*70)

# 1. BYTES TYPE - MODERN BACKEND APPLICATIONS
print("\n1. BYTES TYPE - MODERN BACKEND APPLICATIONS:")
print("="*45)

# File Upload and Processing
class FileProcessor:
    """Modern file processing with bytes"""
    
    def __init__(self):
        self.supported_formats = {
            b'\x89PNG\r\n\x1a\n': 'PNG',
            b'\xff\xd8\xff': 'JPEG',
            b'GIF87a': 'GIF87a',
            b'GIF89a': 'GIF89a',
            b'%PDF': 'PDF',
            b'PK\x03\x04': 'ZIP'
        }
    
    def detect_file_type(self, file_bytes: bytes) -> str:
        """Detect file type by magic bytes"""
        for magic, file_type in self.supported_formats.items():
            if file_bytes.startswith(magic):
                return file_type
        return 'Unknown'
    def process_upload(self, file_data: bytes, filename: str) -> dict:
        """Process uploaded file data"""
        file_type = self.detect_file_type(file_data)
        file_size = len(file_data)
        
        # Calculate checksum for integrity
        checksum = hashlib.md5(file_data).hexdigest()
        
        return {
            'filename': filename,
            'type': file_type,
            'size': file_size,
            'checksum': checksum,
            'is_valid': file_type != 'Unknown'
        }

# Example usage
processor = FileProcessor()
sample_png = b'\x89PNG\r\n\x1a\n' + b'fake_png_data' * 100
result = processor.process_upload(sample_png, 'image.png')
print(f"File processing result: {result}")

# Cryptographic Operations
class CryptoHandler:
    """Modern cryptographic operations with bytes"""
    
    def __init__(self):
        self.hasher = hashlib
    
    def hash_password(self, password: str, salt: bytes = None) -> tuple:
        """Hash password with salt"""
        if salt is None:
            salt = os.urandom(32)  # 32 bytes salt
        
        # Combine password and salt
        password_bytes = password.encode('utf-8')
        salted_password = salt + password_bytes
        
        # Hash using SHA-256
        hashed = self.hasher.sha256(salted_password).digest()
        
        return hashed, salt
    
    def verify_password(self, password: str, hashed: bytes, salt: bytes) -> bool:
        """Verify password against hash"""
        test_hash, _ = self.hash_password(password, salt)
        return test_hash == hashed
    
    def generate_token(self, length: int = 32) -> str:
        """Generate secure random token"""
        token_bytes = os.urandom(length)
        return token_bytes.hex()

# Example usage
crypto = CryptoHandler()
password = "secure_password_123"
hashed, salt = crypto.hash_password(password)
print(f"Password hashed: {hashed.hex()[:20]}...")
print(f"Salt: {salt.hex()[:20]}...")
print(f"Verification: {crypto.verify_password(password, hashed, salt)}")
print(f"Random token: {crypto.generate_token()}")

# Network Protocol Implementation
class HTTPParser:
    """Modern HTTP request parser using bytes"""
    
    def parse_request(self, raw_data: bytes) -> dict:
        """Parse HTTP request from bytes"""
        try:
            # Split headers and body
            if b'\r\n\r\n' in raw_data:
                headers_bytes, body_bytes = raw_data.split(b'\r\n\r\n', 1)
            else:
                headers_bytes = raw_data
                body_bytes = b''
            
            # Parse headers
            headers_str = headers_bytes.decode('utf-8')
            lines = headers_str.split('\r\n')
            
            # Parse request line
            request_line = lines[0]
            method, path, version = request_line.split()
            
            # Parse headers
            headers = {}
            for line in lines[1:]:
                if ':' in line:
                    key, value = line.split(':', 1)
                    headers[key.strip()] = value.strip()
            
            return {
                'method': method,
                'path': path,
                'version': version,
                'headers': headers,
                'body': body_bytes
            }
        except Exception as e:
            return {'error': str(e)}

# Example usage
parser = HTTPParser()
sample_request = b'GET /api/users HTTP/1.1\r\nHost: example.com\r\nUser-Agent: Python/3.9\r\n\r\n'
parsed = parser.parse_request(sample_request)
print(f"Parsed HTTP request: {parsed}")

# 2. BYTEARRAY TYPE - MODERN BACKEND APPLICATIONS
print("\n2. BYTEARRAY TYPE - MODERN BACKEND APPLICATIONS:")
print("="*49)

# Streaming Data Buffer
class StreamingBuffer:
    """Modern streaming data buffer using bytearray"""
    
    def __init__(self, initial_size: int = 1024):
        self.buffer = bytearray(initial_size)
        self.size = 0
        self.position = 0
    
    def write(self, data: bytes) -> int:
        """Write data to buffer"""
        data_len = len(data)
        required_size = self.size + data_len
        
        # Resize if needed
        if required_size > len(self.buffer):
            new_size = max(required_size, len(self.buffer) * 2)
            self.buffer.extend(bytearray(new_size - len(self.buffer)))
        
        # Write data
        self.buffer[self.size:self.size + data_len] = data
        self.size += data_len
        return data_len
    
    def read(self, size: int = None) -> bytes:
        """Read data from buffer"""
        if size is None:
            size = self.size - self.position
        
        actual_size = min(size, self.size - self.position)
        data = bytes(self.buffer[self.position:self.position + actual_size])
        self.position += actual_size
        return data
    
    def peek(self, size: int) -> bytes:
        """Peek at data without consuming it"""
        actual_size = min(size, self.size - self.position)
        return bytes(self.buffer[self.position:self.position + actual_size])
    
    def clear(self):
        """Clear buffer"""
        self.size = 0
        self.position = 0

# Example usage
buffer = StreamingBuffer()
buffer.write(b'Hello ')
buffer.write(b'World!')
print(f"Buffer content: {buffer.read()}")

# Image Processing with Bytearray
class ImageProcessor:
    """Modern image processing using bytearray"""
    
    def __init__(self):
        self.supported_formats = ['RGB', 'RGBA', 'GRAYSCALE']
    
    def create_image_buffer(self, width: int, height: int, format: str = 'RGB') -> bytearray:
        """Create image buffer"""
        channels = {'RGB': 3, 'RGBA': 4, 'GRAYSCALE': 1}
        if format not in channels:
            raise ValueError(f"Unsupported format: {format}")
        
        buffer_size = width * height * channels[format]
        return bytearray(buffer_size)
    
    def set_pixel(self, buffer: bytearray, x: int, y: int, width: int, 
                  color: tuple, format: str = 'RGB'):
        """Set pixel color in buffer"""
        channels = {'RGB': 3, 'RGBA': 4, 'GRAYSCALE': 1}
        channel_count = channels[format]
        
        index = (y * width + x) * channel_count
        for i, value in enumerate(color[:channel_count]):
            buffer[index + i] = value
    
    def get_pixel(self, buffer: bytearray, x: int, y: int, width: int, 
                  format: str = 'RGB') -> tuple:
        """Get pixel color from buffer"""
        channels = {'RGB': 3, 'RGBA': 4, 'GRAYSCALE': 1}
        channel_count = channels[format]
        
        index = (y * width + x) * channel_count
        return tuple(buffer[index:index + channel_count])
    
    def apply_filter(self, buffer: bytearray, filter_func):
        """Apply filter to image buffer"""
        for i in range(len(buffer)):
            buffer[i] = filter_func(buffer[i])

# Example usage
img_processor = ImageProcessor()
img_buffer = img_processor.create_image_buffer(100, 100, 'RGB')
img_processor.set_pixel(img_buffer, 50, 50, 100, (255, 0, 0))  # Red pixel
pixel = img_processor.get_pixel(img_buffer, 50, 50, 100)
print("Choose the right data type for your specific use case!")
# Code travelling in Machine
#  Electricity -> Electrons -> Dopants and SemiConductor Physics -> Transistors -> Logic Gates -> ALUs, Registers,Control Units -> Micro Code / Micro-Operations 
# -> Instructions Set Architecture -> CPU Architecture (Pipelines , caches , branch Predictors) -> Machine Code -> Bootloader / Firmware (e.g. BIOS/UEFI) -> OperatingSystem Kernel
# -> Device Drivers,Interrupt Handlers,Schedulers-> System Calls(SysCalls) -> C standard Library (libc) -> Language Runtimes (e.g. Java Virtual Machine, CPython (Compiled Python) , .NET CLR)
# -> Language Standard Libraries -> Frameworks(e.g. Django , NextJs, Qt) -> App Logic -> High-Level Languages (e.g. Python, Java, C++) -> Application Code-> UI/CLI/API ->User Interaction 
# or Client Requests 


