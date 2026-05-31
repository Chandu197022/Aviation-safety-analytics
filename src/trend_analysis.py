import pandas as pd


class TrendAnalysis:

    @staticmethod
    def yearly_incidents(df):

        return (
            df.groupby("year")
            .size()
            .reset_index(name="incidents")
        )

    @staticmethod
    def yearly_fatalities(df):

        return (
            df.groupby("year")
            ["fatalities"]
            .sum()
            .reset_index()
        )

    @staticmethod
    def yearly_injuries(df):

        return (
            df.groupby("year")
            ["injuries"]
            .sum()
            .reset_index()
        )