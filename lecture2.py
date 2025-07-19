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