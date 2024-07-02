from decimal import Decimal
from app.commands import Command
from calculator import Calculator

class DivideCommand(Command):
    def execute(self, numberA: str, numberB: str):
        print(Calculator.divide(Decimal(numberA), Decimal(numberB)))