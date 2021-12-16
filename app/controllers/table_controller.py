from app.controllers.controller import ControllerBase
from flask import render_template

from calc.calculator import Calculator
from calc.history.calculations import Calculations


class TableController(ControllerBase):
    @staticmethod
    def get():
        return render_template('table.html', data=Calculator.getHistoryFromCSV(),
                               length=Calculations.historyCSVLength())
