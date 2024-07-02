from decimal import Decimal, DecimalException
from app.commands import Command
from calculator import Calculator

class AddCommand(Command):
    def execute(self, command_name: str):
        try:
            print(Calculator.add(Decimal(command_name.split(" ")[1]), Decimal(command_name.split(" ")[2])))
        except (ValueError, DecimalException, TypeError):
            print("Error")