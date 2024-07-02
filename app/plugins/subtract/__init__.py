from decimal import Decimal
from app.commands import Command
from calculator import Calculator

class SubtractCommand(Command):
    def execute(self, numberA: str, numberB: str):
        print(Calculator.subtract(Decimal(numberA), Decimal(numberB)))