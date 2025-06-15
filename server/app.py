from flask import Flask, Response

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<parameter>')
def print_route(parameter):
    print(parameter)  
    return f"{parameter}"

@app.route('/count/<parameter>')
def count(parameter):
    try:
        count_range = int(parameter)
        result = "".join(f"{i}\n" for i in range(count_range))  # fix applied here
        return Response(result, mimetype='text/plain')
    except ValueError:
        return "Invalid input", 400

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 == 0:
            return "Cannot divide by zero", 400
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return "Invalid operation", 400

    return f"{result}"  
