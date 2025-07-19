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
