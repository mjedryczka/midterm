from decimal import Decimal
from app.commands import Command
from calculator import Calculator

class AddCommand(Command):
    def execute(self, numberA: str, numberB: str):
        print(Calculator.add(Decimal(numberA), Decimal(numberB)))