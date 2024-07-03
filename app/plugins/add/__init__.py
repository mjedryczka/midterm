from decimal import Decimal, DecimalException
from app.commands import Command
from calculator import Calculator
import logging


class AddCommand(Command):
    def execute(self, command_name: str):
        try:
            result = Calculator.add(Decimal(command_name.split(" ")[1]), Decimal(command_name.split(" ")[2]))
            print(f"Result: {result}")
            logging.info(f"Result: {result}")
        except:
            print("Error")
            logging.critical("Something has gone wrong")