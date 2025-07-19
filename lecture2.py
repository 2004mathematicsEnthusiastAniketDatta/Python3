# REPL INTERNAL UNDERSTANDING - DEEP DIVE
# ==========================================

import sys
import code
import ast
import dis
import types
from typing import Any, Optional, Dict,Final
import traceback
import ctypes
import gc
import os
from dataclasses import dataclass
from typing import NamedTuple
import hashlib
import json
from datetime import datetime
import threading
from collections import defaultdict
import random
from typing import List, Optional
import json
import time
import math
import re
from datetime import datetime, timedelta

print("🐍 REPL (Read-Eval-Print Loop) - Internal Understanding")
print("="*60)

# REPL: Read-Eval-Print Loop
# ==========================
# A REPL is an interactive programming environment that processes user input in four stages:
# 1. READ: Parse user input from the console
# 2. EVAL: Compile and execute the parsed code
# 3. PRINT: Display the result (if any)
# 4. LOOP: Return to the READ stage

print("\n🔍 REPL ARCHITECTURE AND COMPONENTS")
print("="*40)

class SimplifiedREPL:
    """
    A simplified implementation showing REPL internals
    This demonstrates how Python's interactive shell works internally
    """
    
    def __init__(self):
        # Global namespace for storing variables and functions
        self.globals = {'__name__': '__main__', '__doc__': None}
        self.locals = self.globals  # In REPL, locals = globals
        self.command_count = 0
        
    def read_input(self, prompt=">>> ") -> str:
        """READ phase: Get input from user"""
        try:
            return input(prompt)
        except (EOFError, KeyboardInterrupt):
            return "exit()"
    
    def parse_and_compile(self, source: str) -> Optional[types.CodeType]:
        """Parse and compile the source code"""
        try:
            # First, try to compile as an expression
            return compile(source, '<stdin>', 'eval')
        except SyntaxError:
            try:
                # If that fails, try as a statement
                return compile(source, '<stdin>', 'exec')
            except SyntaxError as e:
                print(f"SyntaxError: {e}")
                return None
    
    def evaluate(self, code_obj: types.CodeType) -> Any:
        """EVAL phase: Execute the compiled code"""
        try:
            if code_obj.co_flags & 0x20:  # CO_GENERATOR flag
                # Handle generator expressions
                result = eval(code_obj, self.globals, self.locals)
            else:
                # Try evaluation first (for expressions)
                try:
                    result = eval(code_obj, self.globals, self.locals)
                except TypeError:
                    # If eval fails, it's a statement - use exec
                    exec(code_obj, self.globals, self.locals)
                    result = None
            return result
        except Exception as e:
            print(f"Error: {type(e).__name__}: {e}")
            return None
    
    def print_result(self, result: Any) -> None:
        """PRINT phase: Display the result"""
        if result is not None:
            print(repr(result))
            # Store the result in _ (like Python REPL)
            self.globals['_'] = result
    
    def repl_loop(self):
        """Main REPL loop"""
        print("Simplified Python REPL (type 'exit()' to quit)")
        
        while True:
            try:
                # READ
                source = self.read_input()
                
                if source.strip() in ['exit()', 'quit()']:
                    break
                
                if not source.strip():
                    continue
                
                self.command_count += 1
                
                # COMPILE
                code_obj = self.parse_and_compile(source)
                if code_obj is None:
                    continue
                
                # EVAL
                result = self.evaluate(code_obj)
                
                # PRINT
                self.print_result(result)
                
                # LOOP (implicit - continue to next iteration)
                
            except KeyboardInterrupt:
                print("\nKeyboardInterrupt")
            except EOFError:
                print("\nExiting...")
                break

# Demonstrate REPL components
print("\n📋 REPL INTERNAL COMPONENTS:")
print("-" * 30)

# 1. Parser and Compiler
print("\n1. PARSING AND COMPILATION:")
source_code = "2 + 3 * 4"
print(f"Source: {source_code}")

# Parse into Abstract Syntax Tree (AST)
parsed_ast = ast.parse(source_code, mode='eval')
print(f"AST: {ast.dump(parsed_ast)}")

# Compile to bytecode
compiled_code = compile(source_code, '<string>', 'eval')
print(f"Code Object: {compiled_code}")

# Show bytecode
print("Bytecode:")
dis.dis(compiled_code)

print("\n2. EVALUATION CONTEXT:")
# Global and local namespaces
repl_globals = {'__name__': '__main__'}
repl_locals = repl_globals

# Evaluate the expression
result = eval(compiled_code, repl_globals, repl_locals)
print(f"Result: {result}")

print("\n3. NAMESPACE MANAGEMENT:")
# Variables persist across REPL commands
exec("x = 10", repl_globals, repl_locals)
exec("y = x * 2", repl_globals, repl_locals)
result = eval("x + y", repl_globals, repl_locals)
print(f"x + y = {result}")
print(f"Namespace contents: {list(repl_globals.keys())}")

print("\n🔧 ADVANCED REPL FEATURES:")
print("="*30)

# 1. Multi-line input handling
print("\n1. MULTI-LINE INPUT DETECTION:")
def is_complete_statement(source: str) -> bool:
    """Check if the source code is a complete statement"""
    try:
        compile(source, '<stdin>', 'exec')
        return True
    except SyntaxError as e:
        if 'unexpected EOF' in str(e) or 'incomplete input' in str(e):
            return False
        return True

# Examples
examples = [
    "def foo():",
    "def foo():\n    pass",
    "if True:",
    "if True:\n    print('hello')"
]

for example in examples:
    complete = is_complete_statement(example)
    print(f"'{repr(example)}' -> Complete: {complete}")

print("\n2. SPECIAL REPL VARIABLES:")
# Python REPL maintains special variables
special_vars = {
    '_': 'Last expression result',
    '__': 'Second-to-last expression result', 
    '___': 'Third-to-last expression result'
}

for var, desc in special_vars.items():
    print(f"{var}: {desc}")

print("\n3. ERROR HANDLING AND RECOVERY:")
def safe_eval(source: str, globals_dict: dict, locals_dict: dict):
    """Safely evaluate code with error handling"""
    try:
        code_obj = compile(source, '<stdin>', 'eval')
        return eval(code_obj, globals_dict, locals_dict)
    except SyntaxError:
        try:
            code_obj = compile(source, '<stdin>', 'exec')
            exec(code_obj, globals_dict, locals_dict)
            return None
        except Exception as e:
            return f"Error: {e}"
    except Exception as e:
        return f"Error: {e}"

# Test error handling
test_cases = [
    "2 + 3",           # Valid expression
    "x = 5",           # Valid statement
    "2 +",             # Syntax error
    "undefined_var",   # Runtime error
]

test_globals = {}
for case in test_cases:
    result = safe_eval(case, test_globals, test_globals)
    print(f"'{case}' -> {result}")

print("\n🏗️ REPL IMPLEMENTATION DETAILS:")
print("="*35)

print("\n1. PYTHON'S CODE MODULE:")
print("Python's REPL is implemented using the 'code' module")
print("Key components:")
print("- InteractiveConsole class")
print("- InteractiveInterpreter class") 
print("- compile_command() function")

print("\n2. BYTECODE EXECUTION:")
print("REPL compiles source -> bytecode -> executes on Python VM")

# Show how Python's real REPL works
print("\n3. REAL REPL BEHAVIOR:")
print("$ python")
print("Python 3.x.x")
print(">>> 2 + 3")
print("5")
print(">>> x = 10")
print(">>> x * 2")
print("20")
print(">>> _")
print("20")

print("\n🎯 REPL USE CASES:")
print("="*20)
use_cases = [
    "Interactive Development: Test code snippets quickly",
    "Debugging: Inspect variables and test fixes",
    "Learning: Experiment with language features",
    "Data Exploration: Analyze data interactively",
    "Prototyping: Develop and test algorithms",
    "System Administration: Execute system commands",
    "API Testing: Test API calls and responses"
]

for i, case in enumerate(use_cases, 1):
    print(f"{i}. {case}")

print("\n⚡ ENHANCED REPLs:")
print("="*20)
enhanced_repls = {
    "IPython": "Enhanced interactive shell with magic commands, better tab completion",
    "Jupyter": "Web-based interactive computing environment",
    "bpython": "Fancy interface with syntax highlighting and auto-completion", 
    "ptpython": "Better Python REPL with syntax highlighting"
}

for name, desc in enhanced_repls.items():
    print(f"• {name}: {desc}")

print("\n🔍 REPL INTERNALS SUMMARY:")
print("="*30)
summary_points = [
    "REPL = Interactive loop of Read → Eval → Print → Loop",
    "Uses Python's compile() and eval()/exec() functions",
    "Maintains persistent namespace across commands",
    "Handles both expressions and statements differently", 
    "Implements error recovery and multi-line input detection",
    "Foundation for advanced interactive environments",
    "Essential for rapid prototyping and learning"
]

for point in summary_points:
    print(f"✓ {point}")

print("\n" + "="*60)
print("End of REPL Internal Understanding")
print("="*60)

# Variable is a symbolic name or identifier that is used to refer to a value or data stored in memory.
# Variable is a symbolic name or identifier that is used to refer to a value or data stored in memory.
# When we write "a=10", here's what happens at different levels:

print("\n🔬 VARIABLE ASSIGNMENT: MULTI-LEVEL ANALYSIS")
print("="*50)


print("\n1. PYTHON LEVEL (High-Level)")
print("-" * 30)
a = 10
print(f"Python statement: a = 10")
print(f"Variable 'a' refers to object with value: {a}")
print(f"Object type: {type(a)}")
print(f"Object id (memory address): {id(a)}")

print("\n2. PYTHON OBJECT LEVEL (Internal Representation)")
print("-" * 45)
print(f"Reference count for object 10: {sys.getrefcount(a) - 1}")  # -1 for temporary ref
print(f"Object size in bytes: {sys.getsizeof(a)}")

# Show memory layout of Python integer object
print("\nPython Integer Object Structure:")
print("┌─────────────────┐")
print("│ PyObject_HEAD   │  <- Reference count + type pointer")
print("│ ob_digit[]      │  <- Actual integer value storage")
print("└─────────────────┘")

# Multiple references to same object
b = a
c = 10
print(f"\nAfter b = a and c = 10:")
print(f"id(a): {id(a)}")
print(f"id(b): {id(b)}")
print(f"id(c): {id(c)}")
print(f"a is b: {a is b}")
print(f"a is c: {a is c}")
print(f"Reference count now: {sys.getrefcount(a) - 1}")

print("\n3. MEMORY MANAGEMENT LEVEL")
print("-" * 30)

# Python's memory allocator hierarchy
print("Python Memory Allocator Hierarchy:")
print("┌─────────────────────────────┐")
print("│ Python Objects (PyMalloc)   │  <- Small objects (<= 512 bytes)")
print("├─────────────────────────────┤")
print("│ Raw Memory Interface        │  <- malloc/free wrapper")
print("├─────────────────────────────┤") 
print("│ Operating System            │  <- Virtual memory pages")
print("└─────────────────────────────┘")

# Show memory arena information
print(f"\nProcess memory info:")
print(f"Process ID: {os.getpid()}")

# Get memory address as raw pointer
memory_address = id(a)
print(f"Memory address of object: 0x{memory_address:x}")

# Try to access raw memory (dangerous - for demonstration only)
try:
    # Read the first few bytes of the Python object
    raw_bytes = ctypes.string_at(memory_address, 32)
    print(f"Raw memory bytes (first 32): {raw_bytes.hex()}")
except:
    print("Raw memory access not available (protected)")

print("\n4. VIRTUAL MEMORY LEVEL (OS Level)")
print("-" * 35)

# Virtual memory concepts
print("Virtual Memory Management:")
print("• Python process has virtual address space")
print("• Virtual addresses mapped to physical RAM")
print("• Page-based memory allocation (typically 4KB pages)")
print("• Memory protection and isolation")

# Show virtual memory regions
print(f"\nVirtual Memory Regions:")
print("┌─────────────────┐ High addresses")
print("│ Stack           │ <- Function calls, local variables")
print("├─────────────────┤")
print("│ Heap            │ <- Dynamic allocation (Python objects)")
print("├─────────────────┤")
print("│ Data Segment    │ <- Global variables, constants")
print("├─────────────────┤")
print("│ Text Segment    │ <- Program code (Python interpreter)")
print("└─────────────────┘ Low addresses")

# Memory allocation demonstration
large_list = [i for i in range(1000)]
print(f"\nAfter allocating large list:")
print(f"List memory size: {sys.getsizeof(large_list)} bytes")
print(f"List memory address: 0x{id(large_list):x}")

print("\n5. KERNEL LEVEL")
print("-" * 15)

print("Kernel Memory Management:")
print("• Page tables map virtual → physical addresses")
print("• Memory Management Unit (MMU) handles translation")
print("• Kernel allocates physical pages on demand")
print("• Copy-on-write optimization for shared pages")
print("• Swapping to disk when RAM is full")

print("\nSystem Calls involved:")
print("• mmap(): Map memory regions")
print("• brk()/sbrk(): Adjust heap size") 
print("• munmap(): Unmap memory regions")

print("\n6. HARDWARE LEVEL")
print("-" * 18)

print("CPU and Memory Hardware:")
print("• CPU registers store immediate values and addresses")
print("• L1/L2/L3 cache hierarchy for fast access")
print("• RAM (DRAM) stores actual data")
print("• Memory controller manages RAM access")
print("• MMU translates virtual to physical addresses")

print("\nHardware Memory Hierarchy:")
print("┌─────────────────┐ Fastest")
print("│ CPU Registers   │ ~1 cycle")
print("├─────────────────┤")
print("│ L1 Cache        │ ~2-4 cycles")
print("├─────────────────┤")
print("│ L2 Cache        │ ~10-20 cycles")
print("├─────────────────┤")
print("│ L3 Cache        │ ~40-75 cycles")
print("├─────────────────┤")
print("│ Main Memory     │ ~200+ cycles")
print("└─────────────────┘ Slowest")

print("\n7. COMPLETE ASSIGNMENT FLOW")
print("-" * 30)

print("When 'a = 10' is executed:")
print("\n🐍 Python Level:")
print("  1. Parser creates AST for assignment")
print("  2. Compiler generates STORE_NAME bytecode")
print("  3. Check if integer 10 object exists in cache")
print("  4. If not, create new PyLongObject")
print("  5. Store reference in local namespace")

print("\n🧠 Memory Level:")
print("  1. PyMalloc requests memory from arena")
print("  2. If arena full, request new block from OS")
print("  3. Initialize object header (refcount, type)")
print("  4. Store integer value in ob_digit array")

print("\n💻 OS Level:")
print("  1. Handle page fault if memory not mapped")
print("  2. Allocate physical page if needed")
print("  3. Update page tables")
print("  4. Set memory protection bits")

print("\n⚡ Hardware Level:")
print("  1. CPU executes memory store instruction")
print("  2. MMU translates virtual to physical address")
print("  3. Check cache hierarchy")
print("  4. Write to memory controller")
print("  5. Store in DRAM cells")

# Demonstrate reference semantics
print("\n8. REFERENCE VS VALUE SEMANTICS")
print("-" * 35)

# Immutable objects (integers) - identity sharing
x = 256
y = 256
print(f"x = 256, y = 256")
print(f"x is y: {x is y} (small integers cached)")

x = 1000  
y = 1000
print(f"x = 1000, y = 1000")
print(f"x is y: {x is y} (large integers not cached)")

# Mutable objects - new objects created
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(f"list1 = [1,2,3], list2 = [1,2,3]")
print(f"list1 is list2: {list1 is list2} (different objects)")

print("\n" + "="*50)
print("Variable assignment involves ALL system levels!")
print("="*50)

# Immutable and Mutable Objects

print("\n🔒 IMMUTABLE AND MUTABLE OBJECTS")

x1:Final = 42
x2:Final = 42.0
print(f"x1: {x1}")
print(f"x2: {x2}")
print(f"x1 is x2: {x1 is x2}")
print(id(x1), id(x2))

print("\n🏗️ IMMUTABLE AND MUTABLE OBJECTS IN BACKEND DEVELOPMENT")
print("="*60)

print("\n1. DATABASE CONFIGURATIONS (Immutable)")
print("-" * 40)


# Immutable database configuration using NamedTuple
class DatabaseConfig(NamedTuple):
    host: str
    port: int
    database: str
    username: str
    password: str
    pool_size: int = 10
    
    def get_connection_string(self) -> str:
        return f"postgresql://{self.username}:{self.password}@{self.host}:{self.port}/{self.database}"
    
    def with_password(self, new_password: str) -> 'DatabaseConfig':
        """Create new config with different password"""
        return self._replace(password=new_password)

# Usage in backend
prod_db = DatabaseConfig(
    host="prod-db.company.com",
    port=5432,
    database="production",
    username="app_user",
    password="secure_password123"
)

dev_db = prod_db._replace(host="localhost", database="development")

print(f"Production DB: {prod_db.host}:{prod_db.port}")
print(f"Development DB: {dev_db.host}:{dev_db.port}")
print(f"Same object? {prod_db is dev_db}")

print("\n2. API RESPONSE CACHING (Immutable Keys)")
print("-" * 40)

# Cache with immutable keys for thread safety
class APICache:
    def __init__(self):
        self._cache = {}
    
    def _make_cache_key(self, endpoint: str, params: dict) -> tuple:
        """Create immutable cache key from mutable params"""
        # Sort items to ensure consistent key
        return (endpoint, tuple(sorted(params.items())))
    
    def get(self, endpoint: str, params: dict):
        key = self._make_cache_key(endpoint, params)
        return self._cache.get(key)
    
    def set(self, endpoint: str, params: dict, response):
        key = self._make_cache_key(endpoint, params)
        self._cache[key] = response

# Usage
api_cache = APICache()
params = {"user_id": 123, "limit": 10}
api_cache.set("/api/users", params, {"users": ["user1", "user2"]})

# Even if original params dict is modified, cache key remains valid
params["limit"] = 20  # This doesn't affect cached entry
cached_result = api_cache.get("/api/users", {"user_id": 123, "limit": 10})
print(f"Cached result: {cached_result}")

print("\n3. USER SESSION MANAGEMENT (Mixed Approach)")
print("-" * 45)

@dataclass(frozen=True)
class UserProfile:
    """Immutable user profile - core identity data"""
    user_id: int
    username: str
    email: str
    role: str
    created_at: datetime
    
    def __post_init__(self):
        # Validate immutable data
        if not self.email or '@' not in self.email:
            raise ValueError("Invalid email")

class UserSession:
    """Mutable session state"""
    def __init__(self, profile: UserProfile):
        self.profile = profile  # Immutable reference
        self.login_time = datetime.now()
        self.last_activity = datetime.now()
        self.permissions = set()  # Mutable
        self.preferences = {}     # Mutable
        self.session_data = {}    # Mutable
    
    def update_activity(self):
        self.last_activity = datetime.now()
    
    def add_permission(self, permission: str):
        self.permissions.add(permission)
    
    def set_preference(self, key: str, value):
        self.preferences[key] = value

# Backend usage
user_profile = UserProfile(
    user_id=12345,
    username="john_doe",
    email="john@company.com",
    role="developer",
    created_at=datetime(2023, 1, 15)
)

session = UserSession(user_profile)
session.add_permission("read_code")
session.add_permission("write_code")
session.set_preference("theme", "dark")

print(f"User: {session.profile.username}")
print(f"Permissions: {session.permissions}")
print(f"Profile is immutable - ID: {id(session.profile)}")

# Cannot modify profile
try:
    session.profile.username = "hacker"  # This will fail
except AttributeError as e:
    print(f"✓ Profile protection: {e}")

print("\n4. CONFIGURATION MANAGEMENT (Environment-based)")
print("-" * 50)

@dataclass(frozen=True)
class ServerConfig:
    """Immutable server configuration"""
    environment: str
    debug: bool
    secret_key: str
    database_url: str
    redis_url: str
    log_level: str
    allowed_hosts: tuple  # Immutable sequence
    
    @classmethod
    def from_environment(cls, env: str) -> 'ServerConfig':
        configs = {
            'development': cls(
                environment='development',
                debug=True,
                secret_key='dev-secret-key',
                database_url='sqlite:///dev.db',
                redis_url='redis://localhost:6379/0',
                log_level='DEBUG',
                allowed_hosts=('localhost', '127.0.0.1')
            ),
            'production': cls(
                environment='production',
                debug=False,
                secret_key='prod-secret-key-very-secure',
                database_url='postgresql://prod-db:5432/app',
                redis_url='redis://prod-redis:6379/0',
                log_level='WARNING',
                allowed_hosts=('api.company.com', 'app.company.com')
            )
        }
        return configs[env]

# Configuration is immutable and thread-safe
config = ServerConfig.from_environment('development')
print(f"Environment: {config.environment}")
print(f"Debug mode: {config.debug}")
print(f"Allowed hosts: {config.allowed_hosts}")

print("\n5. REQUEST/RESPONSE HANDLING")
print("-" * 30)

class HTTPRequest:
    """Mutable request object"""
    def __init__(self, method: str, path: str, headers: dict):
        self.method = method
        self.path = path
        self.headers = headers.copy()  # Defensive copy
        self.body = None
        self.query_params = {}
        self.user = None
        self.session = None
    
    def add_header(self, key: str, value: str):
        self.headers[key] = value
    
    def set_user(self, user):
        self.user = user

@dataclass(frozen=True)
class HTTPResponse:
    """Immutable response object"""
    status_code: int
    headers: dict
    body: str
    
    def with_header(self, key: str, value: str) -> 'HTTPResponse':
        """Return new response with additional header"""
        new_headers = self.headers.copy()
        new_headers[key] = value
        return HTTPResponse(self.status_code, new_headers, self.body)

# Backend request handling
request = HTTPRequest('GET', '/api/users', {'Content-Type': 'application/json'})
request.set_user(user_profile)

response = HTTPResponse(
    status_code=200,
    headers={'Content-Type': 'application/json'},
    body='{"users": []}'
)

# Add security header without mutating original
secured_response = response.with_header('X-Frame-Options', 'DENY')
print(f"Original response headers: {len(response.headers)}")
print(f"Secured response headers: {len(secured_response.headers)}")

print("\n6. THREAD-SAFE SHARED STATE")
print("-" * 30)


class MetricsCollector:
    """Thread-safe metrics using immutable updates"""
    def __init__(self):
        self._metrics = {}
        self._lock = threading.Lock()
    
    def increment_counter(self, name: str, value: int = 1):
        with self._lock:
            current = self._metrics.get(name, 0)
            # Create new immutable value
            self._metrics[name] = current + value
    
    def get_snapshot(self) -> dict:
        """Return immutable snapshot"""
        with self._lock:
            return dict(self._metrics)  # Defensive copy

# Global metrics instance
metrics = MetricsCollector()

def simulate_api_call(endpoint: str):
    """Simulate API call recording metrics"""
    metrics.increment_counter(f"api.{endpoint}.requests")
    # Simulate some processing
    if random.random() > 0.8:
        metrics.increment_counter(f"api.{endpoint}.errors")

# Simulate concurrent API calls
threads = []
for i in range(10):
    thread = threading.Thread(target=simulate_api_call, args=("users",))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(f"Final metrics: {metrics.get_snapshot()}")

print("\n7. DATA VALIDATION AND SERIALIZATION")
print("-" * 40)


@dataclass(frozen=True)
class Product:
    """Immutable product data"""
    id: int
    name: str
    price: float
    category: str
    in_stock: bool
    
    def __post_init__(self):
        if self.price < 0:
            raise ValueError("Price cannot be negative")
    
    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'category': self.category,
            'in_stock': self.in_stock
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> 'Product':
        return cls(**data)

class ShoppingCart:
    """Mutable shopping cart"""
    def __init__(self):
        self.items: List[Product] = []
        self.total = 0.0
        self.created_at = datetime.now()
    
    def add_product(self, product: Product, quantity: int = 1):
        for _ in range(quantity):
            self.items.append(product)  # Immutable products
        self._recalculate_total()
    
    def _recalculate_total(self):
        self.total = sum(item.price for item in self.items)
    
    def to_json(self) -> str:
        data = {
            'items': [item.to_dict() for item in self.items],
            'total': self.total,
            'created_at': self.created_at.isoformat()
        }
        return json.dumps(data, indent=2)

# Usage in e-commerce backend
laptop = Product(1, "Gaming Laptop", 1299.99, "Electronics", True)
mouse = Product(2, "Wireless Mouse", 29.99, "Electronics", True)

cart = ShoppingCart()
cart.add_product(laptop)
cart.add_product(mouse, quantity=2)

print(f"Cart total: ${cart.total:.2f}")
print("Cart JSON:")
print(cart.to_json())

print("\n8. BEST PRACTICES SUMMARY")
print("-" * 30)

practices = [
    "✓ Use immutable objects for configuration and constants",
    "✓ Immutable data structures for cache keys and identifiers", 
    "✓ Mutable objects for session state and request handling",
    "✓ Defensive copying when exposing internal mutable state",
    "✓ Thread-safe patterns with immutable updates",
    "✓ Validation in immutable object constructors",
    "✓ Factory methods for environment-specific configs",
    "✓ Immutable response objects with builder pattern"
]

for practice in practices:
    print(practice)

print("\n9. PERFORMANCE IMPLICATIONS")
print("-" * 30)

# Memory usage comparison

# Immutable tuple vs mutable list
data_tuple = tuple(range(1000))
data_list = list(range(1000))

print(f"Tuple memory: {sys.getsizeof(data_tuple)} bytes")
print(f"List memory: {sys.getsizeof(data_list)} bytes")
print(f"Memory difference: {sys.getsizeof(data_list) - sys.getsizeof(data_tuple)} bytes")

# Hash-based lookups with immutable keys
cache_dict = {
    ("users", frozenset([("limit", 10)])): "cached_users",
    ("products", frozenset([("category", "electronics")])): "cached_products"
}

lookup_key = ("users", frozenset([("limit", 10)]))
print(f"Cache lookup: {cache_dict.get(lookup_key)}")

print("\n" + "="*60)
print("Immutable/Mutable patterns are crucial for backend reliability!")
print("="*60)

# id function - id(): 
# The id() function in python returns the unique memory address of an object. This memory address is constant for the object as long as this exists .
# Every Object created in Python has a unique id.
# The id() function returns the identity of an object. This identity is unique and constant for this object during its lifetime.
# key points:
# Each object in Python has a unique id , representating its location in memory.
# When two variables point to the same object , their IDs will be the same.

print("\n🏢 INDUSTRY APPLICATIONS OF id() FUNCTION")
print("="*50)

print("\n1. MEMORY LEAK DETECTION IN WEB APPLICATIONS")
print("-" * 45)

class MemoryLeakDetector:
    """Detect potential memory leaks by tracking object IDs"""
    
    def __init__(self):
        self.tracked_objects = defaultdict(list)
        self.object_counts = defaultdict(int)
    
    def track_object(self, obj, context: str):
        """Track an object's ID and context"""
        obj_id = id(obj)
        obj_type = type(obj).__name__
        
        self.tracked_objects[obj_type].append({
            'id': obj_id,
            'context': context,
            'timestamp': datetime.now(),
            'size': sys.getsizeof(obj)
        })
        
        self.object_counts[obj_type] += 1
    
    def check_for_leaks(self):
        """Report potential memory leaks"""
        print("Memory Leak Analysis:")
        for obj_type, count in self.object_counts.items():
            if count > 100:  # Threshold for concern
                print(f"⚠️  {obj_type}: {count} instances (potential leak)")
                recent_objects = self.tracked_objects[obj_type][-5:]
                for obj_info in recent_objects:
                    print(f"   ID: {obj_info['id']}, Context: {obj_info['context']}")

# Simulate web application with memory tracking
leak_detector = MemoryLeakDetector()

class WebRequest:
    def __init__(self, path: str, data: dict):
        self.path = path
        self.data = data
        self.created_at = datetime.now()

# Simulate processing requests
for i in range(150):
    request = WebRequest(f"/api/endpoint/{i}", {"data": f"request_{i}"})
    leak_detector.track_object(request, f"API_REQUEST_{i}")

leak_detector.check_for_leaks()

print("\n2. DATABASE CONNECTION POOL MONITORING")
print("-" * 40)

class DatabaseConnectionPool:
    """Monitor database connections using object IDs"""
    
    def __init__(self, max_connections: int = 10):
        self.max_connections = max_connections
        self.active_connections = {}
        self.connection_history = []
    
    def create_connection(self, user_id: str):
        """Create a new database connection"""
        if len(self.active_connections) >= self.max_connections:
            raise Exception("Connection pool exhausted")
        
        # Simulate connection object
        connection = {"host": "db.example.com", "user": user_id}
        conn_id = id(connection)
        
        self.active_connections[conn_id] = {
            'connection': connection,
            'user_id': user_id,
            'created_at': datetime.now(),
            'last_used': datetime.now()
        }
        
        self.connection_history.append({
            'action': 'CREATED',
            'conn_id': conn_id,
            'user_id': user_id,
            'timestamp': datetime.now()
        })
        
        print(f"Connection created for {user_id}: ID {conn_id}")
        return connection
    
    def close_connection(self, connection):
        """Close a database connection"""
        conn_id = id(connection)
        if conn_id in self.active_connections:
            user_id = self.active_connections[conn_id]['user_id']
            del self.active_connections[conn_id]
            
            self.connection_history.append({
                'action': 'CLOSED',
                'conn_id': conn_id,
                'user_id': user_id,
                'timestamp': datetime.now()
            })
            
            print(f"Connection closed for {user_id}: ID {conn_id}")
        else:
            print(f"⚠️  Attempted to close unknown connection: ID {conn_id}")
    
    def get_pool_status(self):
        """Get current pool status"""
        active_count = len(self.active_connections)
        print(f"Pool Status: {active_count}/{self.max_connections} connections active")
        
        for conn_id, info in self.active_connections.items():
            print(f"  ID {conn_id}: User {info['user_id']}, Age: {datetime.now() - info['created_at']}")

# Database connection pool usage
db_pool = DatabaseConnectionPool(max_connections=5)

# Simulate multiple users connecting
users = ["user1", "user2", "user3"]
connections = []

for user in users:
    conn = db_pool.create_connection(user)
    connections.append(conn)

db_pool.get_pool_status()

# Close some connections
db_pool.close_connection(connections[1])
db_pool.get_pool_status()

print("\n3. CACHING SYSTEM IMPLEMENTATION")
print("-" * 35)

class SmartCache:
    """Cache implementation using object IDs for integrity"""
    
    def __init__(self, max_size: int = 1000):
        self.cache = {}
        self.access_times = {}
        self.object_metadata = {}
        self.max_size = max_size
    
    def _generate_cache_key(self, obj) -> str:
        """Generate cache key using object ID and hash"""
        obj_id = id(obj)
        obj_hash = hash(str(obj)) if hasattr(obj, '__hash__') else hash(str(obj))
        return f"{obj_id}_{obj_hash}"
    
    def cache_object(self, obj, computed_result, operation: str):
        """Cache the result of an expensive operation"""
        cache_key = self._generate_cache_key(obj)
        
        if len(self.cache) >= self.max_size:
            self._evict_lru()
        
        self.cache[cache_key] = {
            'result': computed_result,
            'original_object_id': id(obj),
            'operation': operation,
            'cached_at': datetime.now()
        }
        
        self.access_times[cache_key] = datetime.now()
        self.object_metadata[cache_key] = {
            'object_type': type(obj).__name__,
            'object_size': sys.getsizeof(obj)
        }
        
        print(f"Cached {operation} result for object ID {id(obj)}")
    
    def get_cached_result(self, obj, operation: str):
        """Retrieve cached result if available"""
        cache_key = self._generate_cache_key(obj)
        
        if cache_key in self.cache:
            cached_data = self.cache[cache_key]
            
            # Verify object integrity
            if cached_data['original_object_id'] == id(obj):
                self.access_times[cache_key] = datetime.now()
                print(f"Cache HIT for {operation} on object ID {id(obj)}")
                return cached_data['result']
            else:
                print(f"Cache MISS: Object ID mismatch for {operation}")
                del self.cache[cache_key]
                return None
        
        print(f"Cache MISS for {operation} on object ID {id(obj)}")
        return None
    
    def _evict_lru(self):
        """Evict least recently used item"""
        if not self.access_times:
            return
        
        oldest_key = min(self.access_times.keys(), key=lambda k: self.access_times[k])
        del self.cache[oldest_key]
        del self.access_times[oldest_key]
        del self.object_metadata[oldest_key]
        print(f"Evicted LRU cache entry: {oldest_key}")
    
    def get_cache_stats(self):
        """Get cache statistics"""
        print(f"Cache Statistics:")
        print(f"  Total entries: {len(self.cache)}")
        print(f"  Total size: {sum(self.object_metadata[k]['object_size'] for k in self.cache.keys())} bytes")
        
        type_counts = defaultdict(int)
        for metadata in self.object_metadata.values():
            type_counts[metadata['object_type']] += 1
        
        print("  Objects by type:")
        for obj_type, count in type_counts.items():
            print(f"    {obj_type}: {count}")

# Smart cache usage
cache = SmartCache(max_size=10)

# Expensive computation function
def expensive_computation(data_list):
    """Simulate expensive computation"""
    time.sleep(0.01)  # Simulate processing time
    return sum(data_list) * 2

# Test caching
test_data1 = [1, 2, 3, 4, 5]
test_data2 = [10, 20, 30]

# First computation (cache miss)
result1 = cache.get_cached_result(test_data1, "expensive_computation")
if result1 is None:
    result1 = expensive_computation(test_data1)
    cache.cache_object(test_data1, result1, "expensive_computation")

# Second computation (cache hit)
result1_cached = cache.get_cached_result(test_data1, "expensive_computation")

cache.get_cache_stats()

print("\n4. OBJECT LIFECYCLE TRACKING IN FRAMEWORKS")
print("-" * 45)

class ObjectLifecycleTracker:
    """Track object creation, modification, and destruction"""
    
    def __init__(self):
        self.lifecycle_events = defaultdict(list)
        self.object_registry = {}
    
    def register_object(self, obj, name: str, context: str):
        """Register object creation"""
        obj_id = id(obj)
        event = {
            'event': 'CREATED',
            'timestamp': datetime.now(),
            'context': context,
            'object_type': type(obj).__name__,
            'memory_address': hex(obj_id)
        }
        
        self.lifecycle_events[obj_id].append(event)
        self.object_registry[obj_id] = {
            'name': name,
            'object': obj,  # Keep weak reference in real implementation
            'created_at': datetime.now()
        }
        
        print(f"Registered {name} (ID: {obj_id}) in context: {context}")
    
    def track_modification(self, obj, operation: str, details: str):
        """Track object modification"""
        obj_id = id(obj)
        event = {
            'event': 'MODIFIED',
            'operation': operation,
            'details': details,
            'timestamp': datetime.now()
        }
        
        self.lifecycle_events[obj_id].append(event)
        print(f"Tracked modification on ID {obj_id}: {operation}")
    
    def track_destruction(self, obj_id: int, context: str):
        """Track object destruction"""
        event = {
            'event': 'DESTROYED',
            'timestamp': datetime.now(),
            'context': context
        }
        
        self.lifecycle_events[obj_id].append(event)
        
        if obj_id in self.object_registry:
            name = self.object_registry[obj_id]['name']
            del self.object_registry[obj_id]
            print(f"Tracked destruction of {name} (ID: {obj_id})")
    
    def get_object_history(self, obj):
        """Get complete history of an object"""
        obj_id = id(obj)
        history = self.lifecycle_events.get(obj_id, [])
        
        print(f"Object History for ID {obj_id}:")
        for event in history:
            print(f"  {event['timestamp']}: {event['event']}")
            if 'operation' in event:
                print(f"    Operation: {event['operation']}")
            if 'details' in event:
                print(f"    Details: {event['details']}")
    
    def generate_lifecycle_report(self):
        """Generate comprehensive lifecycle report"""
        print("Object Lifecycle Report:")
        print("-" * 25)
        
        total_objects = len(self.lifecycle_events)
        active_objects = len(self.object_registry)
        destroyed_objects = total_objects - active_objects
        
        print(f"Total objects tracked: {total_objects}")
        print(f"Currently active: {active_objects}")
        print(f"Destroyed objects: {destroyed_objects}")
        
        print("\nActive Objects:")
        for obj_id, info in self.object_registry.items():
            age = datetime.now() - info['created_at']
            print(f"  {info['name']} (ID: {obj_id}): Age {age}")

# Object lifecycle tracking usage
tracker = ObjectLifecycleTracker()

# Simulate web application objects
class UserSession:
    def __init__(self, user_id: str):
        self.user_id = user_id
        self.data = {}
        self.created_at = datetime.now()
    
    def update_data(self, key: str, value):
        self.data[key] = value

# Track user sessions
session1 = UserSession("user123")
tracker.register_object(session1, "UserSession_123", "user_login")

session2 = UserSession("user456")
tracker.register_object(session2, "UserSession_456", "user_login")

# Track modifications
session1.update_data("last_page", "/dashboard")
tracker.track_modification(session1, "DATA_UPDATE", "Updated last_page")

session1.update_data("preferences", {"theme": "dark"})
tracker.track_modification(session1, "DATA_UPDATE", "Updated preferences")

# Get object history
tracker.get_object_history(session1)

# Generate report
tracker.generate_lifecycle_report()

# Simulate session destruction
session1_id = id(session1)
del session1  # In real app, this might be garbage collected
tracker.track_destruction(session1_id, "user_logout")

print("\n5. DISTRIBUTED SYSTEM OBJECT SYNCHRONIZATION")
print("-" * 45)

class DistributedObjectManager:
    """Manage objects across distributed systems using IDs"""
    
    def __init__(self, node_id: str):
        self.node_id = node_id
        self.local_objects = {}
        self.remote_object_refs = {}
        self.sync_log = []
    
    def create_distributed_object(self, obj, global_key: str):
        """Create object with distributed tracking"""
        local_id = id(obj)
        distributed_id = f"{self.node_id}_{local_id}_{hash(global_key)}"
        
        self.local_objects[distributed_id] = {
            'object': obj,
            'local_id': local_id,
            'global_key': global_key,
            'created_at': datetime.now(),
            'version': 1,
            'synchronized': False
        }
        
        self.sync_log.append({
            'action': 'CREATE',
            'distributed_id': distributed_id,
            'timestamp': datetime.now(),
            'node_id': self.node_id
        })
        
        print(f"Created distributed object: {distributed_id}")
        return distributed_id
    
    def sync_object_with_remote(self, distributed_id: str, remote_node: str):
        """Simulate synchronization with remote node"""
        if distributed_id in self.local_objects:
            obj_info = self.local_objects[distributed_id]
            
            # Simulate sending object data to remote node
            sync_data = {
                'distributed_id': distributed_id,
                'local_id': obj_info['local_id'],
                'global_key': obj_info['global_key'],
                'version': obj_info['version'],
                'data_hash': hash(str(obj_info['object'])),
                'source_node': self.node_id,
                'target_node': remote_node
            }
            
            obj_info['synchronized'] = True
            obj_info['version'] += 1
            
            self.sync_log.append({
                'action': 'SYNC',
                'distributed_id': distributed_id,
                'target_node': remote_node,
                'timestamp': datetime.now()
            })
            
            print(f"Synchronized {distributed_id} with node {remote_node}")
            return sync_data
        
        return None
    
    def get_synchronization_status(self):
        """Get synchronization status report"""
        print(f"Node {self.node_id} Synchronization Status:")
        print("-" * 35)
        
        total_objects = len(self.local_objects)
        synced_objects = sum(1 for obj in self.local_objects.values() if obj['synchronized'])
        
        print(f"Total objects: {total_objects}")
        print(f"Synchronized objects: {synced_objects}")
        print(f"Pending sync: {total_objects - synced_objects}")
        
        print("\nObject Details:")
        for dist_id, obj_info in self.local_objects.items():
            status = "SYNCED" if obj_info['synchronized'] else "LOCAL"
            print(f"  {dist_id}: {status} (v{obj_info['version']})")

# Distributed system simulation
node_manager = DistributedObjectManager("NODE_001")

# Create distributed objects
user_data = {"user_id": "123", "name": "John", "email": "john@example.com"}
session_data = {"session_id": "abc123", "expires": "2024-12-31"}

user_dist_id = node_manager.create_distributed_object(user_data, "user_123")
session_dist_id = node_manager.create_distributed_object(session_data, "session_abc123")

# Synchronize with remote nodes
node_manager.sync_object_with_remote(user_dist_id, "NODE_002")
node_manager.sync_object_with_remote(session_dist_id, "NODE_003")

# Get status report
node_manager.get_synchronization_status()

print("\n6. SECURITY AND AUDIT LOGGING")
print("-" * 30)

class SecurityAuditLogger:
    """Security-focused object access logging using IDs"""
    
    def __init__(self):
        self.access_log = []
        self.sensitive_objects = set()
        self.access_patterns = defaultdict(list)
    
    def mark_sensitive(self, obj, classification: str):
        """Mark an object as sensitive"""
        obj_id = id(obj)
        self.sensitive_objects.add(obj_id)
        
        self.access_log.append({
            'event': 'CLASSIFIED',
            'object_id': obj_id,
            'classification': classification,
            'timestamp': datetime.now(),
            'object_type': type(obj).__name__
        })
        
        print(f"Marked object ID {obj_id} as {classification}")
    
    def log_access(self, obj, user_id: str, operation: str, context: str):
        """Log access to objects"""
        obj_id = id(obj)
        is_sensitive = obj_id in self.sensitive_objects
        
        access_event = {
            'event': 'ACCESS',
            'object_id': obj_id,
            'user_id': user_id,
            'operation': operation,
            'context': context,
            'is_sensitive': is_sensitive,
            'timestamp': datetime.now(),
            'session_info': f"session_{hash(user_id + str(datetime.now().hour))}"
        }
        
        self.access_log.append(access_event)
        self.access_patterns[user_id].append(access_event)
        
        if is_sensitive:
            print(f"🔒 SENSITIVE ACCESS: User {user_id} performed {operation} on object {obj_id}")
        else:
            print(f"📋 Access logged: {user_id} -> {operation}")
    
    def detect_suspicious_patterns(self):
        """Detect suspicious access patterns"""
        print("Suspicious Activity Detection:")
        print("-" * 30)
        
        for user_id, accesses in self.access_patterns.items():
            sensitive_accesses = [a for a in accesses if a['is_sensitive']]
            
            if len(sensitive_accesses) > 5:  # Threshold
                print(f"⚠️  User {user_id}: {len(sensitive_accesses)} sensitive object accesses")
                
                # Check for rapid successive accesses
                recent_accesses = [a for a in sensitive_accesses 
                                 if (datetime.now() - a['timestamp']).seconds < 300]  # 5 minutes
                
                if len(recent_accesses) > 3:
                    print(f"🚨 ALERT: Rapid sensitive data access by {user_id}")
    
    def generate_audit_report(self):
        """Generate comprehensive audit report"""
        print("Security Audit Report:")
        print("=" * 25)
        
        total_accesses = len(self.access_log)
        sensitive_accesses = len([log for log in self.access_log if log.get('is_sensitive', False)])
        unique_users = len(set(log['user_id'] for log in self.access_log if 'user_id' in log))
        
        print(f"Total access events: {total_accesses}")
        print(f"Sensitive data accesses: {sensitive_accesses}")
        print(f"Unique users: {unique_users}")
        
        print("\nRecent Sensitive Access Events:")
        recent_sensitive = [log for log in self.access_log 
                          if log.get('is_sensitive', False) and 
                          (datetime.now() - log['timestamp']).seconds < 3600]  # Last hour
        
        for event in recent_sensitive[-5:]:  # Show last 5
            print(f"  {event['timestamp']}: {event['user_id']} -> {event['operation']}")

# Security audit usage
audit_logger = SecurityAuditLogger()

# Create sensitive data objects
customer_pii = {
    "ssn": "123-45-6789",
    "credit_card": "4111-1111-1111-1111",
    "address": "123 Main St, Anytown, USA"
}

financial_data = {
    "account_balance": 50000.00,
    "account_number": "ACC-123456789",
    "transaction_history": ["deposit", "withdrawal"]
}

# Mark as sensitive
audit_logger.mark_sensitive(customer_pii, "PII")
audit_logger.mark_sensitive(financial_data, "FINANCIAL")

# Simulate various access patterns
users = ["admin_user", "regular_user", "suspicious_user"]

# Normal access
audit_logger.log_access(customer_pii, "admin_user", "READ", "customer_service")
audit_logger.log_access(financial_data, "admin_user", "READ", "account_inquiry")

# Suspicious access pattern
for i in range(7):
    audit_logger.log_access(customer_pii, "suspicious_user", "READ", f"bulk_export_{i}")
    audit_logger.log_access(financial_data, "suspicious_user", "READ", f"bulk_export_{i}")

# Detect suspicious patterns and generate report
audit_logger.detect_suspicious_patterns()
audit_logger.generate_audit_report()

print("\n7. INDUSTRY SUMMARY: ID() APPLICATIONS")
print("-" * 40)

applications = [
    "🔍 Memory Leak Detection: Track object creation/destruction",
    "🗄️  Database Connection Pooling: Monitor connection lifecycle", 
    "💾 Smart Caching: Object integrity verification",
    "📊 Object Lifecycle Tracking: Framework-level monitoring",
    "🌐 Distributed Systems: Cross-node object synchronization",
    "🔒 Security Auditing: Access control and monitoring",
    "⚡ Performance Profiling: Object allocation patterns",
    "🧪 Testing: Mock object verification and isolation"
]

for app in applications:
    print(app)

print("\n" + "="*50)
print("id() is essential for production system monitoring!")
print("="*50)

# Python - A Dynamically Typed Language

# In python , we don't need to declare the type of a variable explicitly.
# This type is determined automatically at runtime, based on the value assigned.

# Advantages of Dynamic Typing:


# Faster development due to fewer type-related constraints.

# Easier to prtotype and test ideas

# Python's dynamic typing makes this powerfuland easy to use for beginners, while still being versatile for advanced programming.

#  Datatypes in Python are determined at runtime, allowing for flexible and dynamic code.

#  DATA TYPES IN PYTHON

# Python data types classify data items and define what operations can be performed on them. 
# In Python , Everything is an object , So data types are classes and variables are instances of these classes. 
# So data types are classes and variables are instances of these classes in Python.
a=1/5
a.as_integer_ratio()  # Returns the numerator and denominator of the float as a tuple
# a is an object of class 'float'
print(f"Integer ratio of {a}: {a.as_integer_ratio()}")  
# Python data types classify data items and define what operations can be performed on them.
integer=95
floatingpointConstants=3.14
string="Hello, World!"
boolean=True
list_of_numbers=[1, 2, 3, 4, 5]
tuple_of_numbers=(1, 2, 3, 4, 5)
dictionary_of_numbers={"one": 1, "two": 2, "three": 3}
set_of_numbers={1, 2, 3, 4, 5}  

# Numeric Data Types - int , float , complex
# Sequence Data Types - string , list , tuple
# Mapping Data Type - dict
# Set Data Type - set , frozenset
# Boolean Data Type - bool
# None Type - None
none_value = None  # Represents the absence of a value
x=10  #integer
y=9.8 #floating point number
z=1j  #complex number

print(type(x))
print(type(y))
print(type(z))

#str - represents a sequence of unicode characters

# String Data Type - str
s = "Hello World 😊"
print(f"String: {s}")
print(f"Type: {type(s)}")
print(f"String length: {len(s)}")
print(f"String representation: {repr(s)}")

# Alternative ways to include emojis
greeting = "Hello World \U0001F60A"  # Unicode escape sequence
message = "Hello World " + chr(0x1F60A)  # Using chr() function

print(f"Unicode method: {greeting}")
print(f"Chr method: {message}")
print(f"All strings equal: {s == greeting == message}")

# Immutable data types can not be changed once they are created. When modified , create a new object , leaving the original unchanged.

# e.g.- Int , float , complex , bool , str , bytes , tuple etc

# Mutable data types can be changed even after once they are created without changing the variable reference.

#  e.g. - List , Dictionary , set etc.

print("\n🏭 INDUSTRY APPLICATIONS OF PYTHON DATA TYPES")
print("="*60)

print("\n1. INTEGER (int) - FINANCIAL & COUNTING SYSTEMS")
print("-" * 50)

# Banking and Financial Systems
class BankAccount:
    def __init__(self, account_number: int, initial_balance: int):
        self.account_number = account_number  # Unique identifier
        self.balance_cents = initial_balance * 100  # Store in cents to avoid float precision issues
        self.transaction_count = 0  # Counter
    
    def deposit(self, amount_dollars: int):
        self.balance_cents += amount_dollars * 100
        self.transaction_count += 1
        print(f"Deposited ${amount_dollars}. Balance: ${self.balance_cents / 100:.2f}")
    
    def get_balance(self) -> float:
        return self.balance_cents / 100

# E-commerce Inventory Management
class InventorySystem:
    def __init__(self):
        self.product_quantities = {}  # Product ID (int) -> Quantity (int)
        self.total_orders = 0
    
    def add_stock(self, product_id: int, quantity: int):
        self.product_quantities[product_id] = self.product_quantities.get(product_id, 0) + quantity
        print(f"Added {quantity} units to product {product_id}")
    
    def process_order(self, product_id: int, quantity: int) -> bool:
        if self.product_quantities.get(product_id, 0) >= quantity:
            self.product_quantities[product_id] -= quantity
            self.total_orders += 1
            return True
        return False

# Usage Examples
bank_account = BankAccount(123456789, 1000)
bank_account.deposit(500)

inventory = InventorySystem()
inventory.add_stock(101, 50)  # Product ID 101, 50 units
success = inventory.process_order(101, 3)  # Order 3 units
print(f"Order processed: {success}")

print("\nInteger Use Cases:")
print("• User IDs, Product IDs, Transaction IDs")
print("• Counting: Views, likes, downloads, inventory")
print("• Financial calculations (in cents/smallest unit)")
print("• Database primary keys and foreign keys")
print("• Status codes and error codes")

print("\n2. FLOAT - SCIENTIFIC & MEASUREMENT SYSTEMS")
print("-" * 45)

# IoT Sensor Data Processing
class WeatherStation:
    def __init__(self, station_id: str):
        self.station_id = station_id
        self.temperature_readings = []  # Celsius
        self.humidity_readings = []     # Percentage
        self.pressure_readings = []     # hPa
    
    def record_reading(self, temp: float, humidity: float, pressure: float):
        self.temperature_readings.append(temp)
        self.humidity_readings.append(humidity)
        self.pressure_readings.append(pressure)
    
    def get_average_temperature(self) -> float:
        return sum(self.temperature_readings) / len(self.temperature_readings)
    
    def temperature_trend(self) -> str:
        if len(self.temperature_readings) < 2:
            return "Insufficient data"
        
        recent_avg = sum(self.temperature_readings[-3:]) / min(3, len(self.temperature_readings))
        overall_avg = self.get_average_temperature()
        
        if recent_avg > overall_avg + 1.0:
            return "Rising"
        elif recent_avg < overall_avg - 1.0:
            return "Falling"
        return "Stable"

# Financial Analytics
class StockAnalyzer:
    def __init__(self, symbol: str):
        self.symbol = symbol
        self.prices = []
    
    def add_price(self, price: float):
        self.prices.append(price)
    
    def calculate_volatility(self) -> float:
        """Calculate price volatility (standard deviation)"""
        if len(self.prices) < 2:
            return 0.0
        
        mean_price = sum(self.prices) / len(self.prices)
        variance = sum((price - mean_price) ** 2 for price in self.prices) / len(self.prices)
        return variance ** 0.5
    
    def calculate_moving_average(self, window: int) -> list:
        """Calculate moving average"""
        if len(self.prices) < window:
            return []
        
        moving_averages = []
        for i in range(len(self.prices) - window + 1):
            avg = sum(self.prices[i:i+window]) / window
            moving_averages.append(avg)
        return moving_averages

# Usage Examples
weather_station = WeatherStation("NYC-001")
weather_station.record_reading(22.5, 65.2, 1013.25)
weather_station.record_reading(23.1, 68.7, 1012.8)
weather_station.record_reading(21.8, 72.1, 1014.2)

print(f"Average temperature: {weather_station.get_average_temperature():.1f}°C")
print(f"Temperature trend: {weather_station.temperature_trend()}")

stock = StockAnalyzer("AAPL")
prices = [150.25, 151.80, 149.95, 152.30, 148.75]
for price in prices:
    stock.add_price(price)

print(f"Stock volatility: {stock.calculate_volatility():.2f}")

print("\nFloat Use Cases:")
print("• GPS coordinates (latitude, longitude)")
print("• Sensor measurements (temperature, pressure)")
print("• Financial data (stock prices, exchange rates)")
print("• Machine learning (weights, probabilities)")
print("• Graphics and gaming (positions, angles)")

print("\n3. COMPLEX - ENGINEERING & SIGNAL PROCESSING")
print("-" * 45)

# Signal Processing for Telecommunications
class SignalProcessor:
    def __init__(self):
        self.samples = []  # Complex samples
    
    def add_sample(self, real: float, imag: float):
        sample = complex(real, imag)
        self.samples.append(sample)
    
    def calculate_magnitude_spectrum(self):
        """Calculate magnitude of complex signals"""
        magnitudes = []
        for sample in self.samples:
            magnitude = abs(sample)  # |a + bi| = sqrt(a² + b²)
            magnitudes.append(magnitude)
        return magnitudes
    
    def calculate_phase_spectrum(self):
        """Calculate phase of complex signals"""
        phases = []
        for sample in self.samples:
            phase = math.atan2(sample.imag, sample.real)
            phases.append(phase)
        return phases

# Electrical Engineering - AC Circuit Analysis
class ACCircuit:
    def __init__(self):
        self.impedances = []  # Complex impedances Z = R + jX
    
    def add_resistor(self, resistance: float):
        """Add resistor (purely real impedance)"""
        self.impedances.append(complex(resistance, 0))
    
    def add_capacitor(self, reactance: float):
        """Add capacitor (negative imaginary impedance)"""
        self.impedances.append(complex(0, -reactance))
    
    def add_inductor(self, reactance: float):
        """Add inductor (positive imaginary impedance)"""
        self.impedances.append(complex(0, reactance))
    
    def total_impedance_series(self):
        """Calculate total impedance in series"""
        return sum(self.impedances)
    
    def calculate_current(self, voltage: complex):
        """Calculate current using Ohm's law: I = V/Z"""
        total_z = self.total_impedance_series()
        if total_z == 0:
            return complex(0, 0)
        return voltage / total_z

# Usage Examples
signal_processor = SignalProcessor()
signal_processor.add_sample(1.0, 0.5)  # Real: 1.0, Imaginary: 0.5
signal_processor.add_sample(0.8, -0.3)
signal_processor.add_sample(-0.2, 0.9)

magnitudes = signal_processor.calculate_magnitude_spectrum()
print(f"Signal magnitudes: {[f'{m:.2f}' for m in magnitudes]}")

ac_circuit = ACCircuit()
ac_circuit.add_resistor(50.0)    # 50 Ω resistor
ac_circuit.add_capacitor(30.0)   # 30 Ω capacitive reactance
ac_circuit.add_inductor(80.0)    # 80 Ω inductive reactance

total_impedance = ac_circuit.total_impedance_series()
print(f"Total circuit impedance: {total_impedance}")

voltage = complex(120, 0)  # 120V AC voltage
current = ac_circuit.calculate_current(voltage)
print(f"Circuit current: {current}")

print("\nComplex Use Cases:")
print("• Digital signal processing (FFT, filters)")
print("• Electrical engineering (AC circuits, power)")
print("• Control systems (transfer functions)")
print("• Quantum computing (quantum states)")
print("• Computer graphics (rotations, transformations)")

print("\n4. STRING - TEXT PROCESSING & COMMUNICATION")
print("-" * 45)

# Web Development - URL Processing
class URLProcessor:
    def __init__(self):
        self.processed_urls = []
    
    def validate_url(self, url: str) -> bool:
        """Basic URL validation"""
        return url.startswith(('http://', 'https://')) and '.' in url
    
    def extract_domain(self, url: str) -> str:
        """Extract domain from URL"""
        if not self.validate_url(url):
            return ""
        
        # Remove protocol
        domain = url.split('://')[1]
        # Remove path
        domain = domain.split('/')[0]
        # Remove port
        domain = domain.split(':')[0]
        return domain
    
    def create_slug(self, title: str) -> str:
        """Create URL-friendly slug from title"""
        # Convert to lowercase
        slug = title.lower()
        # Replace spaces and special chars with hyphens
        slug = re.sub(r'[^a-z0-9]+', '-', slug)
        # Remove leading/trailing hyphens
        return slug.strip('-')

# Natural Language Processing for Customer Service
class CustomerServiceBot:
    def __init__(self):
        self.responses = {
            'greeting': "Hello! How can I help you today?",
            'billing': "I'll transfer you to our billing department.",
            'technical': "Let me help you with that technical issue.",
            'complaint': "I apologize for the inconvenience. Let me help resolve this."
        }
        self.keywords = {
            'greeting': ['hello', 'hi', 'hey', 'good morning', 'good afternoon'],
            'billing': ['bill', 'charge', 'payment', 'invoice', 'cost'],
            'technical': ['error', 'bug', 'not working', 'broken', 'issue'],
            'complaint': ['angry', 'frustrated', 'disappointed', 'terrible']
        }
    
    def classify_intent(self, message: str) -> str:
        """Classify customer message intent"""
        message_lower = message.lower()
        
        for intent, keywords in self.keywords.items():
            for keyword in keywords:
                if keyword in message_lower:
                    return intent
        
        return 'general'
    
    def generate_response(self, message: str) -> str:
        """Generate appropriate response"""
        intent = self.classify_intent(message)
        return self.responses.get(intent, "I'm sorry, I didn't understand. Could you please rephrase?")

# Log File Analysis for DevOps
class LogAnalyzer:
    def __init__(self):
        self.error_patterns = ['ERROR', 'FATAL', 'EXCEPTION', 'FAILED']
        self.warning_patterns = ['WARN', 'WARNING', 'DEPRECATED']
    
    def parse_log_line(self, line: str) -> dict:
        """Parse log line into components"""
        # Split log line into components: timestamp, level, message
        parts = line.strip().split(' ', 3)
        # Expected format: "2024-01-15 10:30:25 ERROR Database connection failed"
        if len(parts) >= 4:
            return {
                'timestamp': parts[0] + ' ' + parts[1],
                'level': parts[2],
                'message': parts[3]
            }
        return {'raw': line}
    
    def count_log_levels(self, log_content: str) -> dict:
        """Count occurrences of different log levels"""
        lines = log_content.split('\n')
        counts = {'ERROR': 0, 'WARN': 0, 'INFO': 0, 'DEBUG': 0}
        
        for line in lines:
            for level in counts.keys():
                if level in line:
                    counts[level] += 1
                    break
        
        return counts
    
    def extract_error_messages(self, log_content: str) -> list:
        """Extract all error messages"""
        lines = log_content.split('\n')
        errors = []
        
        for line in lines:
            for pattern in self.error_patterns:
                if pattern in line:
                    errors.append(line.strip())
                    break
        
        return errors

# Usage Examples
url_processor = URLProcessor()
test_url = "https://api.company.com/v1/users"
domain = url_processor.extract_domain(test_url)
print(f"Domain extracted: {domain}")

slug = url_processor.create_slug("How to Build REST APIs in Python")
print(f"URL slug: {slug}")

chatbot = CustomerServiceBot()
customer_message = "Hi there, I have an issue with my bill"
response = chatbot.generate_response(customer_message)
print(f"Bot response: {response}")

log_analyzer = LogAnalyzer()
sample_log = """2024-01-15 10:30:25 INFO Application started
2024-01-15 10:31:15 ERROR Database connection failed
2024-01-15 10:31:20 WARN Retrying database connection
2024-01-15 10:31:25 INFO Database connection established"""

log_counts = log_analyzer.count_log_levels(sample_log)
print(f"Log level counts: {log_counts}")

print("\nString Use Cases:")
print("• Web development (URLs, HTML, JSON)")
print("• Database queries and text search")
print("• File paths and configuration")
print("• User interface text and messages")
print("• API responses and data serialization")
print("• Log analysis and text processing")
print("• Email addresses and phone numbers")

print("\n5. LIST - DYNAMIC DATA COLLECTIONS")
print("-" * 40)

# E-commerce Shopping Cart
class ShoppingCart:
    def __init__(self):
        self.items = []  # List of cart items
        self.order_history = []  # List of past orders
    
    def add_item(self, item: dict):
        """Add item to cart"""
        self.items.append(item)
        print(f"Added {item['name']} to cart")
    
    def remove_item(self, item_name: str):
        """Remove item from cart"""
        self.items = [item for item in self.items if item['name'] != item_name]
    
    def get_total(self) -> float:
        """Calculate total price"""
        return sum(item['price'] * item['quantity'] for item in self.items)
    
    def checkout(self):
        """Process checkout and save to order history"""
        if self.items:
            order = {
                'items': self.items.copy(),
                'total': self.get_total(),
                'timestamp': datetime.now()
            }
            self.order_history.append(order)
            self.items.clear()
            return order
        return None

# Real-time Data Processing
class MetricsCollector:
    def __init__(self, max_size: int = 1000):
        self.cpu_usage = []     # Recent CPU measurements
        self.memory_usage = []  # Recent memory measurements
        self.request_times = [] # API response times
        self.max_size = max_size
    
    def add_cpu_reading(self, percentage: float):
        """Add CPU usage reading"""
        self.cpu_usage.append(percentage)
        if len(self.cpu_usage) > self.max_size:
            self.cpu_usage.pop(0)  # Remove oldest reading
    
    def add_memory_reading(self, percentage: float):
        """Add memory usage reading"""
        self.memory_usage.append(percentage)
        if len(self.memory_usage) > self.max_size:
            self.memory_usage.pop(0)
    
    def add_request_time(self, milliseconds: float):
        """Add API response time"""
        self.request_times.append(milliseconds)
        if len(self.request_times) > self.max_size:
            self.request_times.pop(0)
    
    def get_averages(self) -> dict:
        """Calculate average metrics"""
        return {
            'avg_cpu': sum(self.cpu_usage) / len(self.cpu_usage) if self.cpu_usage else 0,
            'avg_memory': sum(self.memory_usage) / len(self.memory_usage) if self.memory_usage else 0,
            'avg_response_time': sum(self.request_times) / len(self.request_times) if self.request_times else 0
        }
    
    def detect_anomalies(self) -> list:
        """Detect performance anomalies"""
        anomalies = []
        
        if self.cpu_usage and max(self.cpu_usage[-10:]) > 90:
            anomalies.append("High CPU usage detected")
        
        if self.memory_usage and max(self.memory_usage[-10:]) > 85:
            anomalies.append("High memory usage detected")
        
        if self.request_times and max(self.request_times[-10:]) > 5000:
            anomalies.append("Slow API responses detected")
        
        return anomalies

# Machine Learning Data Pipeline
class DataPipeline:
    def __init__(self):
        self.raw_data = []        # Raw input data
        self.processed_data = []  # Cleaned and processed data
        self.features = []        # Extracted features
        self.labels = []          # Training labels
    
    def ingest_data(self, data_batch: list):
        """Ingest new data batch"""
        self.raw_data.extend(data_batch)
        print(f"Ingested {len(data_batch)} records")
    
    def clean_data(self):
        """Clean and validate data"""
        self.processed_data = []
        for record in self.raw_data:
            if self._is_valid_record(record):
                cleaned_record = self._clean_record(record)
                self.processed_data.append(cleaned_record)
    
    def _is_valid_record(self, record: dict) -> bool:
        """Validate individual record"""
        required_fields = ['id', 'value']
        return all(field in record for field in required_fields)
    
    def _clean_record(self, record: dict) -> dict:
        """Clean individual record"""
        cleaned = record.copy()
        # Remove null values, normalize strings, etc.
        cleaned['value'] = float(cleaned['value']) if cleaned['value'] else 0.0
        return cleaned
    
    def extract_features(self):
        """Extract features from processed data"""
        self.features = []
        for record in self.processed_data:
            feature_vector = [
                record['value'],
                len(str(record.get('description', ''))),
                1 if record.get('category') == 'premium' else 0
            ]
            self.features.append(feature_vector)

# Usage Examples
cart = ShoppingCart()
cart.add_item({'name': 'Laptop', 'price': 999.99, 'quantity': 1})
cart.add_item({'name': 'Mouse', 'price': 29.99, 'quantity': 2})
print(f"Cart total: ${cart.get_total():.2f}")

order = cart.checkout()
print(f"Order processed: {len(cart.order_history)} orders in history")

metrics = MetricsCollector()
metrics.add_cpu_reading(25.5)
metrics.add_cpu_reading(45.2)
metrics.add_cpu_reading(95.8)  # High usage
metrics.add_memory_reading(60.3)

anomalies = metrics.detect_anomalies()
print(f"Detected anomalies: {anomalies}")

pipeline = DataPipeline()
sample_data = [
    {'id': 1, 'value': '42.5', 'description': 'Test data', 'category': 'premium'},
    {'id': 2, 'value': '18.3', 'description': 'More test data', 'category': 'standard'}
]
pipeline.ingest_data(sample_data)
pipeline.clean_data()
pipeline.extract_features()
print(f"Extracted {len(pipeline.features)} feature vectors")

print("\nList Use Cases:")
print("• Shopping carts and order processing")
print("• Time-series data (metrics, logs, sensors)")
print("• Message queues and task processing")
print("• Machine learning datasets")
print("• User activities and audit trails")
print("• File processing and batch operations")

print("\n6. TUPLE - IMMUTABLE STRUCTURED DATA")
print("-" * 40)

# Database Query Results
class DatabaseConnection:
    def __init__(self):
        self.connection_pool = [
            ('server1', 5432, 'active', 0.2),    # (host, port, status, load)
            ('server2', 5432, 'active', 0.8),
            ('server3', 5432, 'maintenance', 0.0)
        ]
    
    def get_available_servers(self) -> list:
        """Get available database servers"""
        return [server for server in self.connection_pool if server[2] == 'active']
    
    def get_best_server(self) -> tuple:
        """Get server with lowest load"""
        available = self.get_available_servers()
        if not available:
            return None
        return min(available, key=lambda x: x[3])  # Sort by load (index 3)

# Geographic Coordinates
class LocationService:
    def __init__(self):
        self.cities = {
            'New York': (40.7128, -74.0060),
            'London': (51.5074, -0.1278),
            'Tokyo': (35.6762, 139.6503),
            'Sydney': (-33.8688, 151.2093)
        }
    
    def calculate_distance(self, coord1: tuple, coord2: tuple) -> float:
        """Calculate distance between two coordinates"""
        lat1, lon1 = coord1
        lat2, lon2 = coord2
        
        # Haversine formula (simplified)
        dlat = math.radians(lat2 - lat1)
        dlon = math.radians(lon2 - lon1)
        a = (math.sin(dlat/2)**2 + 
             math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * 
             math.sin(dlon/2)**2)
        c = 2 * math.asin(math.sqrt(a))
        r = 6371  # Earth's radius in kilometers
        return c * r
    
    def find_nearest_city(self, location: tuple) -> str:
        """Find nearest city to given coordinates"""
        min_distance = float('inf')
        nearest_city = ""
        
        for city, coords in self.cities.items():
            distance = self.calculate_distance(location, coords)
            if distance < min_distance:
                min_distance = distance
                nearest_city = city
        
        return nearest_city

# API Response Data
class APIResponse:
    def __init__(self):
        pass
    
    def create_response(self, status_code: int, message: str, data=None) -> tuple:
        """Create API response tuple"""
        return (status_code, message, data, datetime.now())
    
    def parse_response(self, response: tuple) -> dict:
        """Parse response tuple into structured data"""
        if len(response) != 4:
            return {'error': 'Invalid response format'}
        
        status_code, message, data, timestamp = response
        return {
            'status_code': status_code,
            'message': message,
            'data': data,
            'timestamp': timestamp,
            'success': 200 <= status_code < 300
        }

# Usage Examples
db_conn = DatabaseConnection()
best_server = db_conn.get_best_server()
print(f"Best server: {best_server[0]}:{best_server[1]} (load: {best_server[3]:.1f})")

location_service = LocationService()
my_location = (40.7589, -73.9851)  # Times Square
nearest = location_service.find_nearest_city(my_location)
distance = location_service.calculate_distance(my_location, location_service.cities[nearest])
print(f"Nearest city to {my_location}: {nearest} ({distance:.1f} km away)")

api = APIResponse()
response = api.create_response(200, "Success", {"user_id": 123, "name": "John"})
parsed = api.parse_response(response)
print(f"API response success: {parsed['success']}")

print("\nTuple Use Cases:")
print("• Database query results and table rows")
print("• Geographic coordinates (latitude, longitude)")
print("• RGB color values (red, green, blue)")
print("• API responses and structured data")
print("• Configuration parameters")
print("• Mathematical vectors and points")
print("• Return multiple values from functions")

print("\n7. DICTIONARY - KEY-VALUE MAPPINGS")
print("-" * 40)

# User Session Management
class SessionManager:
    def __init__(self):
        self.sessions = {}  # session_id -> session_data
        self.user_sessions = {}  # user_id -> list of session_ids
    
    def create_session(self, user_id: str) -> str:
        """Create new user session"""
        session_id = f"sess_{hash(user_id + str(datetime.now()))}"
        
        session_data = {
            'user_id': user_id,
            'created_at': datetime.now(),
            'last_activity': datetime.now(),
            'permissions': set(),
            'data': {}
        }
        
        self.sessions[session_id] = session_data
        
        if user_id not in self.user_sessions:
            self.user_sessions[user_id] = []
        self.user_sessions[user_id].append(session_id)
        
        return session_id
    
    def update_session(self, session_id: str, key: str, value):
        """Update session data"""
        if session_id in self.sessions:
            self.sessions[session_id]['data'][key] = value
            self.sessions[session_id]['last_activity'] = datetime.now()
    
    def get_session_data(self, session_id: str) -> dict:
        """Get session data"""
        return self.sessions.get(session_id, {})
    
    def cleanup_expired_sessions(self, hours: int = 24):
        """Remove expired sessions"""
        cutoff_time = datetime.now() - timedelta(hours=hours)
        expired_sessions = []
        
        for session_id, session_data in self.sessions.items():
            if session_data['last_activity'] < cutoff_time:
                expired_sessions.append(session_id)
        
        for session_id in expired_sessions:
            del self.sessions[session_id]
        
        print(f"Cleaned up {len(expired_sessions)} expired sessions")

# Configuration Management
class ConfigManager:
    def __init__(self):
        self.config = {
            'database': {
                'host': 'localhost',
                'port': 5432,
                'name': 'myapp',
                'pool_size': 10
            },
            'redis': {
                'host': 'localhost',
                'port': 6379,
                'db': 0
            },
            'api': {
                'rate_limit': 1000,
                'timeout': 30,
                'allowed_origins': ['https://myapp.com', 'https://api.myapp.com']
            },
            'features': {
                'new_dashboard': True,
                'beta_analytics': False,
                'premium_features': True
            }
        }
    
    def get_config(self, key_path: str):
        """Get configuration value using dot notation"""
        keys = key_path.split('.')
        value = self.config
        
        for key in keys:
            if isinstance(value, dict) and key in value:
                value = value[key]
            else:
                return None
        
        return value
    
    def update_config(self, key_path: str, new_value):
        """Update configuration value"""
        keys = key_path.split('.')
        config_section = self.config
        
        for key in keys[:-1]:
            if key not in config_section:
                config_section[key] = {}
            config_section = config_section[key]
        
        config_section[keys[-1]] = new_value
    
    def is_feature_enabled(self, feature_name: str) -> bool:
        """Check if feature is enabled"""
        return self.get_config(f'features.{feature_name}') or False

# Caching System
class LRUCache:
    def __init__(self, max_size: int):
        self.cache = {}  # key -> value
        self.access_order = []  # Track access order for LRU
        self.max_size = max_size
    
    def get(self, key: str):
        """Get value from cache"""
        if key in self.cache:
            # Move to end (most recently used)
            self.access_order.remove(key)
            self.access_order.append(key)
            return self.cache[key]
        return None
    
    def put(self, key: str, value):
        """Put value in cache"""
        if key in self.cache:
            # Update existing key
            self.cache[key] = value
            self.access_order.remove(key)
            self.access_order.append(key)
        else:
            # Add new key
            if len(self.cache) >= self.max_size:
                # Remove least recently used
                lru_key = self.access_order.pop(0)
                del self.cache[lru_key]
            
            self.cache[key] = value
            self.access_order.append(key)
    
    def get_cache_info(self) -> dict:
        """Get cache statistics"""
        return {
            'size': len(self.cache),
            'max_size': self.max_size,
            'keys': list(self.cache.keys()),
            'hit_ratio': 'Not implemented'  # Would need hit/miss tracking
        }

# Usage Examples
session_mgr = SessionManager()
session_id = session_mgr.create_session("user123")
session_mgr.update_session(session_id, "shopping_cart", ["item1", "item2"])
session_mgr.update_session(session_id, "preferences", {"theme": "dark"})

session_data = session_mgr.get_session_data(session_id)
print(f"Session data: {session_data['data']}")

config_mgr = ConfigManager()
db_host = config_mgr.get_config("database.host")
rate_limit = config_mgr.get_config("api.rate_limit")
print(f"Database host: {db_host}, API rate limit: {rate_limit}")

is_beta_enabled = config_mgr.is_feature_enabled("beta_analytics")
print(f"Beta analytics enabled: {is_beta_enabled}")

cache = LRUCache(max_size=3)
cache.put("user:123", {"name": "John", "email": "john@example.com"})
cache.put("user:456", {"name": "Jane", "email": "jane@example.com"})
cache.put("product:789", {"name": "Laptop", "price": 999.99})

user_data = cache.get("user:123")
print(f"Cached user data: {user_data}")

cache_info = cache.get_cache_info()
print(f"Cache info: {cache_info}")

print("\nDictionary Use Cases:")
print("• User session and authentication data")
print("• Application configuration and settings")
print("• Caching and memoization")
print("• Database record representation")
print("• JSON API request/response data")
print("• Feature flags and A/B testing")
print("• Lookup tables and mappings")

print("\n8. SET - UNIQUE COLLECTIONS & RELATIONSHIPS")
print("-" * 40)

# User Permissions and Role Management
class RoleBasedAccessControl:
    def __init__(self):
        self.user_permissions = {}  # user_id -> set of permissions
        self.role_permissions = {
            'admin': {'read', 'write', 'delete', 'user_management', 'system_config'},
            'manager': {'read', 'write', 'user_management'},
            'employee': {'read', 'write'},
            'viewer': {'read'}
        }
    
    def assign_role(self, user_id: str, role: str):
        """Assign role to user"""
        if role in self.role_permissions:
            self.user_permissions[user_id] = self.role_permissions[role].copy()
            print(f"Assigned {role} role to user {user_id}")
    
    def grant_additional_permission(self, user_id: str, permission: str):
        """Grant additional permission to user"""
        if user_id not in self.user_permissions:
            self.user_permissions[user_id] = set()
        self.user_permissions[user_id].add(permission)
    
    def has_permission(self, user_id: str, permission: str) -> bool:
        """Check if user has specific permission"""
        return permission in self.user_permissions.get(user_id, set())
    
    def get_common_permissions(self, user1: str, user2: str) -> set:
        """Get permissions common to both users"""
        perms1 = self.user_permissions.get(user1, set())
        perms2 = self.user_permissions.get(user2, set())
        return perms1.intersection(perms2)
    
    def get_unique_permissions(self, user1: str, user2: str) -> set:
        """Get permissions unique to user1 (not in user2)"""
        perms1 = self.user_permissions.get(user1, set())
        perms2 = self.user_permissions.get(user2, set())
        return perms1.difference(perms2)

# Data Deduplication System
class DataDeduplicator:
    def __init__(self):
        self.seen_records = set()  # Store hashes of seen records
        self.unique_emails = set()
        self.unique_phone_numbers = set()
    
    def add_user_record(self, user_data: dict) -> bool:
        """Add user record, return True if new, False if duplicate"""
        # Create hash of critical fields
        critical_data = f"{user_data.get('email', '')}_{user_data.get('phone', '')}"
        record_hash = hash(critical_data)
        
        if record_hash in self.seen_records:
            return False  # Duplicate
        
        # Check individual field uniqueness
        email = user_data.get('email')
        phone = user_data.get('phone')
        
        if email and email in self.unique_emails:
            print(f"Warning: Email {email} already exists")
            return False
        
        if phone and phone in self.unique_phone_numbers:
            print(f"Warning: Phone {phone} already exists")
            return False
        
        # Add to sets
        self.seen_records.add(record_hash)
        if email:
            self.unique_emails.add(email)
        if phone:
            self.unique_phone_numbers.add(phone)
        
        return True
    
    def get_stats(self) -> dict:
        """Get deduplication statistics"""
        return {
            'total_records': len(self.seen_records),
            'unique_emails': len(self.unique_emails),
            'unique_phones': len(self.unique_phone_numbers)
        }

# Content Tag System
class ContentTagSystem:
    def __init__(self):
        self.content_tags = {}  # content_id -> set of tags
        self.tag_content = {}   # tag -> set of content_ids
    
    def add_content(self, content_id: str, tags: list):
        """Add content with tags"""
        tag_set = set(tags)
        self.content_tags[content_id] = tag_set
        
        # Update reverse index
        for tag in tag_set:
            if tag not in self.tag_content:
                self.tag_content[tag] = set()
            self.tag_content[tag].add(content_id)
    
    def find_content_by_tags(self, required_tags: list, any_tags: list = None) -> set:
        """Find content matching tag criteria"""
        if not required_tags and not any_tags:
            return set()
        
        result_set = None
        
        # Content must have ALL required tags
        for tag in required_tags:
            content_with_tag = self.tag_content.get(tag, set())
            if result_set is None:
                result_set = content_with_tag.copy()
            else:
                result_set = result_set.intersection(content_with_tag)
        
        # Content can have ANY of the any_tags
        if any_tags:
            any_content = set()
            for tag in any_tags:
                any_content = any_content.union(self.tag_content.get(tag, set()))
            
            if result_set is None:
                result_set = any_content
            else:
                result_set = result_set.union(any_content)
        
        return result_set or set()
    
    def get_similar_content(self, content_id: str) -> list:
        """Find content with overlapping tags"""
        if content_id not in self.content_tags:
            return []
        
        content_tags = self.content_tags[content_id]
        similar_scores = {}
        
        for other_id, other_tags in self.content_tags.items():
            if other_id != content_id:
                # Calculate Jaccard similarity
                intersection = len(content_tags.intersection(other_tags))
                union = len(content_tags.union(other_tags))
                similarity = intersection / union if union > 0 else 0
                
                if similarity > 0:
                    similar_scores[other_id] = similarity
        
        # Sort by similarity score
        return sorted(similar_scores.items(), key=lambda x: x[1], reverse=True)

# Usage Examples
rbac = RoleBasedAccessControl()
rbac.assign_role("john", "manager")
rbac.assign_role("jane", "employee")

can_delete = rbac.has_permission("john", "delete")
print(f"John can delete: {can_delete}")

common_perms = rbac.get_common_permissions("john", "jane")
print(f"Common permissions: {common_perms}")

unique_perms = rbac.get_unique_permissions("john", "jane")
print(f"John's unique permissions: {unique_perms}")

deduplicator = DataDeduplicator()
users = [
    {"email": "john@example.com", "phone": "555-0123"},
    {"email": "jane@example.com", "phone": "555-0124"},
    {"email": "john@example.com", "phone": "555-0125"},  # Duplicate email
]

for i, user in enumerate(users):
    is_new = deduplicator.add_user_record(user)
    print(f"User {i+1} added: {is_new}")

print(f"Deduplication stats: {deduplicator.get_stats()}")

tag_system = ContentTagSystem()
tag_system.add_content("article1", ["python", "programming", "tutorial"])
tag_system.add_content("article2", ["python", "data-science", "pandas"])
tag_system.add_content("article3", ["javascript", "web-development", "tutorial"])

# Find articles with specific tags
python_content = tag_system.find_content_by_tags(["python"])
tutorial_content = tag_system.find_content_by_tags(["tutorial"])
print(f"Python content: {python_content}")
print(f"Tutorial content: {tutorial_content}")

# Find similar content
similar = tag_system.get_similar_content("article1")
print(f"Content similar to article1: {similar}")

print("\nSet Use Cases:")
print("• User permissions and role-based access control")
print("• Data deduplication and uniqueness constraints")
print("• Content tagging and recommendation systems")
print("• Social network relationships (followers, friends)")
print("• Inventory tracking (available, sold items)")
print("• Feature flags and A/B testing groups")
print("• Cache invalidation and dependency tracking")

print("\n9. BOOLEAN - CONTROL FLOW & FLAGS")
print("-" * 35)

# Feature Toggle System
class FeatureToggleService:
    def __init__(self):
        self.features = {
            'new_dashboard': True,
            'beta_analytics': False,
            'premium_features': True,
            'maintenance_mode': False,
            'debug_logging': False
        }
        self.user_overrides = {}  # user_id -> feature_name -> bool
    
    def is_enabled(self, feature_name: str, user_id: str = None) -> bool:
        """Check if feature is enabled for user"""
        # Check user-specific override first
        if user_id and user_id in self.user_overrides:
            user_features = self.user_overrides[user_id]
            if feature_name in user_features:
                return user_features[feature_name]
        
        # Fall back to global setting
        return self.features.get(feature_name, False)
    
    def enable_feature_for_user(self, feature_name: str, user_id: str):
        """Enable feature for specific user"""
        if user_id not in self.user_overrides:
            self.user_overrides[user_id] = {}
        self.user_overrides[user_id][feature_name] = True
    
    def toggle_global_feature(self, feature_name: str):
        """Toggle global feature state"""
        if feature_name in self.features:
            self.features[feature_name] = not self.features[feature_name]

# API Request Validation
class APIValidator:
    def __init__(self):
        self.validation_rules = {
            'email': self._is_valid_email,
            'phone': self._is_valid_phone,
            'age': self._is_valid_age,
            'required': self._is_not_empty
        }
    
    def validate_request(self, data: dict, rules: dict) -> tuple:
        """Validate request data against rules"""
        is_valid = True
        errors = []
        
        for field, field_rules in rules.items():
            field_value = data.get(field)
            
            for rule in field_rules:
                if rule in self.validation_rules:
                    field_is_valid = self.validation_rules[rule](field_value)
                    if not field_is_valid:
                        is_valid = False
                        errors.append(f"{field} failed {rule} validation")
        
        return is_valid, errors
    
    def _is_valid_email(self, email) -> bool:
        """Basic email validation"""
        return email and '@' in str(email) and '.' in str(email)
    
    def _is_valid_phone(self, phone) -> bool:
        """Basic phone validation"""
        return phone and len(str(phone)) >= 10
    
    def _is_valid_age(self, age) -> bool:
        """Age validation"""
        try:
            age_int = int(age)
            return 0 <= age_int <= 120
        except (ValueError, TypeError):
            return False
    
    def _is_not_empty(self, value) -> bool:
        """Check if value is not empty"""
        return value is not None and str(value).strip() != ""

# Circuit Breaker Pattern
class CircuitBreaker:
    def __init__(self, failure_threshold: int = 5, timeout: int = 60):
        self.failure_threshold = failure_threshold
        self.timeout = timeout
        self.failure_count = 0
        self.last_failure_time = None
        self.is_open = False  # Boolean state
    
    def call(self, func, *args, **kwargs):
        """Call function through circuit breaker"""
        if self.is_open:
            if self._should_attempt_reset():
                self.is_open = False
                self.failure_count = 0
                print("Circuit breaker attempting reset")
            else:
                raise Exception("Circuit breaker is OPEN")
        
        try:
            result = func(*args, **kwargs)
            self._on_success()
            return result
        except Exception as e:
            self._on_failure()
            raise e
    
    def _on_success(self):
        """Handle successful call"""
        self.failure_count = 0
        if self.is_open:
            self.is_open = False
            print("Circuit breaker CLOSED after successful call")
    
    def _on_failure(self):
        """Handle failed call"""
        self.failure_count += 1
        self.last_failure_time = datetime.now()
        
        if self.failure_count >= self.failure_threshold:
            self.is_open = True
            print(f"Circuit breaker OPENED after {self.failure_count} failures")
    
    def _should_attempt_reset(self) -> bool:
        """Check if enough time has passed to attempt reset"""
        if self.last_failure_time is None:
            return True
        
        time_since_failure = (datetime.now() - self.last_failure_time).seconds
        return time_since_failure >= self.timeout
    
    def get_state(self) -> dict:
        """Get circuit breaker state"""
        return {
            'is_open': self.is_open,
            'failure_count': self.failure_count,
            'last_failure_time': self.last_failure_time
        }

# Usage Examples
feature_service = FeatureToggleService()

# Check feature availability
show_new_dashboard = feature_service.is_enabled('new_dashboard')
show_beta_features = feature_service.is_enabled('beta_analytics')
print(f"New dashboard enabled: {show_new_dashboard}")
print(f"Beta analytics enabled: {show_beta_features}")

# Enable beta feature for specific user
feature_service.enable_feature_for_user('beta_analytics', 'power_user_123')
beta_for_user = feature_service.is_enabled('beta_analytics', 'power_user_123')
print(f"Beta analytics for power user: {beta_for_user}")

validator = APIValidator()
test_data = {
    'email': 'user@example.com',
    'phone': '1234567890',
    'age': '25',
    'name': 'John Doe'
}

validation_rules = {
    'email': ['required', 'email'],
    'phone': ['required', 'phone'],
    'age': ['required', 'age'],
    'name': ['required']
}

is_valid, errors = validator.validate_request(test_data, validation_rules)
print(f"Request valid: {is_valid}")
if errors:
    print(f"Validation errors: {errors}")

# Circuit breaker example
circuit_breaker = CircuitBreaker(failure_threshold=3, timeout=30)

def unreliable_service():
    """Simulate an unreliable external service"""
    # Complete the unreliable_service function
    def unreliable_service():
        """Simulate an unreliable external service"""
        if random.random() < 0.7:  # 70% chance of failure
            raise Exception("Service unavailable")
        return "Service call successful"

    # Test the circuit breaker
    print("\nTesting Circuit Breaker:")
    for i in range(6):
        try:
            result = circuit_breaker.call(unreliable_service)
            print(f"Call {i+1}: {result}")
        except Exception as e:
            print(f"Call {i+1}: {e}")

    print(f"Circuit breaker state: {circuit_breaker.get_state()}")

    print("\nBoolean Use Cases:")
    print("• Feature flags and A/B testing")
    print("• User permissions and access control")
    print("• API request validation")
    print("• System health monitoring")
    print("• Circuit breaker patterns")
    print("• Configuration settings")
    print("• Error handling and retry logic")

    print("\n10. NONE TYPE - NULL VALUES & OPTIONAL DATA")
    print("-" * 45)

    # API Response with Optional Data
    class UserProfileAPI:
        def __init__(self):
            self.users = {
                'user1': {
                    'name': 'John Doe',
                    'email': 'john@example.com',
                    'phone': None,  # Optional field
                    'avatar': None,
                    'last_login': datetime(2024, 1, 15)
                },
                'user2': {
                    'name': 'Jane Smith',
                    'email': 'jane@example.com',
                    'phone': '555-0123',
                    'avatar': 'https://example.com/avatar.jpg',
                    'last_login': None  # Never logged in
                }
            }
        
        def get_user_profile(self, user_id: str) -> dict:
            """Get user profile, handling None values"""
            user = self.users.get(user_id)
            if user is None:
                return {'error': 'User not found'}
            
            # Build response, handling None values
            profile = {
                'name': user['name'],
                'email': user['email'],
                'has_phone': user['phone'] is not None,
                'has_avatar': user['avatar'] is not None,
                'last_login': user['last_login'].isoformat() if user['last_login'] else None
            }
            
            return profile

    # Database Connection with None Handling
    class DatabaseManager:
        def __init__(self):
            self.connection = None
            self.last_error = None
        
        def connect(self, host: str, port: int) -> bool:
            """Attempt database connection"""
            try:
                # Simulate connection logic
                if host and port:
                    self.connection = f"Connected to {host}:{port}"
                    self.last_error = None
                    return True
                else:
                    self.connection = None
                    self.last_error = "Invalid host or port"
                    return False
            except Exception as e:
                self.connection = None
                self.last_error = str(e)
                return False
        
        def is_connected(self) -> bool:
            """Check if connection is active"""
            return self.connection is not None
        
        def disconnect(self):
            """Close database connection"""
            self.connection = None
            self.last_error = None

    # Usage Examples
    user_api = UserProfileAPI()
    profile1 = user_api.get_user_profile('user1')
    profile2 = user_api.get_user_profile('user2')
    profile3 = user_api.get_user_profile('unknown')

    print(f"User1 profile: {profile1}")
    print(f"User2 profile: {profile2}")
    print(f"Unknown user: {profile3}")

    db_manager = DatabaseManager()
    connected = db_manager.connect("localhost", 5432)
    print(f"Database connected: {connected}")
    print(f"Connection status: {db_manager.is_connected()}")

    print("\nNone Use Cases:")
    print("• Optional API fields and parameters")
    print("• Database NULL values")
    print("• Uninitialized variables")
    print("• Function return values (no explicit return)")
    print("• Default parameter values")
    print("• Error handling (no result)")
    print("• Caching systems (cache miss)")

    print("\n" + "="*60)
    print("Python data types enable powerful, flexible applications!")
    print("Each type serves specific industry use cases effectively.")
    print("="*60)


# List - Ordered Mutable collection of items
#  this may contain multiple data types




