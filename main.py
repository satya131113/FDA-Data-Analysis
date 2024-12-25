from dash import Dash
from data import read_data
from plots import create_countries_plot
import dash_labs as dl
from layout import create_layout

# Initialize the Dash app
app = Dash(__name__, title="FDA Data Analysis")

# Read the data
drug_recall_data = read_data('./datafiles/drug-enforcement-data.csv')

# Set up the layout
app.layout = create_layout(dataframe=drug_recall_data)

if __name__ == '__main__':
    # Export the app as static files using Dash Labs
    dl.plugins.export(app, './static')
