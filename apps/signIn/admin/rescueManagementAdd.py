import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.dependencies import Input, Output, State

from app import app
from apps.sideNavbar import adminSideNavbar as aSN


layout = html.Div(
    [
        aSN.adminSidebar(),
        html.Div(
            [
                dbc.Row(
                    [
                        dbc.Col(html.H2("Transaction Report", style={"color": "#dba514", "font-weight": "bold"}), width="auto"),
                        dbc.Col(
                            dbc.Button("Back", color="primary", href="/paymentLog", style={"width": "100px"}),  # Adjusted width for button
                            width="auto",
                            style={"textAlign": "right", },
                        )
                    ],
                ),
                dbc.Row(
                    [
                        #Left Column
                        dbc.Col(
                            [
                                html.H6('Rescue Name'),
                                dbc.Input(id="input-rescue-name"),
                                html.Br(),
                                html.H6('Category'),
                                dbc.Input(id="input-category"),
                                html.Br(),
                                html.H6('Gender'),
                                dbc.Input(id="input-gender"),
                                html.Br(),
                                html.H6('Age'),
                                dbc.Input(id="input-age"),
                                html.Br(),
                                html.H6('Breed'),
                                dbc.Input(id="input-breed"),
                                html.Br(),
                                html.H6('Rescue Status'),
                                dbc.DropdownMenu(
                                    label="Menu",
                                    children=[
                                        dbc.DropdownMenuItem("In Care"),
                                        dbc.DropdownMenuItem("Critical Condition"),
                                        dbc.DropdownMenuItem("Passed On"),
                                        dbc.DropdownMenuItem("Adopted"),
                                    ],
                                )
                            ],
                            width=6
                        ),

                        #Right Column
                        dbc.Col(
                            [
                                html.H6('Medical Condition'),
                                dbc.Input(id="input-age"),
                                html.Br(),
                                html.H6('Description'),
                                dbc.Input(id="input-age"),
                                html.Br(),
                                html.H6('Images/s'),
                                dbc.Button("add file goes here", color='light', href="/rescuesManagement/add", className="home-banner-button"),                       
                            ],
                            width=6
                        ),
                    ]
                ),
                dbc.Button("Update", color='primary', href="/rescuesManagement", style={'margin': '0 10px'})
            ], className="customer-admin-menu"
        ), 
    ],
)