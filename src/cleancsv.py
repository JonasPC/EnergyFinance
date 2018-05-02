from src.gdp import GDP
from src.longlat import LongLat
from src.population import Population
from src.prices import Prices
from src.sales import Sales
from src.weather import Weather


GDP.write_gdp()
LongLat.write_longlat()
Weather.write_weather()
Population.write_population()
Prices.write_prices()
Sales.write_sales()
