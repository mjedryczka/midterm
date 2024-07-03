from app.commands import Command
import pandas as pd
import logging

class SaveRemoveOldestt(Command):
    def execute(self, command_name: str):
        try:
            csv_file_path = "calculations.csv"
            df = pd.read_csv(csv_file_path)

            if not df.empty:
                df = df.iloc[:-1]
                df.to_csv(csv_file_path, index=False)
                print("Oldest entry removed.")
            else:
                print("The file is empty. No entries to remove.")
        except:
            print("An error has occured")
            logging.critical("An error has occured")