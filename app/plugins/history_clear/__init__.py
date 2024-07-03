from app.commands import Command
from calculator.calculations import Calculations
import logging

class ClearCommand(Command):
    def execute(self, command_name: str):
        try:
            Calculations.clear_history()
        except:
            print("Error")
            logging.critical("Something has gone wrong")