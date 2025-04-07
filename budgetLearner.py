# Budget Tracker - A simple program to track and summarize expenses

# 1. Syntax and Structure (variables, data types, comments)
budget_limit = 500.0  # float: maximum budget
total_spent = 0  # int: running total of expenses
expense_log = []  # list: stores expense details

# Importing a module (7. Modules and Libraries)
import random  # used to generate a random expense ID

# 8. Object-Oriented Programming (OOP) - Define a class for expenses
class Expense:
    def __init__(self, amount, category):
        self.amount = amount  # attribute: float
        self.category = category  # attribute: string
        self.id = random.randint(1000, 9999)  # random ID for tracking

    def details(self):  # method: returns expense info
        return f"ID: {self.id} | {self.category}: ${self.amount}"

# 5. Input and Output - Get user input for expenses
print("Welcome to Budget Tracker!")
while True:
    try:  # 6. Error Handling - Handle invalid inputs
        user_input = input("Enter expense amount (or 'done' to finish): ")
        if user_input.lower() == "done":
            break  # 2. Control Flow - Exit loop
        amount = float(user_input)  # Convert input to float
        if amount < 0:
            raise ValueError("Amount cannot be negative!")
        category = input("Enter category (e.g., Food, Rent): ")
        
        # Create an expense object (OOP)
        new_expense = Expense(amount, category)
        expense_log.append(new_expense)  # 3. Data Structures - List usage
        total_spent += amount

    except ValueError as e:  # Catch conversion or custom errors
        print(f"Error: {e}. Please enter a valid number.")

# 4. Functions - Define a function to summarize budget
def budget_summary(spent, limit, expenses):
    remaining = limit - spent
    status = "Under" if remaining > 0 else "Over"  # 2. Control Flow - Conditional
    summary = f"Total Spent: ${spent:.2f}\nBudget Limit: ${limit:.2f}\nRemaining: ${remaining:.2f}\nStatus: {status}"
    
    # 3. Data Structures - Dictionary to count categories
    category_totals = {}
    for expense in expenses:  # 2. Control Flow - Loop
        if expense.category in category_totals:
            category_totals[expense.category] += expense.amount
        else:
            category_totals[expense.category] = expense.amount
    
    return summary, category_totals

# 5. File Handling - Save summary to a file
with open("budget_summary.txt", "w") as file:
    summary, categories = budget_summary(total_spent, budget_limit, expense_log)
    file.write(summary + "\n\nCategory Breakdown:\n")
    for category, total in categories.items():  # 3. Data Structures - Dictionary loop
        file.write(f"{category}: ${total:.2f}\n")

# 9. Basic Debugging - Print results to check output
print("\nBudget Summary:")
print(summary)
print("\nCategory Breakdown:")
for category, total in categories.items():
    print(f"{category}: ${total:.2f}")

# Bonus: Practical check - Warn if over budget
if total_spent > budget_limit:  # 2. Control Flow - Conditional
    print(f"WARNING: You are ${total_spent - budget_limit:.2f} over budget!")

# Example output for study:
# Enter expense amount: 50
# Enter category: Food
# Enter expense amount: 200
# Enter category: Rent
# Enter expense amount: done
# Budget Summary:
# Total Spent: $250.00
# Budget Limit: $500.00
# Remaining: $250.00
# Status: Under
# Category Breakdown:
# Food: $50.00
# Rent: $200.00