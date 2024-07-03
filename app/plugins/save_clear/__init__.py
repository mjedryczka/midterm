from app.commands import Command
from calculator.calculations import Calculations
import pandas as pd
import logging

class ClearSaveCommand(Command):
    def execute(self, command_name: str):
        try:
            csv_file_path = "calculations.csv"
            empty_df = pd.DataFrame()
            empty_df.to_csv(csv_file_path, index=False)
            print(f"Cleared the contents of {csv_file_path}")
        except:
            print("Can't clear the file")
            logging.critical("Can't clear save file or it doesn't exists")