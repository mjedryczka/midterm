from app.commands import Command
from calculator.calculations import Calculations
import logging

class GetHistoryCommand(Command):
    def execute(self, command_name: str):
        try:
            result = Calculations.find_by_operation(command_name.split(" ")[1])
            print(f"Result: {result}")
            logging.info(result)
        except:
            print("Error")
            logging.critical("Something has gone wrong")