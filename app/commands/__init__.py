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
        try:
            userInput = command_name.lower().strip().split(" ")
            if len(userInput) == 3:
                self.commands[userInput[0]].execute(userInput[1], userInput[2])
            elif len(userInput) == 1:
                self.commands[userInput[0]].execute()
            else:
                print("Usage: <operation> <numberA> <numberB>")

        except KeyError:
            print(f"No such command: {command_name}")