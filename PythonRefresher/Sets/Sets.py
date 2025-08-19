"""
PYTHON SETS -  BASICS
===========================================================

This comprehensive guide covers sets from basic operations to advanced mathematical problems,
including memory-level insights and complex algorithmic challenges.
"""


# ============================================================================
# PART 1: SETS FUNDAMENTALS & MEMORY ANALYSIS
# ============================================================================

import sys
import time


print("=" * 80)
print("PYTHON SETS: BASICS")
print("=" * 80)

# Basic set creation and memory footprint
def analyze_set_memory():
    """Analyze memory usage of different set operations"""
    
    # Empty set vs list vs dict memory comparison
    empty_set = set()
    empty_list = []
    empty_dict = {}
    
    print(f"Empty set size: {sys.getsizeof(empty_set)} bytes")
    print(f"Empty list size: {sys.getsizeof(empty_list)} bytes")
    print(f"Empty dict size: {sys.getsizeof(empty_dict)} bytes")
    
    # Set with elements
    small_set = {1, 2, 3, 4, 5}
    medium_set = set(range(100))
    large_set = set(range(10000))
    
    print(f"\nSet with 5 elements: {sys.getsizeof(small_set)} bytes")
    print(f"Set with 100 elements: {sys.getsizeof(medium_set)} bytes")
    print(f"Set with 10000 elements: {sys.getsizeof(large_set)} bytes")
    
    # Hash table load factor analysis
    print(f"\nLoad factor analysis:")
    print(f"Small set length: {len(small_set)}, memory: {sys.getsizeof(small_set)}")
    print(f"Estimated slots: {sys.getsizeof(small_set) // 8}")  # Rough estimation

analyze_set_memory()

# ============================================================================
# PART 2: SET OPERATIONS & ALGORITHMIC COMPLEXITY
# ============================================================================

def demonstrate_set_operations():
    """Comprehensive demonstration of all set operations"""
    
    # Create sample sets
    A = {1, 2, 3, 4, 5, 6}
    B = {4, 5, 6, 7, 8, 9}
    C = {6, 7, 8, 9, 10, 11}
    
    print(f"\nSet A: {A}")
    print(f"Set B: {B}")
    print(f"Set C: {C}")
    
    # Union operations
    print(f"\nUNION OPERATIONS:")
    print(f"A ∪ B: {A | B}")
    print(f"A.union(B): {A.union(B)}")
    print(f"A ∪ B ∪ C: {A | B | C}")
    
    # Intersection operations
    print(f"\nINTERSECTION OPERATIONS:")
    print(f"A ∩ B: {A & B}")
    print(f"A.intersection(B): {A.intersection(B)}")
    print(f"A ∩ B ∩ C: {A & B & C}")
    
    # Difference operations
    print(f"\nDIFFERENCE OPERATIONS:")
    print(f"A - B: {A - B}")
    print(f"B - A: {B - A}")
    print(f"A.difference(B): {A.difference(B)}")
    
    # Symmetric difference
    print(f"\nSYMMETRIC DIFFERENCE:")
    print(f"A △ B: {A ^ B}")
    print(f"A.symmetric_difference(B): {A.symmetric_difference(B)}")
    
    # Subset and superset operations
    print(f"\nSUBSET/SUPERSET OPERATIONS:")
    D = {1, 2, 3}
    print(f"D = {D}")
    print(f"D ⊆ A (D.issubset(A)): {D.issubset(A)}")
    print(f"A ⊇ D (A.issuperset(D)): {A.issuperset(D)}")
    print(f"D ⊂ A (D < A): {D < A}")  # Proper subset
    
    # Disjoint sets
    E = {10, 11, 12}
    print(f"E = {E}")
    print(f"A and E are disjoint: {A.isdisjoint(E)}")

demonstrate_set_operations()

# ============================================================================
# PART 3: PERFORMANCE ANALYSIS - TIME COMPLEXITY
# ============================================================================

def performance_analysis():
    """Analyze time complexity of set operations vs other data structures"""
    
    def time_operation(operation, iterations=1000):
        start_time = time.time()
        for _ in range(iterations):
            operation()
        return time.time() - start_time
    
    # Setup data structures
    large_set = set(range(10000))
    large_list = list(range(10000))
    target = 8888
    
    print(f"\nPERFORMANCE ANALYSIS (10000 elements, 1000 iterations):")
    print("-" * 60)
    
    # Membership testing
    set_lookup_time = time_operation(lambda: target in large_set)
    list_lookup_time = time_operation(lambda: target in large_list)
    
    print(f"Set membership test: {set_lookup_time:.6f} seconds")
    print(f"List membership test: {list_lookup_time:.6f} seconds")
    print(f"Set is {list_lookup_time/set_lookup_time:.1f}x faster for lookup")
    
    # Addition operations
    def add_to_set():
        s = set()
        for i in range(100):
            s.add(i)
    
    def append_to_list():
        l = []
        for i in range(100):
            l.append(i)
    
    set_add_time = time_operation(add_to_set, 100)
    list_add_time = time_operation(append_to_list, 100)
    
    print(f"\nSet addition (100 elements): {set_add_time:.6f} seconds")
    print(f"List append (100 elements): {list_add_time:.6f} seconds")

performance_analysis()

# ============================================================================
# PART 4: ADVANCED MATHEMATICAL PROBLEMS WITH SETS
# ============================================================================

def sieve_of_eratosthenes(n):
    """
    HARD PROBLEM 1: Prime Number Generation using Set Operations
    Generate all prime numbers up to n using sets
    """
    if n < 2:
        return set()
    
    # Initialize set with all numbers from 2 to n
    candidates = set(range(2, n + 1))
    primes = set()
    
    while candidates:
        # Get the smallest remaining candidate (it's prime)
        prime = min(candidates)
        primes.add(prime)
        
        # Remove all multiples of this prime
        multiples = set(range(prime * prime, n + 1, prime))
        candidates -= multiples
        candidates.discard(prime)
    
    return primes

def goldbach_conjecture_verification(n):
    """
    HARD PROBLEM 2: Goldbach Conjecture Verification
    Every even number > 2 can be expressed as sum of two primes
    """
    if n <= 2 or n % 2 != 0:
        return False, []
    
    primes = sieve_of_eratosthenes(n)
    
    # Find pairs of primes that sum to n
    pairs = []
    for p in primes:
        complement = n - p
        if complement in primes and p <= complement:
            pairs.append((p, complement))
    
    return len(pairs) > 0, pairs

def solve_subset_sum_problem(arr, target_sum):
    """
    HARD PROBLEM 3: Subset Sum Problem using Sets
    Dynamic Programming approach with sets
    """
    n = len(arr)
    
    # dp[i] will store all possible sums with first i elements
    dp = [set() for _ in range(n + 1)]
    dp[0].add(0)  # Base case: empty subset sums to 0
    
    # Track subsets for reconstruction
    parent = {}
    
    for i in range(1, n + 1):
        dp[i] = dp[i-1].copy()  # Don't include current element
        
        # Include current element
        for s in dp[i-1]:
            new_sum = s + arr[i-1]
            if new_sum not in dp[i]:
                dp[i].add(new_sum)
                parent[new_sum] = (s, i-1)
    
    if target_sum not in dp[n]:
        return False, []
    
    # Reconstruct subset
    subset = []
    current_sum = target_sum
    while current_sum in parent:
        prev_sum, index = parent[current_sum]
        subset.append(arr[index])
        current_sum = prev_sum
    
    return True, subset[::-1]

def set_cover_problem(universe, subsets):
    """
    HARD PROBLEM 4: Set Cover Problem (Greedy Approximation)
    Find minimum number of subsets that cover the universe
    """
    universe = set(universe)
    subsets = [set(s) for s in subsets]
    covered = set()
    solution = []
    
    while covered != universe:
        # Greedy choice: pick subset covering most uncovered elements
        best_subset = None
        max_new_coverage = 0
        best_index = -1
        
        for i, subset in enumerate(subsets):
            if i in [sol[1] for sol in solution]:  # Skip already used subsets
                continue
            
            new_coverage = len(subset - covered)
            if new_coverage > max_new_coverage:
                max_new_coverage = new_coverage
                best_subset = subset
                best_index = i
        
        if best_subset is None:
            break  # No more subsets can add coverage
        
        covered |= best_subset
        solution.append((best_subset, best_index))
    
    return solution, len(solution)


