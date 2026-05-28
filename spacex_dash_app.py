"""
SpaceX Falcon 9 First Stage Landing - Interactive Dashboard
This application provides an interactive dashboard to visualize SpaceX launch records,
success rates by launch sites, and correlations between payload mass and launch success.
"""

import pandas as pd
import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import plotly.express as px

# 1. Load and prepare the dataset
spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# 2. Initialize the Dash application
app = dash.Dash(__name__)

# 3. Define the application layout
app.layout = html.Div(children=[
    html.H1('SpaceX Launch Records Dashboard',
            style={'textAlign': 'center', 'color': '#503D36', 'font-size': 40}),
    
    # Dropdown for Launch Site selection
    html.Div([
        dcc.Dropdown(
            id='site-dropdown',
            options=[
                {'label': 'All Sites', 'value': 'ALL'},
                {'label': 'CCAFS LC-40', 'value': 'CCAFS LC-40'},
                {'label': 'CCAFS SLC-40', 'value': 'CCAFS SLC-40'},
                {'label': 'VAFB SLC-4E', 'value': 'VAFB SLC-4E'},
                {'label': 'KSC LC-39A', 'value': 'KSC LC-39A'}
            ],
            value='ALL',
            placeholder="Select a launch site here",
            searchable=True
        ),
    ]),
    html.Br(),

    # Pie chart for success rate
    html.Div(dcc.Graph(id='success-pie-chart')),
    html.Br(),

    html.P("Payload range (Kg):"),

    # Slider for payload range selection
    dcc.RangeSlider(
        id='payload-slider',
        min=0, max=10000, step=1000,
        marks={i: str(i) for i in range(0, 10001, 1000)},
        value=[min_payload, max_payload]
    ),
    html.Br(),

    # Scatter chart for payload vs success correlation
    html.Div(dcc.Graph(id='success-payload-scatter-chart')),
])

# 4. Define Callbacks for interactivity

@app.callback(
    Output(component_id='success-pie-chart', component_property='figure'),
    Input(component_id='site-dropdown', component_property='value')
)
def update_pie_chart(entered_site):
    """Updates the pie chart based on the selected launch site."""
    if entered_site == 'ALL':
        fig = px.pie(spacex_df, values='class',
                     names='Launch Site',
                     title='Total Success Launches By Site')
    else:
        filtered_df = spacex_df[spacex_df['Launch Site'] == entered_site]
        success_counts = filtered_df['class'].value_counts().reset_index()
        success_counts.columns = ['class', 'count']
        
        fig = px.pie(success_counts, values='count', names='class',
                     title=f'Success vs Failure for {entered_site}')
    return fig

@app.callback(
    Output('success-payload-scatter-chart', 'figure'),
    [Input('site-dropdown', 'value'), Input("payload-slider", "value")]
)
def update_scatter_chart(entered_site, payload_range):
    """Updates the scatter chart based on the selected launch site and payload range."""
    # Filter by payload range
    filtered_df = spacex_df[
        (spacex_df['Payload Mass (kg)'] >= payload_range[0]) &
        (spacex_df['Payload Mass (kg)'] <= payload_range[1])
    ]
    
    # Filter by selected site
    if entered_site != 'ALL':
        filtered_df = filtered_df[filtered_df['Launch Site'] == entered_site]

    # Clean missing booster categories
    filtered_df = filtered_df.dropna(subset=['Booster Version Category'])
    unique_boosters = sorted(spacex_df['Booster Version Category'].dropna().unique())

    # Generate scatter plot
    site_title = entered_site if entered_site != "ALL" else "All Sites"
    fig = px.scatter(
        filtered_df, x='Payload Mass (kg)', y='class',
        color='Booster Version Category',
        category_orders={'Booster Version Category': unique_boosters},
        title=f'Correlation Between Payload and Success ({site_title})'
    )

    return fig

# 5. Run the application
if __name__ == '__main__':
    app.run_server(debug=True)
