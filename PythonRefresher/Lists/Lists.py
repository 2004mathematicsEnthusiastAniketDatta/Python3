import sys
from functools import reduce
from collections import deque
import copy
from operator import itemgetter
from itertools import chain, combinations, permutations

"""
Lists are a collection of data
"""


my_list = [80, 96, 72, 100, 8]
print(my_list)
my_list.append(1000)
print(my_list)
my_list.insert(2, 1000)
print(my_list)
my_list.remove(8)
print(my_list)
my_list.pop(0)
print(my_list)
my_list.sort()
print(my_list)


# Basic List Operations and Techniques

# 1. List Comprehensions - Pythonic way to create lists
squares = [x**2 for x in range(10)]
print(f"Squares: {squares}")

# Conditional list comprehension
evens = [x for x in range(20) if x % 2 == 0]
print(f"Even numbers: {evens}")

# Nested list comprehension
matrix = [[i*j for j in range(1, 4)] for i in range(1, 4)]
print(f"Matrix: {matrix}")

# 2. Advanced Slicing
data = list(range(20))
print(f"Original: {data}")
print(f"Every 2nd element: {data[::2]}")
print(f"Reverse: {data[::-1]}")
print(f"Last 5 elements: {data[-5:]}")

# 3. List Methods Deep Dive
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
print(f"Count of 1: {numbers.count(1)}")
print(f"Index of 4: {numbers.index(4)}")
numbers.reverse()
print(f"Reversed: {numbers}")

# 4. Memory Efficiency - Generator vs List
list_comp = [x for x in range(1000)]
gen_exp = (x for x in range(1000))
print(f"List size: {sys.getsizeof(list_comp)} bytes")
print(f"Generator size: {sys.getsizeof(gen_exp)} bytes")

# 5. Functional Programming with Lists
nums = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, nums))
filtered = list(filter(lambda x: x > 2, nums))
sum_all = reduce(lambda x, y: x + y, nums)
print(f"Mapped: {squared}, Filtered: {filtered}, Reduced: {sum_all}")

# 6. List as Stack and Queue
stack = []
stack.append(1)
stack.append(2)
stack.append(3)
print(f"Stack: {stack}")
print(f"Popped: {stack.pop()}")

queue = deque([1, 2, 3])
queue.append(4)
print(f"Queue: {list(queue)}")
print(f"Dequeued: {queue.popleft()}")

# 7. Shallow vs Deep Copy
original = [[1, 2, 3], [4, 5, 6]]
shallow = original.copy()
deep = copy.deepcopy(original)
original[0][0] = 999
print(f"Original: {original}")
print(f"Shallow: {shallow}")
print(f"Deep: {deep}")

# 8. Performance Optimization
# Pre-allocate list size when possible
large_list = [None] * 1000000  # More efficient than repeated appends

# Use list() constructor for iteration
string_list = list("hello")
print(f"String to list: {string_list}")

# 9. Advanced Sorting
students = [('Alice', 85), ('Bob', 90), ('Charlie', 78)]
students.sort(key=lambda x: x[1], reverse=True)  # Sort by grade
print(f"Sorted by grade: {students}")

# Multiple criteria sorting
data = [('John', 'A', 15), ('Jane', 'B', 12), ('Dave', 'B', 10)]
data.sort(key=itemgetter(1, 2))  # Sort by grade, then age
print(f"Multi-criteria sort: {data}")

# 10. List Unpacking and Packing
a, b, *rest = [1, 2, 3, 4, 5]
print(f"a: {a}, b: {b}, rest: {rest}")

# 11. Enumerate and Zip
colors = ['red', 'green', 'blue']
for i, color in enumerate(colors):
    print(f"Index {i}: {color}")

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
zipped = list(zip(list1, list2))
print(f"Zipped: {zipped}")

# 12. List Flattening
nested = [[1, 2], [3, 4], [5, 6]]
flattened = [item for sublist in nested for item in sublist]
print(f"Flattened: {flattened}")

# Using itertools for complex operations
flattened_chain = list(chain.from_iterable(nested))
print(f"Chain flattened: {flattened_chain}")

# Combinations and permutations
items = [1, 2, 3]
combos = list(combinations(items, 2))
perms = list(permutations(items, 2))
print(f"Combinations: {combos}")
print(f"Permutations: {perms}")









