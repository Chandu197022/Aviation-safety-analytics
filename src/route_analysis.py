import pandas as pd


class RouteAnalysis:

    @staticmethod
    def top_risky_routes(routes):

        return (
            routes
            .sort_values(
                "risk_index",
                ascending=False
            )
            .head(20)
        )

    @staticmethod
    def longest_routes(routes):

        return (
            routes
            .sort_values(
                "distance_km",
                ascending=False
            )
            .head(20)
        )

    @staticmethod
    def most_used_routes(routes):

        return (
            routes
            .sort_values(
                "annual_passengers",
                ascending=False
            )
            .head(20)
        )