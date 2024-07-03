from app.commands import Command
from calculator.calculations import Calculations

class GetLatestCommand(Command):
    def execute(self, command_name: str):
        print(Calculations.get_latest())