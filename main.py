from flask import Flask, request, jsonify, render_template
from calculator import Calculator

app = Flask(__name__, template_folder='templates')

class Main:
    def __init__(self):
        self.calculator = Calculator()

    def run(self):
        app.run(debug=True)
