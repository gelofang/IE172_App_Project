import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, State, dcc, html
from dash.exceptions import PreventUpdate

from app import app
from apps.sideNavbar import adminSideNavbar as aSN
from apps.dbconnect import getDataFromDB

layout=html.Div(
    [
        dcc.Location(id='url', refresh=False),
        aSN.adminSidebar(),
        html.Div(
            [
                dbc.Col(
                    [
                        dbc.Row(
                            [
                                dbc.Col(html.H3("Rescues Management", style={"color": "#fcbf49", "margin-top": "20px"})),
                                dbc.Col(
                                    dbc.Button("Add", color='light', href="/rescuesManagement/add", className="home-banner-button")
                                ),
                            ], align="center"
                        ),
                        html.Div(
                            [
                                html.H4('List of Rescues'),
                                dcc.Loading(  # Wrap the output in a loading spinner
                                    id="loading-1",
                                    type="default",
                                    children=[html.Div(id='rescues_rescueslist')]
                                )
                            ]
                        ),
                    ],
                    width=9,
                    className="customer-admin-menu"
                )
            ]
        )
    ]
)

# Callback to retrieve and display data from the database when the page loads
@app.callback(
    [
        Output('rescues_rescueslist', 'children'),
    ],
    [
        Input('url', 'pathname'),
    ],
)

def load_rescues_list(pathname):
    if pathname != '/rescuesManagement':
        raise PreventUpdate
    
    sql = "SELECT * FROM rescues"
    val = []
    col = ["rescue_name","category","gender",'age','breed','med_condition',"description","rescue_id"]

    try:
        df = getDataFromDB(sql, val, col)
        if df.empty:
            return [html.Div("No rescues found.")]
        
        df['Action'] = [
        html.Div(
            dbc.Button("Edit", color='warning', size='sm', 
                        href = f"/rescuesManagement?mode=edit&id={row['rescue_id']}"),
            className='text-center'
        ) for idx, row in df.iterrows()
        ]

        df = df[["rescue_name","category","gender",'age','breed','med_condition',"description", 'Action']]

        rescues_table = dbc.Table.from_dataframe(df, striped=True, bordered=True, hover=True, size='sm')

        return[rescues_table]
    
    except Exception as e:
        return f"Error retrieving data: {e}"
