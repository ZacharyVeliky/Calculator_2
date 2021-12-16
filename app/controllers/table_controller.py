from app.controllers.controller import ControllerBase
from flask import render_template


class TableController(ControllerBase):
    @staticmethod
    def get():
        return render_template('table.html')
