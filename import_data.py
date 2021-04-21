import pandas as pd
import requests
from sqlalchemy import create_engine

# url for failte ireland API's
url_activities = "https://failteireland.azure-api.net/opendata-api/v1/activities"
url_accomodation = "https://failteireland.azure-api.net/opendata-api/v1/accommodation"


# create a reusable function to call API's and load data into a Pandas DataFrome
def make_api_call(url):
    results = requests.get(url)
    if results.status_code != 200:
        raise requests.ConnectionError("Expected status code 200, but got {}".format(results.status_code))
    data = results.json()
    df_results = pd.DataFrame(data['results'])
    return df_results


api_call = False  # Set api_call to false for testing purposes, so not calling it over and over
if api_call:
    df_activities = make_api_call(url_activities)
    df_activities.to_pickle("./data/pickle_df_activities.pkl")
    df_accomodation = make_api_call(url_accomodation)
    df_accomodation.to_pickle("./data/pickle_df_accomodation.pkl")
df_activities = pd.read_pickle("./data/pickle_df_activities.pkl")
df_accomodation = pd.read_pickle("./data/pickle_df_accomodation.pkl")


# Import data from a CSV file and load data into the df_attractions Pandas DataFrome
read_csv_url = False  # to skip constantly call this for testing
if read_csv_url:
    attractions_csv = 'https://failteireland.azure-api.net/opendata-api/v1/attractions/csv'
    df_attractions = pd.read_csv(attractions_csv, sep=',')
    df_attractions.to_pickle("./data/pickle_df_attractions.pkl")
df_attractions = pd.read_pickle("./data/pickle_df_attractions.pkl")

# Import data from a relational database into a dataframe
engine = create_engine('sqlite:///data///sqlliteDB_ucdproj.db')
df_county_province = pd.read_sql_query('SELECT * FROM COUNTY_PROVINCE_LINK WHERE country = "ROI"', engine)


# Importing data from html Web Scrapping into a Pandas DataFrame
read_html = False  # to skip constantly call this for testing
if read_html:
    url = 'https://en.wikipedia.org/wiki/List_of_cities,_boroughs_and_towns_in_the_Republic_of_Ireland'
    df_from_wikipedia = pd.read_html(url, header=[0], flavor='bs4')[2]
    df_from_wikipedia.to_pickle("./data/pickle_df_from_wikipedia.pkl")

df_area_type = pd.read_pickle("./data/pickle_df_from_wikipedia.pkl")

