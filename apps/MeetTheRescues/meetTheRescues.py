import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.exceptions import PreventUpdate

from app import app

'''
Class Names
className="class-dog-cat-button"
className="cat-dog-cards"
classname="main-body"

'''
layout = html.Div(
    [
        html.Div(
            [
                html.H1("Find your New Bestfur-iend!", style={'textAlign': 'center'}),  # Centered header
                html.Br(),
                dbc.Row(  # Use Bootstrap Row
                    [
                        dbc.Col(  # First card
                            dbc.Card(
                                [
                                    dbc.CardImg(
                                        src="https://placedog.net/300/300?random=1",
                                        top=True,
                                        style={"opacity": 0.3},
                                    ),
                                    dbc.CardImgOverlay(
                                        dbc.CardBody(
                                            [
                                                html.P(
                                                    "Dogs thrive on Routine, Regular Exercise and Basic Training. They will need patience and dedication but will give you a lifetime of loyalty and companionship.",
                                                    className="class-dog-cat-card-text",
                                                ),
                                                dbc.Button("Dogs", color="primary", href="/meettherescues/dogs", className="class-dog-cat-button"),
                                            ],
                                        ),
                                    ),
                                ],
                                style={"width": "18rem"},
                            ),
                            width=6,  # This card takes up half the width of the row
                        ),
                        dbc.Col(  # Second card
                            dbc.Card(
                                [
                                    dbc.CardImg(
                                        src="https://placedog.net/300/300?random=2",
                                        top=True,
                                        style={"opacity": 0.3},
                                    ),
                                    dbc.CardImgOverlay(
                                        dbc.CardBody(
                                            [
                                                html.P(
                                                    "Cats are perfect for those looking for a Low-Maintenance and Independent pet. They can seem aloof and anti-social but once they open up, be ready for some cuddles!",
                                                    className="class-dog-cat-card-text"
                                                ),
                                                dbc.Button("Cats", color="primary", href="/meettherescues/cats", className="class-dog-cat-button"),
                                            ],
                                        ),
                                    ),
                                ],
                                style={"width": "18rem"},
                            ),
                            width=6,  # This card also takes up half the width of the row
                        ),
                    ],
                    justify="center",  # Centers the columns horizontally
                    style={'textAlign': 'center'},  # Ensures the content inside the row is centered
                    className="cat-dog-cards"
                ),
            ]
        ),
        html.Br(),
        html.Div(
            [
                html.P("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."),
                html.P("[INTRO ABOUT THE PETS WE HAVE AND HOW MANY ARE RESCUED ETC]"),
                html.P("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."),
                html.P("[DETAILS ABOUT THE SHELTERS]")
            ]
        )
    ],
    style={"paddingTop": "200px", "paddingLeft": "150px", "paddingRight": "150px", "paddingBottom": "200px", "backgroundColor": "#FAF3EB"}
)