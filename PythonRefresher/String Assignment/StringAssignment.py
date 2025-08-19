'''
String Assignment we will do together:

Ask the user how many days until their birthday
and print an approx number of weeks until their birthday

Weeks is = 7 days

decimals within the return is allowed..
'''

class BirthdayCalculator:
    def __init__(self):
        self.days_per_week = 7
    
    def get_days_input(self):
        """Get the number of days from user input"""
        return int(input("How many days until your birthday? "))
    
    def calculate_weeks(self, days):
        """Calculate weeks from days"""
        return round(days / self.days_per_week, 2)
    
    def display_result(self, weeks):
        """Display the result"""
        print(weeks)
    
    def run(self):
        """Main method to run the birthday calculator"""
        days = self.get_days_input()
        weeks = self.calculate_weeks(days)
        self.display_result(weeks)

# Create an instance and run the calculator
calculator = BirthdayCalculator()
calculator.run()