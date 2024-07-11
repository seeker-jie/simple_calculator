from flask import Flask, request, jsonify, render_template
from calculator import Calculator

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def home():
    return render_template('index.html')

class Main:
    def __init__(self):
        self.calculator = Calculator()

    def run(self):
        app.run(debug=True)

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

main_instance.run()
