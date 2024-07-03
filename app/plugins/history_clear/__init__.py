from app.commands import Command
from calculator.calculations import Calculations

class ClearCommand(Command):
    def execute(self, command_name: str):
        Calculations.clear_history()