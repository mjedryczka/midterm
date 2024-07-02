from abc import ABC, abstractmethod
from decimal import Decimal

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, command_name: str, command: Command):
        self.commands[command_name] = command

    def execute_command(self, command_name: str):
        # print("Entered Command: ", command_name)
        try:
            self.commands[command_name.split(" ")[0]].execute(command_name)
        except KeyError:
            print(f"No such command: {command_name}")