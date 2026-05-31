import pandas as pd
from pathlib import Path


class DataLoader:

    def __init__(self, data_directory):

        self.data_directory = Path(
            data_directory
        )

    def load_incidents(self):

        file_path = (
            self.data_directory
            / "incidents.csv"
        )

        return pd.read_csv(
            file_path
        )

    def load_airlines(self):

        file_path = (
            self.data_directory
            / "airlines.csv"
        )

        return pd.read_csv(
            file_path
        )

    def load_aircraft(self):

        file_path = (
            self.data_directory
            / "aircraft_types.csv"
        )

        return pd.read_csv(
            file_path
        )

    def load_routes(self):

        file_path = (
            self.data_directory
            / "routes.csv"
        )

        return pd.read_csv(
            file_path
        )

    def load_trends(self):

        file_path = (
            self.data_directory
            / "safety_trends.csv"
        )

        return pd.read_csv(
            file_path
        )

    def load_all(self):

        return {

            "incidents":
                self.load_incidents(),

            "airlines":
                self.load_airlines(),

            "aircraft":
                self.load_aircraft(),

            "routes":
                self.load_routes(),

            "trends":
                self.load_trends()

        }