"""A simple flask web app"""
from flask import Flask, render_template

# from app.controllers import table_controller
from app.controllers.table_controller import TableController
from app.controllers.index_controller import IndexController
from app.controllers.calculator_controller import CalculatorController
from werkzeug.debug import DebuggedApplication

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.wsgi_app = DebuggedApplication(app.wsgi_app, True)


@app.route("/", methods=['GET'])
def index_get():
    return IndexController.get()


@app.route("/calculator", methods=['GET'])
def calculator_get():
    return CalculatorController.get()


@app.route("/calculator", methods=['POST'])
def calculator_post():
    return CalculatorController.post()


@app.route("/table", methods=['GET'])
def table_post():
    return TableController.get()


@app.route("/pylint", methods=['GET'])
def pylint():
    return render_template('pylint.html')


@app.route("/AAAtest", methods=['GET'])
def aaa_test():
    return render_template('AAAtest.html')


@app.route("/oop", methods=['GET'])
def oop():
    return render_template('oop.html')


@app.route("/soc", methods=['GET'])
def soc():
    return render_template('soc.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)
