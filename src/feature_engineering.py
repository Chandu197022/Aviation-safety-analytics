import numpy as np


class FeatureEngineering:

    @staticmethod
    def total_casualties(df):

        df["total_casualties"] = (

            df["fatalities"]

            +

            df["injuries"]

        )

        return df

    @staticmethod
    def fatality_rate(df):

        df["fatality_rate"] = np.where(

            df["occupants_onboard"] > 0,

            (

                df["fatalities"]

                /

                df["occupants_onboard"]

            ) * 100,

            0

        )

        return df

    @staticmethod
    def injury_rate(df):

        df["injury_rate"] = np.where(

            df["occupants_onboard"] > 0,

            (

                df["injuries"]

                /

                df["occupants_onboard"]

            ) * 100,

            0

        )

        return df

    @staticmethod
    def severity_score(df):

        df["severity_score"] = (

            df["fatalities"] * 5

            +

            df["injuries"] * 2

        )

        return df

    @staticmethod
    def risk_category(df):

        df["risk_category"] = np.where(

            df["severity_score"] > 200,

            "High",

            np.where(

                df["severity_score"] > 50,

                "Medium",

                "Low"

            )

        )

        return df

    @staticmethod
    def create_features(df):

        df = (
            FeatureEngineering
            .total_casualties(df)
        )

        df = (
            FeatureEngineering
            .fatality_rate(df)
        )

        df = (
            FeatureEngineering
            .injury_rate(df)
        )

        df = (
            FeatureEngineering
            .severity_score(df)
        )

        df = (
            FeatureEngineering
            .risk_category(df)
        )

        return df