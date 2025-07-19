# REPL INTERNAL UNDERSTANDING - DEEP DIVE
# ==========================================

import sys
import code
import ast
import dis
import types
from typing import Any, Optional, Dict
import traceback

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
# When we write "a=10"