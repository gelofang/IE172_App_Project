import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, State, dcc, html
from dash.exceptions import PreventUpdate

from app import app
from apps.sideNavbar import adminSideNavbar as aSN
from dbconnect import getDataFromDB

layout=html.Div(
    [
        aSN.adminSidebar(),
        html.Div(
            [
                dbc.Col(
                    [
                        dbc.Row(
                            [
                                dbc.Col(html.H3("Rescues Management", style={"color": "#fcbf49", "margin-top": "20px"})),
                                dbc.Col(
                                    dbc.Button("Add", color='light', href="/rescuesManagementProfile?mode=add", className="home-banner-button")
                                ),
                            ], align="center"
                        ),
                        html.Div('List of Rescues go here', id='rescues_rescueslist')
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
    print(pathname)
    if pathname != '/rescuesManagement':
        raise PreventUpdate
    
    
    sql = "SELECT * FROM rescues"
    val = []
    col = ["Rescue Name","Gender",'Age','Breed','Medical Condition',"Description", "Category","rescue_id"]

    df = getDataFromDB(sql, val, col)

    df['Action'] = [
        html.Div(
            dbc.Button("Edit", color='warning', size='sm', 
                        href = f"/rescuesManagementProfile?mode=edit&id={row['rescue_id']}"),
            className='text-center'
        ) for idx, row in df.iterrows()
        ]
    
    df = df[['Rescue Name','Gender','Age','Breed','Medical Condition','Description', 'Category', 'Action']]

    rescues_table = dbc.Table.from_dataframe(df, striped=True, bordered=True, hover=True, size='sm')

    return[rescues_table]
