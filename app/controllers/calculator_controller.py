from app.controllers.controller import ControllerBase
from app.table_handler.table import Operations, db
from calc.calculator import Calculator
from flask import render_template, request, flash, redirect, url_for, session


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

            # op = Operations(input_1=value1,
            #                 input_2=value2,
            #                 operation=operation,
            #                 result=str(Calculator.get_last_result_value()))
            # db.session.add(op)
            # db.session.commit()

            data = {'input_1': value1, 'input_2': value2, 'operation': operation,
                    'result': Calculator.get_last_result_value()}
            Calculator.writeHistoryToCSV(data)
            #
            return render_template('result.html', data=Calculator.getHistoryFromCSV(), value1=value1, value2=value2,
                                   operation=operation, result=result)
        return render_template('calculator.html', error=error)

    @staticmethod
    def get():
        return render_template('calculator.html')

    """
    The easy calculator solution
    1.  fix your calculator to read and write calculations to the csv
    2.  fix the controller to read the the csv to history first
    3.  Fix the controller to write the history to csv after you add the calculation to history
    4.  Make a method on the calculator to return the history in the format you want to print in the template
    
    Optional
       Fix it so that you store the type of calculation and perform the calulation at runtime, 
       so you don't store the raw result
       
       IF you want to be fancy you can change the delimeter for the file to semicolon and write your tuple of value to the file
       
       Values, Operation
       1,2,3,4; Addition
       1,2,3,4; Addition
    
    """
