def calculator():
    print("Simple Calculator")
    print("Operations: +, -, *, /")
    
    while True:
        try:
            # Get user input
            num1 = float(input("Enter first number: "))
            operator = input("Enter operator (+, -, *, /): ")
            num2 = float(input("Enter second number: "))
            
            # Perform calculation based on operator
            if operator == '+':
                result = num1 + num2
                print(f"{num1} + {num2} = {result}")
                
            elif operator == '-':
                result = num1 - num2
                print(f"{num1} - {num2} = {result}")
                
            elif operator == '*':
                result = num1 * num2
                print(f"{num1} * {num2} = {result}")
                
            elif operator == '/':
                if num2 == 0:
                    print("Error: Cannot divide by zero!")
                else:
                    result = num1 / num2
                    print(f"{num1} / {num2} = {result}")
                    
            else:
                print("Invalid operator! Please use +, -, *, or /")
            
            # Ask if user wants to continue
            again = input("Calculate again? (yes/no): ").lower()
            if again != 'yes':
                print("Goodbye!")
                break
                
        except ValueError:
            print("Error: Please enter valid numbers!")
            
        except Exception as e:
            print(f"An error occurred: {e}")

# Run the calculator
if __name__ == "__main__":
    calculator()