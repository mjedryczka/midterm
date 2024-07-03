from app.commands import Command
from calculator.calculations import Calculations
import pandas as pd
import logging
import os

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

            try:
                csv_file_path = os.getenv("save_file_dest")
            except:
                logging.warning("Env variable, save_file_dest, is not set")
                csv_file_path = "calculations.csv"

            df.to_csv(csv_file_path, index = False)
            print(f"Calculations saved to {csv_file_path}")
        except:
            print("Error while saving history")
            logging.critical("Error while saving history")