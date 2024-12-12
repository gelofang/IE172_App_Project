import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.exceptions import PreventUpdate

from app import app

# instead of app.layout, we just use the variable "layout" here
# We cannot really modify the "app" variable here, we only do it in index.py

cats = [
    {"name": "Zeta", "image": "https://placedog.net/300/300?random=1", "profile": "/meettherescues/cats/Zeta"},
    {"name": "Tau", "image": "https://placedog.net/300/300?random=2", "profile": "/meettherescues/cats/Tau"},
    {"name": "Gamma", "image": "https://placedog.net/300/300?random=3", "profile": "/meettherescues/cats/Gamma"},
    {"name": "Rho", "image": "https://placedog.net/300/300?random=4", "profile": "/meettherescues/cats/Rho"},
]

import dash
import dash_bootstrap_components as dbc
from dash import dcc, html

import dash
import dash_bootstrap_components as dbc
from dash import dcc, html

cats = [
    {"name": "Zeta", "image": "https://placedog.net/300/300?random=1", "profile": "/meettherescues/cats/Zeta"},
    {"name": "Tau", "image": "https://placedog.net/300/300?random=2", "profile": "/meettherescues/cats/Tau"},
    {"name": "Gamma", "image": "https://placedog.net/300/300?random=3", "profile": "/meettherescues/cats/Gamma"},
    {"name": "Rho", "image": "https://placedog.net/300/300?random=4", "profile": "/meettherescues/cats/Rho"},
]

layout = html.Div(
    [
        # Header Section (Header aligned left, search bar aligned right)
        dbc.Row(
            [
                dbc.Col(
                    html.H1("Meet the CATS!!!"),  # Header aligned to the left
                    width=8,  # Takes 8 columns of the row
                    style={'textAlign': 'left'}
                ),
                dbc.Col(
                    dcc.Input(
                        id="search-input",
                        placeholder="Search for a cat...",
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

        # Cat Gallery Section
        dbc.Row(  # Bootstrap Row for the cat cards
            [
                # First Column (Cat 1)
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody(
                            [
                                html.Img(src=cats[0]["image"], className="dog-image", style={"width": "100%", "borderRadius": "8px"}),
                                html.H5(cats[0]["name"], className="dog-name", style={'textAlign': 'center', 'marginTop': '10px'}),
                                html.A(
                                    dbc.Button("View Profile", color="primary", style={'display': 'block', 'margin': '0 auto', 'marginTop': '10px'}),
                                    href=cats[0]["profile"],
                                    className="profile-button"
                                )
                            ]
                        ),
                    ), width=3, className="mb-4"  # 3 columns wide (1/4 of the row)
                ),
                # Second Column (Cat 2)
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody(
                            [
                                html.Img(src=cats[1]["image"], className="dog-image", style={"width": "100%", "borderRadius": "8px"}),
                                html.H5(cats[1]["name"], className="dog-name", style={'textAlign': 'center', 'marginTop': '10px'}),
                                html.A(
                                    dbc.Button("View Profile", color="primary", style={'display': 'block', 'margin': '0 auto', 'marginTop': '10px'}),
                                    href=cats[1]["profile"],
                                    className="profile-button"
                                )
                            ]
                        ),
                    ), width=3, className="mb-4"  # 3 columns wide (1/4 of the row)
                ),
                # Third Column (Cat 3)
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody(
                            [
                                html.Img(src=cats[2]["image"], className="dog-image", style={"width": "100%", "borderRadius": "8px"}),
                                html.H5(cats[2]["name"], className="dog-name", style={'textAlign': 'center', 'marginTop': '10px'}),
                                html.A(
                                    dbc.Button("View Profile", color="primary", style={'display': 'block', 'margin': '0 auto', 'marginTop': '10px'}),
                                    href=cats[2]["profile"],
                                    className="profile-button"
                                )
                            ]
                        ),
                    ), width=3, className="mb-4"  # 3 columns wide (1/4 of the row)
                ),
                # Fourth Column (Cat 4)
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody(
                            [
                                html.Img(src=cats[3]["image"], className="dog-image", style={"width": "100%", "borderRadius": "8px"}),
                                html.H5(cats[3]["name"], className="dog-name", style={'textAlign': 'center', 'marginTop': '10px'}),
                                html.A(
                                    dbc.Button("View Profile", color="primary", style={'display': 'block', 'margin': '0 auto', 'marginTop': '10px'}),
                                    href=cats[3]["profile"],
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
    style={"paddingTop": "200px", "paddingLeft": "150px", "paddingRight": "150px", "paddingBottom": "200px", "backgroundColor": "#FAF3EB"}
)

