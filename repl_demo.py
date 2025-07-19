#!/usr/bin/env python3
"""
REPL Demonstration Script
========================

This script demonstrates REPL internals and provides an interactive example.
Run this to see how a simplified REPL works internally.
"""

import sys
import ast
import dis
from typing import Any, Optional
import traceback

def demonstrate_repl_phases():
    """Demonstrate each phase of the REPL cycle"""
    print("🔄 REPL CYCLE DEMONSTRATION")
    print("=" * 30)
    
    # Sample inputs to process
    test_inputs = [
        "2 + 3",
        "x = 10",
        "x * 2",
        "def greet(name): return f'Hello, {name}!'",
        "greet('World')",
        "import math; math.pi",
        "[i**2 for i in range(5)]"
    ]
    
    # Simulate REPL environment
    repl_namespace = {'__name__': '__main__'}
    
    for i, source in enumerate(test_inputs, 1):
        print(f"\n--- Command {i} ---")
        print(f"INPUT: {source}")
        
        try:
            # READ phase (simulated - we already have the input)
            print("📖 READ: Input received")
            
            # PARSE and COMPILE phase
            print("🔧 COMPILE: Parsing and compiling...")
            
            # Try as expression first
            try:
                code_obj = compile(source, '<stdin>', 'eval')
                is_expression = True
                print("   → Compiled as expression")
            except SyntaxError:
                # If that fails, try as statement
                code_obj = compile(source, '<stdin>', 'exec')
                is_expression = False
                print("   → Compiled as statement")
            
            # Show bytecode for expressions (keep it simple)
            if is_expression and len(source) < 20:
                print("   Bytecode:")
                dis.dis(code_obj)
            
            # EVAL phase
            print("⚡ EVAL: Executing code...")
            if is_expression:
                result = eval(code_obj, repl_namespace)
            else:
                exec(code_obj, repl_namespace)
                result = None
            
            # PRINT phase
            print("📺 PRINT: Displaying result...")
            if result is not None:
                print(f"   OUTPUT: {repr(result)}")
                # Store in _ like real Python REPL
                repl_namespace['_'] = result
            else:
                print("   OUTPUT: (no output)")
                
        except Exception as e:
            print(f"❌ ERROR: {type(e).__name__}: {e}")
        
        print("🔄 LOOP: Ready for next command")
    
    print(f"\n📋 Final namespace contents: {list(repl_namespace.keys())}")

def show_repl_internals():
    """Show the internal mechanics of REPL"""
    print("\n🔍 REPL INTERNAL MECHANICS")
    print("=" * 30)
    
    print("\n1. AST (Abstract Syntax Tree) Analysis:")
    expression = "x * 2 + y"
    tree = ast.parse(expression, mode='eval')
    print(f"Expression: {expression}")
    print(f"AST: {ast.dump(tree, indent=2)}")
    
    print("\n2. Compilation Modes:")
    modes = {
        'eval': 'For expressions that return a value',
        'exec': 'For statements that perform actions', 
        'single': 'For interactive single statements (REPL mode)'
    }
    
    for mode, desc in modes.items():
        print(f"   {mode}: {desc}")
    
    print("\n3. Namespace Persistence:")
    print("   Variables and functions persist across REPL commands")
    print("   Each command shares the same global namespace")
    
    print("\n4. Error Recovery:")
    print("   REPL continues running even after errors")
    print("   Syntax errors are caught during compilation")
    print("   Runtime errors are caught during execution")

def create_mini_repl():
    """Create a minimal working REPL"""
    print("\n🐍 MINI REPL IMPLEMENTATION")
    print("=" * 30)
    print("(This is a simplified version showing the core concepts)")
    
    namespace = {'__name__': '__main__'}
    
    print("\nType 'quit' to exit")
    while True:
        try:
            # READ
            user_input = input("mini>>> ").strip()
            
            if user_input in ['quit', 'exit']:
                print("Goodbye!")
                break
            
            if not user_input:
                continue
            
            # COMPILE & EVAL
            try:
                # Try as expression
                result = eval(user_input, namespace)
                # PRINT
                if result is not None:
                    print(result)
                    namespace['_'] = result
            except SyntaxError:
                try:
                    # Try as statement
                    exec(user_input, namespace)
                except Exception as e:
                    print(f"Error: {e}")
            except Exception as e:
                print(f"Error: {e}")
                
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

if __name__ == "__main__":
    demonstrate_repl_phases()
    show_repl_internals()
    
    print("\n" + "=" * 50)
    print("🚀 Want to try the mini REPL? (y/n): ", end="")
    
    try:
        choice = input().strip().lower()
        if choice in ['y', 'yes']:
            create_mini_repl()
        else:
            print("Demo complete! 🎉")
    except (EOFError, KeyboardInterrupt):
        print("\nDemo complete! 🎉")
# What Happens in a REPL
# Read Phase

# Parse incomplete input (handle multi-line expressions)
# Maintain parsing state across inputs
# Handle syntax errors gracefully without crashing

# Eval Phase
# This is where it gets interesting - different languages handle this very differently:
# Python's Approach
# Python compiles each line to bytecode, then executes it in the existing namespace. It's not "just evaluating compiled code" - it's dynamically compiling and immediately executing while maintaining state.
# python# Each line becomes bytecode:
# >>> x = 5        # compile to STORE_NAME, execute
# >>> x + 10       # compile to LOAD_NAME, BINARY_ADD, execute
# Interpreted Languages (JavaScript, Ruby)
# The REPL directly interprets AST nodes without a separate compilation step. Each expression is parsed into an AST and evaluated in the current environment.
# Compiled Languages (Go, Rust)
# These are trickier - some compile to temporary executables, others use interpretation mode:

# Go's REPL (like gore) compiles fragments and links them
# Rust REPLs often use LLVM JIT compilation

# JIT-Compiled Languages (Java, C#)
# Compile to intermediate code (bytecode/IL) then JIT compile to machine code on demand.
# Key REPL Complexities
# State Management
# Variables, function definitions, and imports must persist across evaluations. The REPL maintains a global environment/namespace.
# Error Recovery
# Unlike batch compilation, REPLs must recover from errors gracefully and continue running. Syntax errors shouldn't crash the entire session.
# Incremental Compilation
# Some REPLs recompile only changed parts, maintaining compilation caches and dependency tracking.
# Expression vs Statement Handling
# REPLs need to distinguish between expressions (which return values to print) and statements (which don't).
# Advanced Features

# History and editing capabilities
# Tab completion requiring symbol table access
# Debugging integration
# Module/package reloading
# Multi-line input handling

# So no, it's not just "evaluating compiled code" - it's a sophisticated system that needs to handle incremental parsing, compilation, execution, state management, and error recovery in an interactive environment. Each language's REPL reflects its underlying execution model.

# Made changes.


# ```
# Perfect! I've created a comprehensive deep dive into REPL internal understanding in your lecture2.py file. Let me run this code to demonstrate the concepts: Let me check if there are any errors by running Python with verbose output: Excellent! The comprehensive REPL internal understanding demonstration is now working perfectly. Let me also create a simple interactive demo to show how you could test the simplified REPL implementation: 

# Made changes.

# Now let's run the interactive demo: Perfect! Now you have a comprehensive understanding of REPL internals. Let me create a summary document that explains the key concepts: 

# Made changes.

# 2004mathematicsEnthusiastAniketDatta: @agent Try Again

# GitHub Copilot: ## Summary

# I've provided you with a comprehensive understanding of **REPL internal workings** through multiple resources:

# ### 📚 What You Now Have:

# 1. **Enhanced lecture2.py** - Deep technical dive into REPL internals with:
#    - Complete REPL architecture explanation
#    - Working simplified REPL implementation
#    - Bytecode analysis and AST demonstrations
#    - Error handling mechanisms
#    - Namespace management examples

# 2. **Interactive repl_demo.py** - Hands-on demonstration showing:
#    - Step-by-step REPL cycle execution
#    - Real-time bytecode compilation
#    - Mini REPL implementation you can actually use

# 3. **Comprehensive REPL_Understanding.md** - Complete reference guide covering:
#    - All four REPL phases (Read-Eval-Print-Loop)
#    - Internal architecture and implementation details
#    - Advanced features and enhanced REPLs
#    - Practical examples and use cases

# ### 🎯 Key REPL Internal Concepts You've Learned:

# - **Four-Phase Cycle**: Read → Eval → Print → Loop
# - **Dual Compilation**: Expressions vs Statements
# - **Namespace Persistence**: Variables survive across commands
# - **Error Recovery**: Graceful handling of syntax/runtime errors
# - **Bytecode Execution**: How Python compiles and runs your code
# - **Multi-line Detection**: Smart input completion
# - **Enhanced REPLs**: IPython, Jupyter, and beyond

# The materials demonstrate both the **theoretical understanding** and **practical implementation** of how Python's interactive shell works internally, giving you deep insights into this fundamental development tool.

# You can run the demos to see REPL internals in action and refer to the markdown file as a complete reference guide! 🚀

# 2004mathematicsEnthusiastAniketDatta: Keeping the code intact can you explain each line of code in low-level and interview uunderstanding for the Program

# GitHub.copilot-chat.github.copilot.editor: I'll explain this REPL demonstration script line by line, focusing on both low-level mechanics and interview-relevant concepts.

# ## Script Header and Imports

# ```python
# #!/usr/bin/env python3
# ```
# **Low-level**: This shebang tells the system to use `python3` from the environment PATH to execute this script.
# **Interview relevance**: Shows understanding of script execution and cross-platform compatibility.

# ```python
# import sys
# import ast
# import dis
# from typing import Any, Optional
# import traceback
# ```
# **Low-level breakdown**:
# - `sys`: Access to interpreter internals and system-specific parameters
# - `ast`: Parse Python code into Abstract Syntax Trees for analysis
# - `dis`: Disassembler for Python bytecode - lets us see compiled instructions
# - `typing`: Type hints for better code documentation and IDE support
# - `traceback`: Format and display exception information

# ## Function 1: `demonstrate_repl_phases()`

# ```python
# def demonstrate_repl_phases():
#     """Demonstrate each phase of the REPL cycle"""
#     print("🔄 REPL CYCLE DEMONSTRATION")
#     print("=" * 30)
# ```
# **Interview concept**: The REPL cycle is **Read-Eval-Print-Loop**. This function simulates how Python's interactive interpreter works internally.

# ```python
# test_inputs = [
#     "2 + 3",                                    # Simple expression
#     "x = 10",                                   # Variable assignment
#     "x * 2",                                    # Variable usage
#     "def greet(name): return f'Hello, {name}!'", # Function definition
#     "greet('World')",                           # Function call
#     "import math; math.pi",                     # Import and attribute access
#     "[i**2 for i in range(5)]"                 # List comprehension
# ]
# ```
# **Low-level**: These represent different types of Python constructs that a REPL must handle - expressions vs statements, function definitions, imports, etc.

# ```python
# repl_namespace = {'__name__': '__main__'}
# ```
# **Critical concept**: This dictionary simulates the global namespace where variables and functions persist across REPL commands. The `__name__` key mimics Python's module system.

# ### The Core REPL Loop

# ```python
# for i, source in enumerate(test_inputs, 1):
#     print(f"\n--- Command {i} ---")
#     print(f"INPUT: {source}")
# ```
# **Low-level**: `enumerate(test_inputs, 1)` creates pairs of (index, value) starting from 1.

# #### READ Phase
# ```python
# print("📖 READ: Input received")
# ```
# **Interview insight**: In a real REPL, this phase handles user input, including multi-line statements and syntax completion.

# #### COMPILE Phase - The Tricky Part
# ```python
# try:
#     code_obj = compile(source, '<stdin>', 'eval')
#     is_expression = True
#     print("   → Compiled as expression")
# except SyntaxError:
#     code_obj = compile(source, '<stdin>', 'exec')
#     is_expression = False
#     print("   → Compiled as statement")
# ```

# **Low-level mechanics**:
# - `compile()` transforms source code into Python bytecode objects
# - `'<stdin>'` is the filename (fake, since it's from user input)
# - `'eval'` mode: for expressions that return values (`2 + 3`)
# - `'exec'` mode: for statements that don't return values (`x = 10`)

# **Interview gotcha**: Python tries `eval` first because expressions should display their results, but statements like assignments don't. This is why `x = 10` doesn't print anything, but `2 + 3` prints `5`.

# #### Bytecode Display
# ```python
# if is_expression and len(source) < 20:
#     print("   Bytecode:")
#     dis.dis(code_obj)
# ```
# **Low-level**: `dis.dis()` shows the bytecode instructions that the Python VM will execute. This is what makes Python "compiled" - it compiles to bytecode, not machine code.

# #### EVAL Phase
# ```python
# if is_expression:
#     result = eval(code_obj, repl_namespace)
# else:
#     exec(code_obj, repl_namespace)
#     result = None
# ```

# **Critical distinction**:
# - `eval()`: Executes and returns the result of an expression
# - `exec()`: Executes statements but returns `None`
# - Both use `repl_namespace` to maintain variable persistence

# #### PRINT Phase
# ```python
# if result is not None:
#     print(f"   OUTPUT: {repr(result)}")
#     # Store in _ like real Python REPL
#     repl_namespace['_'] = result
# else:
#     print("   OUTPUT: (no output)")
# ```

# **Interview detail**: `repr()` gives the "official" string representation. The `_` variable stores the last non-None result, just like Python's real REPL.

# ## Function 2: `show_repl_internals()`

# #### AST Analysis
# ```python
# expression = "x * 2 + y"
# tree = ast.parse(expression, mode='eval')
# print(f"AST: {ast.dump(tree, indent=2)}")
# ```

# **Low-level**: This shows how Python parses code into a tree structure before compilation. The AST represents the syntactic structure of the code.

# #### Compilation Modes Explanation
# ```python
# modes = {
#     'eval': 'For expressions that return a value',
#     'exec': 'For statements that perform actions', 
#     'single': 'For interactive single statements (REPL mode)'
# }
# ```

# **Interview insight**: The `'single'` mode is what Python's actual REPL uses - it can handle both expressions and statements intelligently.

# ## Function 3: `create_mini_repl()`

# This implements a working REPL:

# ```python
# namespace = {'__name__': '__main__'}

# while True:
#     try:
#         user_input = input("mini>>> ").strip()
        
#         if user_input in ['quit', 'exit']:
#             break
            
#         if not user_input:
#             continue
# ```

# **Low-level**: The infinite loop with `input()` is the core of any REPL. The `strip()` removes whitespace.

# #### The Expression-First Strategy
# ```python
# try:
#     result = eval(user_input, namespace)
#     if result is not None:
#         print(result)
#         namespace['_'] = result
# except SyntaxError:
#     try:
#         exec(user_input, namespace)
#     except Exception as e:
#         print(f"Error: {e}")
# ```

# **Interview concept**: This "try expression first, then statement" approach is a common REPL pattern. It ensures that expressions display their values while statements execute silently.

# ## Key Interview Takeaways

# 1. **REPL Architecture**: Read-Eval-Print-Loop with persistent namespace
# 2. **Python's Execution Model**: Source → AST → Bytecode → Execution
# 3. **Expression vs Statement Handling**: Different compilation modes for different code types
# 4. **Error Recovery**: REPLs must continue running after errors
# 5. **Namespace Persistence**: Variables and functions survive across commands
# 6. **Bytecode Compilation**: Python compiles incrementally, not just at startup

# This code demonstrates that a REPL isn't just "evaluating code" - it's a sophisticated system handling parsing, compilation, execution, state management, and error recovery in an interactive environment.