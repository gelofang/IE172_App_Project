import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.exceptions import PreventUpdate
from dash.dependencies import Input, Output, State

from app import app

# instead of app.layout, we just use the variable "layout" here
# We cannot really modify the "app" variable here, we only do it in index.py

import dash
import dash_bootstrap_components as dbc
from dash import dcc, html

dogs = [
    {"name": "Alpha", "image": "https://placedog.net/300/300?random=1", "profile": "/meettherescues/dogs/Alpha"},
    {"name": "Charlie", "image": "https://placedog.net/300/300?random=2", "profile": "/meettherescues/dogs/Charlie"},
    {"name": "Buddy", "image": "https://placedog.net/300/300?random=3", "profile": "/meettherescues/dogs/Buddy"},
    {"name": "Delta", "image": "https://placedog.net/300/300?random=4", "profile": "/meettherescues/dogs/Delta"},
]

layout = html.Div(
    [
        # Header Section (Header aligned left, search bar aligned right)
        dbc.Row(
            [
                dbc.Col(
                    html.H1("Meet the Dogs"),  # Header aligned to the left
                    width=8,  # Takes 8 columns of the row
                    style={'textAlign': 'left'}
                ),
                dbc.Col(
                    dcc.Input(
                        id="search-input",
                        placeholder="Search for a dog...",
                        type="text",
                        className="search-bar",
                        style={'width': '100%'}
                    ),  
                    width=4,  # Takes 4 columns of the row
                    style={'textAlign': 'right'}
                )
            ],
            className="mb-4"
        ),

        # Dog Gallery Section
        dbc.Row(  # Bootstrap Row for the dog cards
            [
                # First Column (Dog 1)
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody(
                            [
                                html.Img(src=dogs[0]["image"], className="dog-image", style={"width": "100%", "borderRadius": "8px"}),
                                html.H5(dogs[0]["name"], className="dog-name", style={'textAlign': 'center', 'marginTop': '10px'}),
                                html.A(
                                    dbc.Button("View Profile", color="primary", style={'display': 'block', 'margin': '0 auto', 'marginTop': '10px'}),
                                    href=dogs[0]["profile"],
                                    className="profile-button"
                                )
                            ]
                        ),
                    ), width=3, className="mb-4"  # 3 columns wide (1/4 of the row)
                ),
                # Second Column (Dog 2)
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody(
                            [
                                html.Img(src=dogs[1]["image"], className="dog-image", style={"width": "100%", "borderRadius": "8px"}),
                                html.H5(dogs[1]["name"], className="dog-name", style={'textAlign': 'center', 'marginTop': '10px'}),
                                html.A(
                                    dbc.Button("View Profile", color="primary", style={'display': 'block', 'margin': '0 auto', 'marginTop': '10px'}),
                                    href=dogs[1]["profile"],
                                    className="profile-button"
                                )
                            ]
                        ),
                    ), width=3, className="mb-4"  # 3 columns wide (1/4 of the row)
                ),
                # Third Column (Dog 3)
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody(
                            [
                                html.Img(src=dogs[2]["image"], className="dog-image", style={"width": "100%", "borderRadius": "8px"}),
                                html.H5(dogs[2]["name"], className="dog-name", style={'textAlign': 'center', 'marginTop': '10px'}),
                                html.A(
                                    dbc.Button("View Profile", color="primary", style={'display': 'block', 'margin': '0 auto', 'marginTop': '10px'}),
                                    href=dogs[2]["profile"],
                                    className="profile-button"
                                )
                            ]
                        ),
                    ), width=3, className="mb-4"  # 3 columns wide (1/4 of the row)
                ),
                # Fourth Column (Dog 4)
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody(
                            [
                                html.Img(src=dogs[3]["image"], className="dog-image", style={"width": "100%", "borderRadius": "8px"}),
                                html.H5(dogs[3]["name"], className="dog-name", style={'textAlign': 'center', 'marginTop': '10px'}),
                                html.A(
                                    dbc.Button("View Profile", color="primary", style={'display': 'block', 'margin': '0 auto', 'marginTop': '10px'}),
                                    href=dogs[3]["profile"],
                                    className="profile-button"
                                )
                            ]
                        ),
                    ), width=3, className="mb-4"  # 3 columns wide (1/4 of the row)
                ),
            ],
            justify="center",  # Center align all the columns in the row
        ),
    ],
    className="main-body",
    style={"paddingTop": "200px", "paddingLeft": "150px", "paddingRight": "150px", "paddingBottom": "200px", "backgroundColor": "#FAF3EB"}
)
