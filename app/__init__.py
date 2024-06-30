from app.commands import CommandHandler
from app.commands import Command

class App:
    def __init__(self):
        self.command_handler = CommandHandler()

    def start(self):
        print("Type 'exit' to exit.")
        while True:
            self.command_handler.execute_command(input(">>> ").strip())