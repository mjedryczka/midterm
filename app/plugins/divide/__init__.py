from decimal import Decimal
from app.commands import Command
from calculator import Calculator

class DivideCommand(Command):
    def execute(self, command_name: str):
        print(Calculator.divide(Decimal(command_name.split(" ")[1]), Decimal(command_name.split(" ")[2])))