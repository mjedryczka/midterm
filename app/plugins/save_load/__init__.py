from app.commands import Command
from calculator.calculations import Calculations
from calculator import Calculator
from decimal import Decimal
import pandas as pd

class SaveLoadCommand(Command):
    def execute(self, command_name: str):
        try:
            csv_file_path = "calculations.csv"

            try:
                df_read = df_read = pd.read_csv(csv_file_path)
            except:
                print(f"Save file, {csv_file_path}, cannot be loaded")

            operation_mappings = {
                'add': Calculator.add,
                'subtract': Calculator.subtract,
                'multiply': Calculator.multiply,
                'divide': Calculator.divide
            }

            for index, row in df_read.iterrows():
                try:
                    operation_mappings[row['Operation']](Decimal(row['Num1']), Decimal(row['Num2']))
                except:
                    print("Invalid save entry")
        except:
            print("Error while loading save")