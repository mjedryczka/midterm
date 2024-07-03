from app.commands import Command
from calculator.calculations import Calculations
import pandas as pd

class SaveHistoryCommand(Command):
    def execute(self, command_name: str):
        try:
            calculations = Calculations.get_history()
            data = {
                "Operation": [],
                "Num1": [],
                "Num2": [],
                "Result": []
            }
            for calc in calculations:
                repr = calc.__repr__().split(" ")
                print(repr)
                data["Operation"].append(repr[0])
                data["Num1"].append(repr[1])
                data["Num2"].append(repr[2])
                data["Result"].append(repr[3])

            df = pd.DataFrame(data)
            csv_file_path = "calculations.csv"
            df.to_csv(csv_file_path, index = False)
            print(f"Calculations saved to {csv_file_path}")
        except:
            print("Error while saving history")