import sys

"""
User Input
"""

first_name = input("Enter your first name: ")
days = input("How many days before your birthday: ")
print(f"Hi {first_name}, only {days} days "
      f"before your birthday!")

class UserInput:
       def userInput(self):
                  # Read from stdin character by character
                  input_chars = []
                  while True:
                        char = sys.stdin.read(1)
                        if char == '\n' or char == '':
                              break
                        input_chars.append(char)
                  return ''.join(input_chars)


n=UserInput().userInput()
print(f"You entered: {n}")


