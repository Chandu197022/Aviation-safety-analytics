from src.data_loader import DataLoader
from src.cleaner import DataCleaner
from src.feature_engineering import FeatureEngineering
from src.kpi import KPI

from src.airline_analysis import AirlineAnalysis
from src.aircraft_analysis import AircraftAnalysis
from src.route_analysis import RouteAnalysis
from src.trend_analysis import TrendAnalysis


loader = DataLoader("data")

datasets = loader.load_all()

incidents = datasets["incidents"]
airlines = datasets["airlines"]
aircraft = datasets["aircraft"]
routes = datasets["routes"]
trends = datasets["trends"]

incidents = DataCleaner.clean_incidents(
    incidents
)

incidents = (
    FeatureEngineering
    .create_features(
        incidents
    )
)

print(
    KPI.get_kpis(
        incidents
    )
)

print(
    AirlineAnalysis
    .airline_incidents(
        incidents
    )
    .head()
)

print(
    AircraftAnalysis
    .manufacturer_fatalities(
        incidents
    )
    .head()
)