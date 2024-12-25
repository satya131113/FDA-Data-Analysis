from dash import Dash
from data import read_data
from plots import create_countries_plot
from layout import create_layout

app = Dash(__name__, title="FDA Data Analysis")


drug_recall_data = read_data('./datafiles/drug-enforcement-data.csv')

app.layout = create_layout(dataframe= drug_recall_data)

# Expose the Flask server instance for Gunicorn
server = app.server

if __name__ == '__main__':
    app.run(debug=False)