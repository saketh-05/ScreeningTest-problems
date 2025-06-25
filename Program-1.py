'''
  Create a small calculator which performs operations such as Addition, Subtraction, Multiplication and Division using class.
  Calculator inputs :> ‘a’, ‘b’ and ‘type of operation’
  Datatype :> ‘a’ = double, ‘b’ = double, ‘type of operation’ = string
'''

class Calculator:
    def __init__(self, a, b, operation):
        self.a = a
        self.b = b
        self.operation = operation
        
    def calculate(self):
        if self.operation in ['add', '+']:
            self.result = self.a + self.b
            
        elif self.operation in ['subtract', '-']:
            self.result = self.a - self.b
            
        elif self.operation in ['multiply', 'x']:
            self.result = self.a * self.b
            
        elif self.operation in ['divide', '/']:
            if self.b == 0:
                return "Error: Division by zero is not allowed."
            self.result = self.a / self.b
            
        return f"The result of {self.operation} operation on {self.a} and {self.b} is: {self.result}"
        
        
        
if __name__ == "__main__":
    while True:
        try:
            a = float(input("Enter first number (a): "))
            b = float(input("Enter second number (b): "))
        except ValueError:
            print("Invalid input. Please enter numeric values for a and b.")
            continue
    
        operation = input("Enter operation (add or +, subtract or -, multiply or x, divide or /): ").strip().lower()
        if operation not in ['add', '+' , 'subtract', '-', 'multiply', 'x', 'divide', '/']:
            print("Invalid operation. Please choose from add, subtract, multiply, divide or respective symbols.")
        else:
            break
    calculator = Calculator(a, b, operation)
    print(calculator.calculate())
        