## calculator.py

class Calculator:
    def add(self, number1: float, number2: float) -> float:
        """Add two numbers and return the result.

        Args:
            number1 (float): The first number.
            number2 (float): The second number.

        Returns:
            float: The sum of the two numbers.
        """
        return number1 + number2

    def subtract(self, number1: float, number2: float) -> float:
        """Subtract the second number from the first and return the result.

        Args:
            number1 (float): The first number.
            number2 (float): The second number.

        Returns:
            float: The difference between the two numbers.
        """
        return number1 - number2

    def multiply(self, number1: float, number2: float) -> float:
        """Multiply two numbers and return the result.

        Args:
            number1 (float): The first number.
            number2 (float): The second number.

        Returns:
            float: The product of the two numbers.
        """
        return number1 * number2

    def divide(self, number1: float, number2: float) -> float:
        """Divide the first number by the second and return the result.

        Args:
            number1 (float): The first number.
            number2 (float): The second number.

        Returns:
            float: The quotient of the two numbers.

        Raises:
            ValueError: If the second number is zero.
        """
        if number2 == 0:
            raise ValueError("Cannot divide by zero.")
        return number1 / number2

    def reset(self) -> None:
        """Reset the calculator to its initial state.

        This method is currently a placeholder as the Calculator class
        does not maintain any internal state. However, it's included for
        future extensibility.
        """
        pass  # No state to reset; method is here for potential future use.


if __name__ == '__main__':
    calculator = Calculator()
    print(calculator.add(1, 2))  # 3
    print(calculator.subtract(5, 3))  # 2
    print(calculator.multiply(4, 6))  # 24
    print(calculator.divide(8, 0))
    calculator.reset()
    print("Calculator has been reset.")