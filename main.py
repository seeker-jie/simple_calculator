## main.py

from flask import Flask, request, jsonify, render_template
from calculator import Calculator

app = Flask(__name__)

class Main:
    def __init__(self):
        self.calculator = Calculator()

    def run(self):
        app.run(debug=True)

    def calculate(self, operation: str, number1: float, number2: float) -> float:
        if operation == 'add':
            return self.calculator.add(number1, number2)
        elif operation == 'subtract':
            return self.calculator.subtract(number1, number2)
        elif operation == 'multiply':
            return self.calculator.multiply(number1, number2)
        elif operation == 'divide':
            return self.calculator.divide(number1, number2)
        else:
            raise ValueError(f"Unsupported operation: {operation}")

main_instance = Main()

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    operation = data.get('operation')
    number1 = data.get('number1', 0.0)
    number2 = data.get('number2', 0.0)
    
    try:
        result = main_instance.calculate(operation, number1, number2)
        return jsonify(result=result), 200
    except ValueError as e:
        return jsonify(error=str(e)), 400

@app.route('/reset', methods=['POST'])
def reset():
    main_instance.calculator.reset()
    return jsonify(message="Calculator reset"), 200

if __name__ == '__main__':
    main_instance.run()
