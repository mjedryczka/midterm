from decimal import Decimal
from app.commands import Command
from calculator import Calculator

class MultiplyCommand(Command):
    def execute(self, numberA: str, numberB: str):
        print(Calculator.multiply(Decimal(numberA), Decimal(numberB)))