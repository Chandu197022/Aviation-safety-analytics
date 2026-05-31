import pandas as pd
import numpy as np


class DataCleaner:

    @staticmethod
    def standardize_columns(df):

        df.columns = (

            df.columns

            .str.strip()

            .str.lower()

            .str.replace(
                " ",
                "_"
            )

        )

        return df

    @staticmethod
    def remove_duplicates(df):

        before = len(df)

        df = df.drop_duplicates()

        after = len(df)

        print(
            f"Removed {before-after} duplicates"
        )

        return df

    @staticmethod
    def handle_missing_values(df):

        numeric_columns = [

            "fatalities",
            "injuries",
            "occupants_onboard"

        ]

        for col in numeric_columns:

            if col in df.columns:

                df[col] = (
                    df[col]
                    .fillna(0)
                )

        categorical_columns = [

            "airline",
            "aircraft_type",
            "manufacturer",
            "country",
            "region",
            "incident_type",
            "phase_of_flight",
            "weather_conditions"

        ]

        for col in categorical_columns:

            if col in df.columns:

                df[col] = (
                    df[col]
                    .fillna(
                        "Unknown"
                    )
                )

        return df

    @staticmethod
    def convert_data_types(df):

        if "year" in df.columns:

            df["year"] = (

                pd.to_numeric(

                    df["year"],

                    errors="coerce"

                )

            )

        return df

    @staticmethod
    def clean_incidents(df):

        df = (
            DataCleaner
            .standardize_columns(df)
        )

        df = (
            DataCleaner
            .remove_duplicates(df)
        )

        df = (
            DataCleaner
            .handle_missing_values(df)
        )

        df = (
            DataCleaner
            .convert_data_types(df)
        )

        return df

    @staticmethod
    def clean_airlines(df):

        return (
            DataCleaner
            .standardize_columns(df)
        )

    @staticmethod
    def clean_routes(df):

        return (
            DataCleaner
            .standardize_columns(df)
        )

    @staticmethod
    def clean_aircraft(df):

        return (
            DataCleaner
            .standardize_columns(df)
        )

    @staticmethod
    def clean_trends(df):

        return (
            DataCleaner
            .standardize_columns(df)
        )