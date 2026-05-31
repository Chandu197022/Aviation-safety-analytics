import matplotlib.pyplot as plt
import seaborn as sns


class Visualizer:

    @staticmethod
    def yearly_trend(df):

        plt.figure(figsize=(12,6))

        sns.lineplot(
            data=df,
            x="year",
            y="incidents"
        )

        plt.title(
            "Incidents By Year"
        )

        plt.show()

    @staticmethod
    def fatalities_chart(df):

        plt.figure(figsize=(12,6))

        sns.barplot(
            data=df.head(10),
            x="fatalities",
            y="airline"
        )

        plt.show()

    @staticmethod
    def manufacturer_chart(df):

        plt.figure(figsize=(12,6))

        sns.barplot(
            data=df.head(10),
            x="fatalities",
            y="manufacturer"
        )

        plt.show()

    @staticmethod
    def correlation(df):

        plt.figure(
            figsize=(10,8)
        )

        sns.heatmap(
            df.corr(
                numeric_only=True
            ),
            annot=True
        )

        plt.show()