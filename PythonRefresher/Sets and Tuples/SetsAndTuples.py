import sys
from collections import namedtuple
import sys
import timeit
import copy
import numpy as np

"""
Sets are similar to lists but are unordered and cannot contain duplications
Use curly brackets
"""

# my_set = {1, 2, 3, 4, 5, 1, 2}
# print(my_set)
# print(len(my_set))
#
#
# for x in my_set:
#     print(x)
#
#
# my_set.discard(3)
# print(my_set)
# my_set.add(6)
# print(my_set)
# my_set.update([7, 8])
# print(my_set)


my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[1])
# my_tuple[1] = 100

# This will raise a TypeError because tuples are immutable
# TypeError: 'tuple' object does not support item assignment

# ============================================================================
# DEEP DIVE: TUPLES - IMMUTABLE SEQUENCES
# ============================================================================

# Tuple creation and memory efficiency
print("=== TUPLE CREATION ===")
t1 = (1, 2, 3)  # Literal syntax
t2 = tuple([1, 2, 3])  # Constructor
t3 = 1, 2, 3  # Parentheses optional for multiple items
single_tuple = (42,)  # Comma required for single item tuple
print(f"t1: {t1}, id: {id(t1)}")
print(f"Single tuple: {single_tuple}")

# Tuple interning for small tuples (CPython optimization)
a = (1, 2)
b = (1, 2)
print(f"Small tuples interned: {a is b}")  # May be True in CPython

# Memory layout demonstration
tuple_sizes = [(i,) * i for i in range(1, 6)]
for t in tuple_sizes:
    print(f"Tuple {t}: {sys.getsizeof(t)} bytes")

# ============================================================================
# ADVANCED TUPLE OPERATIONS
# ============================================================================

print("\n=== ADVANCED TUPLE OPERATIONS ===")

# Tuple unpacking and packing
coordinates = (10, 20, 30)
x, y, z = coordinates  # Unpacking
print(f"Unpacked: x={x}, y={y}, z={z}")

# Extended unpacking (Python 3+)
numbers = (1, 2, 3, 4, 5, 6)
first, *middle, last = numbers
print(f"First: {first}, Middle: {middle}, Last: {last}")

# Nested tuple structures
matrix = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print(f"Matrix[1][2]: {matrix[1][2]}")

# Named tuples for structured data
Point = namedtuple('Point', ['x', 'y', 'z'])
p1 = Point(1, 2, 3)
print(f"Named tuple: {p1}, x-coordinate: {p1.x}")

# ============================================================================
# DEEP DIVE: LISTS - DYNAMIC ARRAYS
# ============================================================================

print("\n=== LIST INTERNALS ===")

# List creation and memory allocation
my_list = [1, 2, 3, 4, 5]
print(f"List: {my_list}, Size: {sys.getsizeof(my_list)} bytes")

# Dynamic resizing demonstration
capacity_demo = []
for i in range(20):
    size_before = sys.getsizeof(capacity_demo)
    capacity_demo.append(i)
    size_after = sys.getsizeof(capacity_demo)
    if size_before != size_after:
        print(f"Capacity increased at length {len(capacity_demo)}: {size_before} -> {size_after} bytes")

# ============================================================================
# LIST METHODS AND OPERATIONS
# ============================================================================

print("\n=== ADVANCED LIST OPERATIONS ===")

# List comprehensions vs traditional loops
squares_traditional = []
for x in range(10):
    squares_traditional.append(x**2)

squares_comprehension = [x**2 for x in range(10)]
print(f"Squares (comprehension): {squares_comprehension}")

# Advanced list methods
data = [3, 1, 4, 1, 5, 9, 2, 6, 5]
print(f"Original: {data}")
print(f"Index of 5: {data.index(5)}")
print(f"Count of 1: {data.count(1)}")

# Sorting and reversing
data_copy = data.copy()
data_copy.sort()  # In-place sorting
print(f"Sorted: {data_copy}")

data_copy.reverse()  # In-place reversal
print(f"Reversed: {data_copy}")

# List slicing with step
numbers = list(range(20))
print(f"Every 3rd element: {numbers[::3]}")
print(f"Reverse slice: {numbers[::-1]}")
print(f"Middle section: {numbers[5:15:2]}")

# ============================================================================
# PERFORMANCE COMPARISONS
# ============================================================================

print("\n=== PERFORMANCE INSIGHTS ===")


# Tuple vs List creation time
tuple_time = timeit.timeit(lambda: (1, 2, 3, 4, 5), number=1000000)
list_time = timeit.timeit(lambda: [1, 2, 3, 4, 5], number=1000000)
print(f"Tuple creation time: {tuple_time:.6f}s")
print(f"List creation time: {list_time:.6f}s")

# Memory comparison
sample_data = range(1000)
tuple_memory = sys.getsizeof(tuple(sample_data))
list_memory = sys.getsizeof(list(sample_data))
print(f"Tuple memory (1000 items): {tuple_memory} bytes")
print(f"List memory (1000 items): {list_memory} bytes")

# ============================================================================
# ADVANCED PATTERNS AND USE CASES
# ============================================================================

print("\n=== ADVANCED PATTERNS ===")

# Using tuples as dictionary keys (immutable requirement)
location_data = {
    (0, 0): "Origin",
    (1, 1): "Northeast",
    (-1, -1): "Southwest"
}
print(f"Location at (1,1): {location_data[(1, 1)]}")

# Tuple as return values for multiple data
def get_name_age():
    return "Alice", 30  # Returns a tuple

name, age = get_name_age()
print(f"Returned data: {name}, {age}")

# List as stack (LIFO)
stack = [1, 2, 3]
stack.append(4)  # Push
top = stack.pop()  # Pop
print(f"Stack after pop: {stack}, popped: {top}")

# List as queue (less efficient, use collections.deque for real queues)
queue = [1, 2, 3]
queue.append(4)  # Enqueue
first = queue.pop(0)  # Dequeue (O(n) operation!)
print(f"Queue after dequeue: {queue}, dequeued: {first}")

# ============================================================================
# MEMORY AND REFERENCE BEHAVIOR
# ============================================================================

print("\n=== MEMORY BEHAVIOR ===")

# Shallow vs deep copying
original_list = [[1, 2], [3, 4]]
shallow_copy = original_list.copy()  # or original_list[:]
shallow_copy[0][0] = 999
print(f"Original after shallow copy modification: {original_list}")

deep_copy = copy.deepcopy(original_list)
deep_copy[0][0] = 111
print(f"Original after deep copy modification: {original_list}")

# List references vs copies
list1 = [1, 2, 3]
list2 = list1  # Reference
list3 = list1.copy()  # Copy
list1.append(4)
print(f"list1: {list1}")
print(f"list2 (reference): {list2}")
print(f"list3 (copy): {list3}")

# Tuple immutability with mutable contents
tuple_with_list = ([1, 2], [3, 4])
tuple_with_list[0].append(999)  # Modifying the list inside tuple
print(f"Tuple with modified list: {tuple_with_list}")

print("\n=== SUMMARY ===")
print("Tuples: Immutable, hashable, memory efficient, faster creation")
print("Lists: Mutable, dynamic, rich methods, flexible but more overhead")

# ============================================================================
# DEEP DIVE: NUMPY ARRAYS - HIGH-PERFORMANCE COMPUTING
# ============================================================================


print("\n=== NUMPY ARRAYS FUNDAMENTALS ===")

# Array creation methods
arr1 = np.array([1, 2, 3, 4, 5])  # From list
arr2 = np.zeros((3, 4))  # Zeros matrix
arr3 = np.ones((2, 3))  # Ones matrix
arr4 = np.arange(0, 10, 2)  # Range with step
arr5 = np.linspace(0, 1, 5)  # Linear spacing
arr6 = np.random.random((2, 3))  # Random values

print(f"Basic array: {arr1}")
print(f"Zeros matrix:\n{arr2}")
print(f"Arange: {arr4}")
print(f"Linspace: {arr5}")

# Array properties
print(f"\nArray shape: {arr2.shape}")
print(f"Array dtype: {arr1.dtype}")
print(f"Array size: {arr2.size}")
print(f"Array ndim: {arr2.ndim}")
print(f"Memory usage: {arr1.nbytes} bytes")

# ============================================================================
# ARRAY CREATION AND DATA TYPES
# ============================================================================

print("\n=== DATA TYPES AND MEMORY ===")

# Explicit data types
int_array = np.array([1, 2, 3], dtype=np.int32)
float_array = np.array([1, 2, 3], dtype=np.float64)
bool_array = np.array([True, False, True])

print(f"Int32 array: {int_array}, size: {int_array.nbytes} bytes")
print(f"Float64 array: {float_array}, size: {float_array.nbytes} bytes")
print(f"Bool array: {bool_array}, size: {bool_array.nbytes} bytes")

# Memory layout (C vs Fortran order)
c_order = np.array([[1, 2, 3], [4, 5, 6]], order='C')
f_order = np.array([[1, 2, 3], [4, 5, 6]], order='F')
print(f"C-order flags: {c_order.flags}")

# ============================================================================
# ADVANCED INDEXING AND SLICING
# ============================================================================

print("\n=== ADVANCED INDEXING ===")

# Multi-dimensional indexing
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"Matrix:\n{matrix}")
print(f"Element [1,2]: {matrix[1, 2]}")
print(f"Row 1: {matrix[1, :]}")
print(f"Column 2: {matrix[:, 2]}")

# Boolean indexing
data = np.array([1, 2, 3, 4, 5, 6])
mask = data > 3
print(f"Boolean mask: {mask}")
print(f"Filtered data: {data[mask]}")

# Fancy indexing
indices = np.array([0, 2, 4])
print(f"Fancy indexing: {data[indices]}")

# Advanced slicing
arr_3d = np.random.randint(0, 10, (3, 4, 5))
print(f"3D array shape: {arr_3d.shape}")
print(f"Slice [1, :, ::2]:\n{arr_3d[1, :, ::2]}")

# ============================================================================
# VECTORIZED OPERATIONS
# ============================================================================

print("\n=== VECTORIZED OPERATIONS ===")

# Element-wise operations
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

print(f"Addition: {a + b}")
print(f"Multiplication: {a * b}")
print(f"Power: {a ** 2}")
print(f"Square root: {np.sqrt(a)}")
print(f"Trigonometric: {np.sin(a)}")

# Broadcasting
scalar = 10
matrix = np.array([[1, 2], [3, 4]])
print(f"Scalar broadcasting:\n{matrix + scalar}")

# Different shapes broadcasting
row_vector = np.array([[1, 2, 3]])
col_vector = np.array([[1], [2], [3]])
print(f"Broadcasting result:\n{row_vector + col_vector}")

# ============================================================================
# ARRAY MANIPULATION
# ============================================================================

print("\n=== ARRAY MANIPULATION ===")

# Reshaping
original = np.arange(12)
reshaped = original.reshape(3, 4)
print(f"Original: {original}")
print(f"Reshaped (3x4):\n{reshaped}")

# Flattening
flattened = reshaped.flatten()  # Copy
raveled = reshaped.ravel()  # View when possible
print(f"Flattened: {flattened}")

# Concatenation and splitting
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

h_concat = np.hstack((arr1, arr2))
v_concat = np.vstack((arr1, arr2))
print(f"Horizontal concat:\n{h_concat}")
print(f"Vertical concat:\n{v_concat}")

# Splitting
split_arrays = np.hsplit(h_concat, 2)
print(f"Split result: {len(split_arrays)} arrays")

# ============================================================================
# MATHEMATICAL OPERATIONS
# ============================================================================

print("\n=== MATHEMATICAL OPERATIONS ===")

# Aggregation functions
data = np.random.randint(1, 10, (3, 4))
print(f"Data matrix:\n{data}")
print(f"Sum: {np.sum(data)}")
print(f"Mean: {np.mean(data)}")
print(f"Standard deviation: {np.std(data)}")
print(f"Min/Max: {np.min(data)}, {np.max(data)}")

# Axis-specific operations
print(f"Row sums: {np.sum(data, axis=1)}")
print(f"Column means: {np.mean(data, axis=0)}")

# Linear algebra
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

dot_product = np.dot(A, B)  # Matrix multiplication
print(f"Matrix multiplication:\n{dot_product}")
print(f"Determinant of A: {np.linalg.det(A)}")
print(f"Eigenvalues: {np.linalg.eigvals(A)}")

# ============================================================================
# PERFORMANCE COMPARISONS
# ============================================================================

print("\n=== PERFORMANCE COMPARISONS ===")

# NumPy vs Python list performance
size = 100000

# Setup
python_list = list(range(size))
numpy_array = np.arange(size)

# Sum operation timing
python_time = timeit.timeit(lambda: sum(python_list), number=100)
numpy_time = timeit.timeit(lambda: np.sum(numpy_array), number=100)

print(f"Python list sum time: {python_time:.6f}s")
print(f"NumPy array sum time: {numpy_time:.6f}s")
print(f"NumPy speedup: {python_time/numpy_time:.2f}x")

# Memory efficiency
print(f"Python list memory: {sys.getsizeof(python_list)} bytes")
print(f"NumPy array memory: {numpy_array.nbytes} bytes")

# ============================================================================
# ADVANCED NUMPY FEATURES
# ============================================================================

print("\n=== ADVANCED FEATURES ===")

# Universal functions (ufuncs)
def custom_func(x, y):
    return x**2 + y**2

vectorized_func = np.vectorize(custom_func)
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
result = vectorized_func(x, y)
print(f"Vectorized function result: {result}")

# Structured arrays
dt = np.dtype([('name', 'U20'), ('age', 'i4'), ('score', 'f8')])
students = np.array([('Alice', 20, 85.5), ('Bob', 21, 92.3)], dtype=dt)
print(f"Structured array:\n{students}")
print(f"Names: {students['name']}")

# Memory views and copies
original = np.arange(6).reshape(2, 3)
view = original[::2, ::2]  # Creates a view
copy_arr = original.copy()  # Creates a copy

original[0, 0] = 999
print(f"Original modified:\n{original}")
print(f"View affected:\n{view}")
print(f"Copy unaffected:\n{copy_arr}")

# ============================================================================
# REAL-WORLD APPLICATIONS
# ============================================================================

print("\n=== REAL-WORLD EXAMPLES ===")

# Image processing simulation (grayscale image)
image = np.random.randint(0, 256, (100, 100), dtype=np.uint8)
print(f"Image shape: {image.shape}, dtype: {image.dtype}")

# Apply a simple filter (blur)
kernel = np.ones((3, 3)) / 9
# Note: Real convolution would use scipy.ndimage or cv2
print("Image processing kernel created")

# Statistical analysis
data_sample = np.random.normal(100, 15, 1000)  # Normal distribution
print(f"Sample mean: {np.mean(data_sample):.2f}")
print(f"Sample std: {np.std(data_sample):.2f}")
print(f"95th percentile: {np.percentile(data_sample, 95):.2f}")

# Time series data
time = np.linspace(0, 2*np.pi, 100)
signal = np.sin(time) + 0.1 * np.random.random(100)
print(f"Signal shape: {signal.shape}")

print("\n=== NUMPY SUMMARY ===")
print("NumPy provides:")
print("- Homogeneous, typed arrays for numerical computing")
print("- Vectorized operations for performance")
print("- Broadcasting for operations on different shapes")
print("- Rich mathematical and linear algebra functions")
print("- Memory-efficient storage and views")
print("- Foundation for scientific Python ecosystem")






# ============================================================================
# USER INPUT WITH ARRAYS AND NUMPY ARRAYS
# ============================================================================

print("\n=== USER INPUT WITH ARRAYS ===")

# Getting user input for Python lists
def get_user_list():
    """Get a list of numbers from user input"""
    try:
        user_input = input("Enter numbers separated by spaces: ")
        # Convert string input to list of numbers
        numbers = [float(x) for x in user_input.split()]
        return numbers
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return []

# Getting user input for NumPy arrays
def get_user_numpy_array():
    """Get a NumPy array from user input"""
    try:
        user_input = input("Enter numbers for NumPy array (space-separated): ")
        numbers = [float(x) for x in user_input.split()]
        return np.array(numbers)
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return np.array([])

# Interactive matrix input
def get_user_matrix():
    """Get a matrix from user input"""
    try:
        rows = int(input("Enter number of rows: "))
        cols = int(input("Enter number of columns: "))
        
        matrix = []
        for i in range(rows):
            row_input = input(f"Enter row {i+1} ({cols} numbers): ")
            row = [float(x) for x in row_input.split()]
            if len(row) != cols:
                print(f"Error: Expected {cols} numbers, got {len(row)}")
                return np.array([])
            matrix.append(row)
        
        return np.array(matrix)
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        return np.array([])

# Example usage (commented out for automation)
# print("Example: Getting user input for arrays")
# user_list = get_user_list()
# if user_list:
#     print(f"Your list: {user_list}")
#     print(f"List operations - Sum: {sum(user_list)}, Max: {max(user_list)}")

# user_array = get_user_numpy_array()
# if user_array.size > 0:
#     print(f"Your NumPy array: {user_array}")
#     print(f"Array operations - Sum: {np.sum(user_array)}, Mean: {np.mean(user_array)}")

# user_matrix = get_user_matrix()
# if user_matrix.size > 0:
#     print(f"Your matrix:\n{user_matrix}")
#     print(f"Matrix shape: {user_matrix.shape}")

# ============================================================================
# ADVANCED INPUT VALIDATION AND PROCESSING
# ============================================================================

print("\n=== ADVANCED INPUT PROCESSING ===")

def safe_input_to_array(prompt, expected_length=None):
    """Safely convert user input to NumPy array with validation"""
    while True:
        try:
            user_input = input(prompt)
            if user_input.lower() == 'quit':
                return None
            
            # Handle different input formats
            if ',' in user_input:
                numbers = [float(x.strip()) for x in user_input.split(',')]
            else:
                numbers = [float(x) for x in user_input.split()]
            
            if expected_length and len(numbers) != expected_length:
                print(f"Expected {expected_length} numbers, got {len(numbers)}")
                continue
                
            return np.array(numbers)
            
        except ValueError:
            print("Invalid input. Please enter numbers only (or 'quit' to exit).")
        except KeyboardInterrupt:
            print("\nOperation cancelled.")
            return None

def input_with_range(prompt, min_val=None, max_val=None):
    """Get array input with value range validation"""
    array = safe_input_to_array(prompt)
    if array is None:
        return None
    
    # Validate range
    if min_val is not None and np.any(array < min_val):
        print(f"Warning: Some values are below minimum ({min_val})")
    if max_val is not None and np.any(array > max_val):
        print(f"Warning: Some values are above maximum ({max_val})")
    
    return array

# Example with validation (commented for automation)
# print("Example: Input with validation")
# validated_array = safe_input_to_array("Enter 5 numbers: ", expected_length=5)
# if validated_array is not None:
#     print(f"Validated array: {validated_array}")

# ============================================================================
# FILE INPUT/OUTPUT FOR ARRAYS
# ============================================================================

print("\n=== FILE I/O FOR ARRAYS ===")

def save_array_to_file(array, filename):
    """Save NumPy array to file"""
    try:
        np.save(filename, array)
        print(f"Array saved to {filename}.npy")
    except Exception as e:
        print(f"Error saving array: {e}")

def load_array_from_file(filename):
    """Load NumPy array from file"""
    try:
        array = np.load(f"{filename}.npy")
        print(f"Array loaded from {filename}.npy")
        return array
    except Exception as e:
        print(f"Error loading array: {e}")
        return None

def save_array_as_text(array, filename):
    """Save array as human-readable text"""
    try:
        np.savetxt(f"{filename}.txt", array, fmt='%.2f')
        print(f"Array saved as text to {filename}.txt")
    except Exception as e:
        print(f"Error saving as text: {e}")

def load_array_from_text(filename):
    """Load array from text file"""
    try:
        array = np.loadtxt(f"{filename}.txt")
        print(f"Array loaded from {filename}.txt")
        return array
    except Exception as e:
        print(f"Error loading from text: {e}")
        return None

# Example array for file operations
sample_array = np.random.rand(5, 3)
print(f"Sample array for file operations:\n{sample_array}")

# Demonstrate file operations (using temporary filename)
temp_filename = "temp_array"
save_array_to_file(sample_array, temp_filename)
loaded_array = load_array_from_file(temp_filename)
if loaded_array is not None:
    print(f"Loaded array matches original: {np.array_equal(sample_array, loaded_array)}")

# Text file operations
save_array_as_text(sample_array, temp_filename)
text_loaded = load_array_from_text(temp_filename)

# ============================================================================
# INTERACTIVE ARRAY CALCULATOR
# ============================================================================

print("\n=== INTERACTIVE ARRAY CALCULATOR ===")

class ArrayCalculator:
    """Interactive calculator for array operations"""
    
    def __init__(self):
        self.arrays = {}
        
    def add_array(self, name):
        """Add a named array from user input"""
        print(f"Adding array '{name}'")
        array = safe_input_to_array(f"Enter values for {name}: ")
        if array is not None:
            self.arrays[name] = array
            print(f"Array '{name}' added: {array}")
        
    def list_arrays(self):
        """List all stored arrays"""
        if not self.arrays:
            print("No arrays stored.")
            return
        
        for name, array in self.arrays.items():
            print(f"{name}: {array}")
    
    def operate_arrays(self, name1, name2, operation):
        """Perform operation between two arrays"""
        if name1 not in self.arrays or name2 not in self.arrays:
            print("One or both arrays not found.")
            return
        
        a1, a2 = self.arrays[name1], self.arrays[name2]
        
        try:
            if operation == 'add':
                result = a1 + a2
            elif operation == 'subtract':
                result = a1 - a2
            elif operation == 'multiply':
                result = a1 * a2
            elif operation == 'dot':
                result = np.dot(a1, a2)
            else:
                print("Unknown operation")
                return
            
            print(f"Result of {name1} {operation} {name2}: {result}")
            return result
            
        except Exception as e:
            print(f"Operation failed: {e}")

# Example calculator usage (interactive part commented)
calculator = ArrayCalculator()
print("Array Calculator created")

# Demonstrate with predefined arrays
calculator.arrays['a'] = np.array([1, 2, 3])
calculator.arrays['b'] = np.array([4, 5, 6])
calculator.list_arrays()
calculator.operate_arrays('a', 'b', 'add')
calculator.operate_arrays('a', 'b', 'multiply')

# ============================================================================
# CSV AND STRUCTURED DATA INPUT
# ============================================================================

print("\n=== CSV AND STRUCTURED DATA ===")

def create_sample_csv():
    """Create a sample CSV file for demonstration"""
    data = """Name,Age,Score
Alice,25,85.5
Bob,30,92.3
Charlie,28,78.9
Diana,35,95.1"""
    
    with open("sample_data.csv", "w") as f:
        f.write(data)
    print("Sample CSV file created")

def load_csv_as_array():
    """Load CSV data as NumPy array"""
    try:
        create_sample_csv()
        # Load only numeric columns
        data = np.loadtxt("sample_data.csv", delimiter=',', skiprows=1, usecols=(1, 2))
        print("CSV data loaded as NumPy array:")
        print("Columns: Age, Score")
        print(data)
        return data
    except Exception as e:
        print(f"Error loading CSV: {e}")
        return None

# Load and analyze CSV data
csv_data = load_csv_as_array()
if csv_data is not None:
    print(f"Average age: {np.mean(csv_data[:, 0]):.1f}")
    print(f"Average score: {np.mean(csv_data[:, 1]):.1f}")
    print(f"Correlation coefficient: {np.corrcoef(csv_data[:, 0], csv_data[:, 1])[0, 1]:.3f}")

print("\n=== USER INPUT SUMMARY ===")
print("Key concepts for user input with arrays:")
print("- Input validation and error handling")
print("- Converting strings to numeric arrays")
print("- File I/O for persistent storage")
print("- Interactive array operations")
print("- Structured data handling (CSV)")
print("- Safe input practices with try-except blocks")


class MemoryInspector:
    """Class for memory analysis and inspection utilities"""
    
    def __init__(self):
        self.tracked_objects = {}
    
    def inspect_object(self, obj, name="object"):
        """Inspect memory properties of an object"""
        obj_id = id(obj)
        obj_size = sys.getsizeof(obj)
        obj_type = type(obj).__name__
        
        info = {
            'name': name,
            'id': obj_id,
            'size': obj_size,
            'type': obj_type,
            'value': obj
        }
        
        self.tracked_objects[name] = info
        return info
    
    def compare_objects(self, obj1, obj2, name1="obj1", name2="obj2"):
        """Compare memory properties of two objects"""
        info1 = self.inspect_object(obj1, name1)
        info2 = self.inspect_object(obj2, name2)
        
        print(f"\n=== MEMORY COMPARISON ===")
        print(f"{name1}: ID={info1['id']}, Size={info1['size']}, Type={info1['type']}")
        print(f"{name2}: ID={info2['id']}, Size={info2['size']}, Type={info2['type']}")
        print(f"Same object in memory: {info1['id'] == info2['id']}")
        print(f"Size difference: {abs(info1['size'] - info2['size'])} bytes")
        
        return info1, info2
    
    def get_memory_view(self, obj):
        """Get memory view of an object if possible"""
        try:
            if hasattr(obj, 'tobytes') or isinstance(obj, (bytes, bytearray)):
                return memoryview(obj)
            elif isinstance(obj, np.ndarray):
                return memoryview(obj)
            else:
                print(f"Cannot create memory view for {type(obj)}")
                return None
        except Exception as e:
            print(f"Error creating memory view: {e}")
            return None


class TupleManager:
    """Enhanced tuple operations and management"""
    
    def __init__(self):
        self.memory_inspector = MemoryInspector()
        self.created_tuples = []
    
    def create_tuple(self, *args, name=None):
        """Create and track a tuple"""
        new_tuple = tuple(args)
        self.created_tuples.append(new_tuple)
        
        if name:
            self.memory_inspector.inspect_object(new_tuple, name)
        
        return new_tuple
    
    def demonstrate_immutability(self):
        """Demonstrate tuple immutability and memory behavior"""
        print("\n=== TUPLE IMMUTABILITY DEMONSTRATION ===")
        
        # Create original tuple
        original = self.create_tuple(1, 2, 3, name="original")
        print(f"Original tuple: {original}, ID: {id(original)}")
        
        # Attempt to "modify" (creates new tuple)
        try:
            # This creates a new tuple, not modifying the original
            modified = original + (4,)
            self.memory_inspector.compare_objects(original, modified, "original", "modified")
            
            # Demonstrate that original is unchanged
            print(f"Original unchanged: {original}")
            print(f"New tuple created: {modified}")
            
        except Exception as e:
            print(f"Error: {e}")
    
    def analyze_tuple_interning(self):
        """Analyze tuple interning behavior"""
        print("\n=== TUPLE INTERNING ANALYSIS ===")
        
        # Small tuples might be interned
        t1 = (1, 2)
        t2 = (1, 2)
        self.memory_inspector.compare_objects(t1, t2, "small_tuple_1", "small_tuple_2")
        
        # Larger tuples usually not interned
        large1 = tuple(range(100))
        large2 = tuple(range(100))
        self.memory_inspector.compare_objects(large1, large2, "large_tuple_1", "large_tuple_2")


class ListManager:
    """Enhanced list operations and management"""
    
    def __init__(self):
        self.memory_inspector = MemoryInspector()
        self.created_lists = []
    
    def create_list(self, *args, name=None):
        """Create and track a list"""
        new_list = list(args)
        self.created_lists.append(new_list)
        
        if name:
            self.memory_inspector.inspect_object(new_list, name)
        
        return new_list
    
    def demonstrate_mutability(self):
        """Demonstrate list mutability and memory behavior"""
        print("\n=== LIST MUTABILITY DEMONSTRATION ===")
        
        # Create original list
        original = self.create_list(1, 2, 3, name="original_list")
        original_id = id(original)
        print(f"Original list: {original}, ID: {original_id}")
        
        # Modify in place
        original.append(4)
        print(f"After append: {original}, ID: {id(original)}")
        print(f"Same object: {id(original) == original_id}")
        
        # Demonstrate reference vs copy
        reference = original
        copy_list = original.copy()
        
        original.append(5)
        print(f"Original: {original}")
        print(f"Reference: {reference}")
        print(f"Copy: {copy_list}")
    
    def analyze_capacity_growth(self):
        """Analyze how list capacity grows"""
        print("\n=== LIST CAPACITY GROWTH ===")
        
        dynamic_list = []
        prev_size = sys.getsizeof(dynamic_list)
        
        for i in range(20):
            dynamic_list.append(i)
            current_size = sys.getsizeof(dynamic_list)
            if current_size != prev_size:
                print(f"Length {len(dynamic_list)}: {prev_size} -> {current_size} bytes")
                prev_size = current_size


class ArrayManager:
    """NumPy array operations and management"""
    
    def __init__(self):
        self.memory_inspector = MemoryInspector()
        self.created_arrays = []
    
    def create_array(self, data, dtype=None, name=None):
        """Create and track a NumPy array"""
        new_array = np.array(data, dtype=dtype)
        self.created_arrays.append(new_array)
        
        if name:
            self.memory_inspector.inspect_object(new_array, name)
        
        return new_array
    
    def demonstrate_memory_layout(self):
        """Demonstrate NumPy memory layout"""
        print("\n=== NUMPY MEMORY LAYOUT ===")
        
        # Different data types
        int_arr = self.create_array([1, 2, 3, 4], dtype=np.int32, name="int32_array")
        float_arr = self.create_array([1, 2, 3, 4], dtype=np.float64, name="float64_array")
        
        print(f"Int32 array: {int_arr.nbytes} bytes")
        print(f"Float64 array: {float_arr.nbytes} bytes")
        
        # Memory view demonstration
        mv = self.memory_inspector.get_memory_view(int_arr)
        if mv:
            print(f"Memory view created: {len(mv)} bytes")
            print(f"First 4 bytes: {mv[:4].tobytes()}")
    
    def demonstrate_views_vs_copies(self):
        """Demonstrate views vs copies in NumPy"""
        print("\n=== VIEWS VS COPIES ===")
        
        original = self.create_array([[1, 2, 3], [4, 5, 6]], name="original_array")
        
        # Create a view
        view = original[::2, ::2]  # Every other element
        print(f"Original base: {original.base is None}")
        print(f"View base: {view.base is original}")
        
        # Create a copy
        copy_arr = original.copy()
        print(f"Copy base: {copy_arr.base is None}")
        
        # Modify original and see effects
        original[0, 0] = 999
        print(f"Original: {original}")
        print(f"View: {view}")
        print(f"Copy: {copy_arr}")


class UserInputManager:
    """Enhanced user input handling for arrays"""
    
    def __init__(self):
        self.memory_inspector = MemoryInspector()
        self.validators = {
            'numeric': self._validate_numeric,
            'positive': self._validate_positive,
            'range': self._validate_range
        }
    
    def _validate_numeric(self, value):
        """Validate if value is numeric"""
        try:
            float(value)
            return True
        except ValueError:
            return False
    
    def _validate_positive(self, value):
        """Validate if value is positive"""
        try:
            return float(value) > 0
        except ValueError:
            return False
    
    def _validate_range(self, value, min_val=0, max_val=100):
        """Validate if value is within range"""
        try:
            num = float(value)
            return min_val <= num <= max_val
        except ValueError:
            return False
    
    def get_validated_input(self, prompt, validator_type='numeric', **kwargs):
        """Get validated user input"""
        validator = self.validators.get(validator_type)
        if not validator:
            raise ValueError(f"Unknown validator: {validator_type}")
        
        while True:
            try:
                user_input = input(prompt)
                if user_input.lower() == 'quit':
                    return None
                
                if validator_type == 'range':
                    if validator(user_input, **kwargs):
                        return float(user_input)
                elif validator(user_input):
                    return float(user_input)
                
                print("Invalid input. Please try again.")
                
            except KeyboardInterrupt:
                print("\nOperation cancelled.")
                return None
    
    def create_array_from_input(self, array_type='numpy'):
        """Create array from user input with validation"""
        print(f"\n=== CREATING {array_type.upper()} ARRAY ===")
        
        # Get array size
        size = self.get_validated_input("Enter array size (or 'quit'): ", 'positive')
        if size is None:
            return None
        
        size = int(size)
        elements = []
        
        # Get array elements
        for i in range(size):
            element = self.get_validated_input(f"Enter element {i+1}: ")
            if element is None:
                return None
            elements.append(element)
        
        # Create appropriate array type
        if array_type == 'numpy':
            result = np.array(elements)
        else:
            result = elements
        
        # Inspect memory
        self.memory_inspector.inspect_object(result, f"user_{array_type}_array")
        return result


class FileManager:
    """File I/O operations for different array types"""
    
    def __init__(self):
        self.memory_inspector = MemoryInspector()
    
    def save_data(self, data, filename, format_type='numpy'):
        """Save data in specified format"""
        try:
            if format_type == 'numpy':
                np.save(f"{filename}.npy", data)
            elif format_type == 'text':
                if isinstance(data, np.ndarray):
                    np.savetxt(f"{filename}.txt", data)
                else:
                    with open(f"{filename}.txt", 'w') as f:
                        for item in data:
                            f.write(f"{item}\n")
            elif format_type == 'binary':
                with open(f"{filename}.bin", 'wb') as f:
                    if isinstance(data, np.ndarray):
                        f.write(data.tobytes())
                    else:
                        # Convert list to bytes
                        byte_data = str(data).encode()
                        f.write(byte_data)
            
            print(f"Data saved as {format_type} format to {filename}")
            return True
            
        except Exception as e:
            print(f"Error saving data: {e}")
            return False
    
    def load_data(self, filename, format_type='numpy'):
        """Load data from specified format"""
        try:
            if format_type == 'numpy':
                data = np.load(f"{filename}.npy")
            elif format_type == 'text':
                data = np.loadtxt(f"{filename}.txt")
            elif format_type == 'binary':
                with open(f"{filename}.bin", 'rb') as f:
                    raw_data = f.read()
                    # For demonstration, assume it's numpy array bytes
                    data = np.frombuffer(raw_data, dtype=np.float64)
            
            self.memory_inspector.inspect_object(data, f"loaded_{format_type}_data")
            return data
            
        except Exception as e:
            print(f"Error loading data: {e}")
            return None


class DataStructureFactory:
    """Factory pattern for creating different data structures"""
    
    def __init__(self):
        self.memory_inspector = MemoryInspector()
        self.tuple_manager = TupleManager()
        self.list_manager = ListManager()
        self.array_manager = ArrayManager()
    
    def create_structure(self, structure_type, data, **kwargs):
        """Factory method to create data structures"""
        if structure_type == 'tuple':
            return self.tuple_manager.create_tuple(*data, **kwargs)
        elif structure_type == 'list':
            return self.list_manager.create_list(*data, **kwargs)
        elif structure_type == 'numpy':
            return self.array_manager.create_array(data, **kwargs)
        else:
            raise ValueError(f"Unknown structure type: {structure_type}")
    
    def benchmark_structures(self, data_size=1000):
        """Benchmark different data structures"""
        print(f"\n=== BENCHMARKING STRUCTURES (size={data_size}) ===")
        
        test_data = list(range(data_size))
        
        # Benchmark creation time
        for structure_type in ['tuple', 'list', 'numpy']:
            start_time = timeit.default_timer()
            for _ in range(100):
                self.create_structure(structure_type, test_data)
            end_time = timeit.default_timer()
            
            avg_time = (end_time - start_time) / 100
            print(f"{structure_type} creation time: {avg_time:.6f}s")
        
        # Memory comparison
        tuple_obj = tuple(test_data)
        list_obj = list(test_data)
        array_obj = np.array(test_data)
        
        print(f"Tuple memory: {sys.getsizeof(tuple_obj)} bytes")
        print(f"List memory: {sys.getsizeof(list_obj)} bytes")
        print(f"NumPy memory: {array_obj.nbytes} bytes")


# ============================================================================
# DEMONSTRATION OF OOP IMPLEMENTATION
# ============================================================================

def demonstrate_oop_approach():
    """Demonstrate the OOP approach to array and memory management"""
    
    print("=== OBJECT-ORIENTED APPROACH DEMONSTRATION ===")
    
    # Create factory instance
    factory = DataStructureFactory()
    
    # Memory inspector demonstration
    print("\n--- Memory Inspector ---")
    inspector = MemoryInspector()
    
    obj1 = [1, 2, 3]
    obj2 = [1, 2, 3]
    inspector.compare_objects(obj1, obj2)
    
    # Tuple manager demonstration
    print("\n--- Tuple Manager ---")
    tuple_mgr = TupleManager()
    tuple_mgr.demonstrate_immutability()
    tuple_mgr.analyze_tuple_interning()
    
    # List manager demonstration
    print("\n--- List Manager ---")
    list_mgr = ListManager()
    list_mgr.demonstrate_mutability()
    list_mgr.analyze_capacity_growth()
    
    # Array manager demonstration
    print("\n--- Array Manager ---")
    array_mgr = ArrayManager()
    array_mgr.demonstrate_memory_layout()
    array_mgr.demonstrate_views_vs_copies()
    
    # File manager demonstration
    print("\n--- File Manager ---")
    file_mgr = FileManager()
    test_array = np.array([1, 2, 3, 4, 5])
    file_mgr.save_data(test_array, "test_data", "numpy")
    loaded_data = file_mgr.load_data("test_data", "numpy")
    print(f"Data saved and loaded successfully: {np.array_equal(test_array, loaded_data)}")
    
    # Factory pattern demonstration
    print("\n--- Factory Pattern ---")
    factory.benchmark_structures(1000)
    
    # User input manager (interactive part commented for automation)
    print("\n--- User Input Manager ---")
    input_mgr = UserInputManager()
    print("User input manager created (interactive methods available)")
    
    # Example of creating structures through factory
    sample_data = [1, 2, 3, 4, 5]
    
    tuple_result = factory.create_structure('tuple', sample_data, name="factory_tuple")
    list_result = factory.create_structure('list', sample_data, name="factory_list")
    array_result = factory.create_structure('numpy', sample_data, name="factory_array")
    
    print(f"Factory created tuple: {tuple_result}")
    print(f"Factory created list: {list_result}")
    print(f"Factory created array: {array_result}")

# Run the OOP demonstration
demonstrate_oop_approach()

print("\n=== OOP SUMMARY ===")
print("Object-Oriented approach provides:")
print("- Encapsulation of related functionality")
print("- Reusable and maintainable code structure")
print("- Factory pattern for creating different data structures")
print("- Separation of concerns (memory inspection, file I/O, etc.)")
print("- Extensible design for adding new features")
print("- Better error handling and validation")






