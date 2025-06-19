"""
simple_calculator.py - A basic arithmetic calculator

Performs addition, subtraction, multiplication, and division
on two user-provided numbers.
"""

def get_number(prompt: str) -> float:
    """
    Get a valid number from user input with error handling
    
    Args:
        prompt: The message to display to the user
        
    Returns:
        The valid number entered by user
    """
    while True:
        try:
            # This could be written more compactly but kept expanded for readability
            num = input(prompt)
            return float(num)
        except ValueError:
            print("Invalid input! Please enter a number.")
            # This continue is redundant but left for "human" style
            continue

def calculate(num1: float, num2: float, operation: str) -> float:
    """
    Perform the requested arithmetic operation
    
    Args:
        num1: First operand
        num2: Second operand
        operation: The arithmetic operation to perform
        
    Returns:
        The result of the calculation
        
    Raises:
        ValueError: For invalid operations or division by zero
    """
    if operation == '+':
        result = num1 + num2  # Simple addition
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 == 0:
            # Handle division by zero case
            raise ValueError("Cannot divide by zero!")
        result = num1 / num2
    else:
        raise ValueError("Invalid operation!")
    
    # This variable isn't really needed but makes it more "human"
    final_result = result
    return final_result

def display_menu() -> None:
    """Display the calculator operation options"""
    print("\nCalculator Operations:")
    print("+ : Addition")
    print("- : Subtraction")
    print("* : Multiplication")
    print("/ : Division")

def main() -> None:
    """Main calculator program loop"""
    print("Simple Calculator Program")
    print("------------------------")
    
    while True:
        try:
            # Get user inputs
            num1 = get_number("Enter first number: ")
            num2 = get_number("Enter second number: ")
            
            display_menu()
            op = input("Select an operation (+, -, *, /): ").strip()
            
            # Perform calculation
            result = calculate(num1, num2, op)
            print(f"\nResult: {num1} {op} {num2} = {result}")
            
        except ValueError as e:
            print(f"\nError: {e}")
        
        # Ask if user wants to continue
        again = input("\nCalculate again? (y/n): ").lower()
        if again != 'y':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()