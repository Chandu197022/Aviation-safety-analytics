import pandas as pd


class AirlineAnalysis:

    @staticmethod
    def airline_incidents(df):

        return (
            df.groupby("airline")
            .size()
            .reset_index(name="incident_count")
            .sort_values(
                "incident_count",
                ascending=False
            )
        )

    @staticmethod
    def airline_fatalities(df):

        return (
            df.groupby("airline")["fatalities"]
            .sum()
            .reset_index()
            .sort_values(
                "fatalities",
                ascending=False
            )
        )

    @staticmethod
    def airline_injuries(df):

        return (
            df.groupby("airline")["injuries"]
            .sum()
            .reset_index()
            .sort_values(
                "injuries",
                ascending=False
            )
        )

    @staticmethod
    def airline_risk_score(df):

        summary = (
            df.groupby("airline")
            .agg({
                "fatalities":"sum",
                "incident_id":"count"
            })
            .reset_index()
        )

        summary["risk_score"] = (
            summary["fatalities"]
            /
            summary["incident_id"]
        )

        return summary.sort_values(
            "risk_score",
            ascending=False
        )