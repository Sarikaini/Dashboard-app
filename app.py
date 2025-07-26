import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

# Load your dataset
df = pd.read_csv("COVID.csv")  # Change to your actual filename

# Create bar charts
fig1 = px.bar(
    df,
    x='Name of the District',
    y='Earmarked beds for COVID with O2 supply under CHC and CDH as on 15.06.2022',
    title='COVID O2 Beds per District'
)

fig2 = px.bar(
    df,
    x='Name of the District',
    y='Occupancy of beds with O2 supply under CHC and CDH as on 15.06.2022',
    title='Occupied O2 Beds per District'
)

fig3 = px.bar(
    df,
    x='Name of the District',
    y='Vacancy of beds with O2 supply under CHC and CDH as on 15.06.2022',
    title='Vacant O2 Beds per District'
)

# Initialize Dash app
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("COVID-19 Bed Availability Dashboard", style={'textAlign': 'center'}),

    dcc.Graph(figure=fig1),
    dcc.Graph(figure=fig2),
    dcc.Graph(figure=fig3),

    html.P("Developed for CODTECH Internship - Task 3", style={'textAlign': 'center', 'fontStyle': 'italic'})
])

if __name__ == '__main__':
    app.run(debug=True)
