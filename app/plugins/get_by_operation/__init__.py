from app.commands import Command
from calculator.calculations import Calculations


class GetHistoryCommand(Command):
    def execute(self, command_name: str):
        print("Looking for: ", command_name.split(" "[0]))
        print(Calculations.find_by_operation(command_name.split(" ")[1]))