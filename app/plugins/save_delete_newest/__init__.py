from app.commands import Command
from calculator.calculations import Calculations
import pandas as pd

class SaveRemoveNewest(Command):
    def execute(self, command_name: str):
        csv_file_path = "calculations.csv"
        df = pd.read_csv(csv_file_path)

        if not df.empty:
            df = df.iloc[1:]
            df.to_csv(csv_file_path, index=False)
            print("Oldest entry removed.")
        else:
            print("The file is empty. No entries to remove.")