from app.commands import Command
from calculator.calculations import Calculations
import logging

class GetHistoryCommand(Command):
    def execute(self, command_name: str):
        try:
            hist = Calculations.get_history()
            print(f"History: {hist}")
            logging.info(f"History: {hist}")
        except:
            print("Error")
            logging.critical("Something has gone wrong")