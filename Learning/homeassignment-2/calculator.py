class Calculator:

    def addition(self, num_a, num_b):
        return num_a + num_b

    def subtraction(self, num_a, num_b):
        return num_a - num_b

    def multiplication(self, num_a, num_b):
        return num_a * num_b

    def division(self, num_a, num_b):
        if num_b == 0:
            return "Error: Division by zero is not allowed."
        return num_a / num_b
