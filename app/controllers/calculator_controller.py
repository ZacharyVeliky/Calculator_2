import os

from app.controllers.controller import ControllerBase
from app.table_handler.table import Operations, db
from calc.calculator import Calculator
from flask import render_template, request, flash, redirect, url_for, session

from calc.history.calculations import Calculations
from csvmanager.read import Read


class CalculatorController(ControllerBase):
    @staticmethod
    def post():
        if request.form['value1'] == '' or request.form['value2'] == '':
            error = 'You must enter a value for value 1 and or value 2'
        else:
            flash('You successfully calculated')
            # get the values out of the form
            value1 = request.form['value1']
            value2 = request.form['value2']
            operation = request.form['operation']
            # make the tuple
            my_tuple = (value1, value2)
            # this will call the correct operation
            getattr(Calculator, operation)(my_tuple)
            result = str(Calculator.get_last_result_value())
            data = {'input_1': value1, 'input_2': value2, 'operation': operation,
                    'result': Calculator.get_last_result_value()}
            Calculator.writeHistoryToCSV(data)
            #
            return render_template('result.html', data=Calculator.getHistoryFromCSV(),
                                   length=Calculations.historyCSVLength(),
                                   value1=value1, value2=value2, operation=operation, result=result)
        return render_template('calculator.html', error=error)

    @staticmethod
    def get():
        return render_template('calculator.html')
