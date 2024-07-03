from app.commands import Command
from calculator.calculations import Calculations
import logging

class GetLatestCommand(Command):
    def execute(self, command_name: str):
        try:
            latest = Calculations.get_latest()
            print(latest)
            logging.info(f"Latest: {latest}")
        except:
            print("Error")
            logging.critical("Something has gone wrong")