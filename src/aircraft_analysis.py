import pandas as pd


class AircraftAnalysis:

    @staticmethod
    def aircraft_incidents(df):

        return (
            df.groupby("aircraft_type")
            .size()
            .reset_index(name="incidents")
            .sort_values(
                "incidents",
                ascending=False
            )
        )

    @staticmethod
    def manufacturer_fatalities(df):

        return (
            df.groupby("manufacturer")
            ["fatalities"]
            .sum()
            .reset_index()
            .sort_values(
                "fatalities",
                ascending=False
            )
        )

    @staticmethod
    def aircraft_risk(df):

        result = (
            df.groupby("aircraft_type")
            .agg({
                "fatalities":"sum",
                "incident_id":"count"
            })
            .reset_index()
        )

        result["risk_score"] = (
            result["fatalities"]
            /
            result["incident_id"]
        )

        return result