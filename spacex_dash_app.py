# Import required libraries
import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the airline data into pandas dataframe
spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# Create a dash application
app = dash.Dash(__name__)

# Create an app layout
app.layout = html.Div(children=[html.H1('SpaceX Launch Records Dashboard',
                                        style={'textAlign': 'center', 'color': '#503D36',
                                               'font-size': 40}),
                                # TASK 1: Add a dropdown list to enable Launch Site selection
                                # The default select value is for ALL sites
                                # dcc.Dropdown(id='site-dropdown',...)
                                  html.Div([
                                    dcc.Dropdown(id='site-dropdown',
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
                                
                                

                                # TASK 2: Add a pie chart to show the total successful launches count for all sites
                                # If a specific launch site was selected, show the Success vs. Failed counts for the site
                                html.Div(dcc.Graph(id='success-pie-chart')),
                                html.Br(),

                                html.P("Payload range (Kg):"),


                                # TASK 3: Add a slider to select payload range
                                #dcc.RangeSlider(id='payload-slider',...)
                                 dcc.RangeSlider(id='payload-slider',
                                                 min=0, max=10000, step=1000,
                                                 marks={0: '0',
                                                        100: '100'},
                                                 value=[min_payload, max_payload]),
                                # TASK 4: Add a scatter chart to show the correlation between payload and launch success
                                html.Div(dcc.Graph(id='success-payload-scatter-chart')),
                                ])

# TASK 2:
# Add a callback function for `site-dropdown` as input, `success-pie-chart` as output
@app.callback(Output(component_id='success-pie-chart', component_property='figure'),
              Input(component_id='site-dropdown', component_property='value'))
def get_pie_chart(entered_site):
    if entered_site == 'ALL':
        fig = px.pie(spacex_df, values='class',
                     names='Launch Site',
                     title='Total Success Launches By Site')
        return fig
    else:
        # Filter the data for the selected site
        filtered_df = spacex_df[spacex_df['Launch Site'] == entered_site]
        success_counts = filtered_df['class'].value_counts().reset_index()
        success_counts.columns = ['class', 'count']
        
        # Création du Pie Chart avec succès vs échec
        fig = px.pie(success_counts, values='count', names='class',
                     title=f'Success vs Failure for {entered_site}')
        return fig


# TASK 4:
# Add a callback function for `site-dropdown` and `payload-slider` as inputs, `success-payload-scatter-chart` as output


@app.callback(
    Output('success-payload-scatter-chart', 'figure'),
    [Input('site-dropdown', 'value'), Input("payload-slider", "value")]
)
def get_scatter_chart(entered_site, payload_range):
    # Filtrer les données en fonction de la plage de payload
    filtered_df = spacex_df[(spacex_df['Payload Mass (kg)'] >= payload_range[0]) &
                             (spacex_df['Payload Mass (kg)'] <= payload_range[1])]
    
    # Si un site spécifique est sélectionné, filtrer en plus par site
    if entered_site != 'ALL':
        filtered_df = filtered_df[filtered_df['Launch Site'] == entered_site]

    # Vérifier et supprimer les valeurs NaN dans "Booster Version Category"
    filtered_df = filtered_df.dropna(subset=['Booster Version Category'])

    # Récupérer toutes les catégories uniques de boosters
    unique_boosters = sorted(spacex_df['Booster Version Category'].dropna().unique())

    # Créer le scatter plot avec toutes les catégories de boosters visibles
    fig = px.scatter(filtered_df, x='Payload Mass (kg)', y='class',
                     color='Booster Version Category',
                     category_orders={'Booster Version Category': unique_boosters},
                     title=f'Correlation Between Payload and Success for {entered_site if entered_site != "ALL" else "All Sites"}')

    return fig

   



# Run the app
if __name__ == '__main__':
    app.run_server()
