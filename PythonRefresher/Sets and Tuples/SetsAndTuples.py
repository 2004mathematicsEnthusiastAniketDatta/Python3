import sys
from collections import namedtuple
import sys
import timeit
import copy

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






















