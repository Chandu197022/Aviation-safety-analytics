class KPI:

    @staticmethod
    def total_incidents(df):

        return len(df)

    @staticmethod
    def total_fatalities(df):

        return (
            df["fatalities"]
            .sum()
        )

    @staticmethod
    def total_injuries(df):

        return (
            df["injuries"]
            .sum()
        )

    @staticmethod
    def total_casualties(df):

        return (
            df["total_casualties"]
            .sum()
        )

    @staticmethod
    def fatal_incidents(df):

        return (

            df["is_fatal"]

            .sum()

        )

    @staticmethod
    def average_fatalities(df):

        return round(

            df["fatalities"]

            .mean(),

            2

        )

    @staticmethod
    def average_injuries(df):

        return round(

            df["injuries"]

            .mean(),

            2

        )

    @staticmethod
    def fatality_percentage(df):

        fatal_count = (

            df["is_fatal"]

            .sum()

        )

        return round(

            (

                fatal_count

                /

                len(df)

            ) * 100,

            2

        )

    @staticmethod
    def get_kpis(df):

        return {

            "Total Incidents":
                KPI.total_incidents(df),

            "Total Fatalities":
                KPI.total_fatalities(df),

            "Total Injuries":
                KPI.total_injuries(df),

            "Total Casualties":
                KPI.total_casualties(df),

            "Fatal Incidents":
                KPI.fatal_incidents(df),

            "Fatal Incident %":
                KPI.fatality_percentage(df),

            "Average Fatalities":
                KPI.average_fatalities(df),

            "Average Injuries":
                KPI.average_injuries(df)

        }