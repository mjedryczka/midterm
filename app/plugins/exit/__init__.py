import sys
from app.commands import Command


class ExitCommand(Command):
    def execute(self, command_name: str):
        sys.exit("Exiting...")