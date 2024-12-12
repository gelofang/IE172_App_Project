import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.exceptions import PreventUpdate
import dash_core_components as dcc

from app import app

# instead of app.layout, we just use the variable "layout" here
# We cannot really modify the "app" variable here, we only do it in index.py
layout = html.Div(
    [
        # Use a row to align the content and the image side by side
        dbc.Row(
            [
                # Column for the form content
                dbc.Col(
                    [
                        html.H1("Payment Module"),  # Heading for the Payment Module
                        html.P("Make a Donation"),
                        html.Br(),
                        html.P("Type of Donation"),
                        
                        # Donation Type Dropdown
                        dcc.Dropdown(
                            id='donation-dropdown',  # Unique ID for the Dropdown
                            options=[
                                {'label': 'Apple', 'value': 'apple'},
                                {'label': 'Banana', 'value': 'banana'},
                                {'label': 'Cherry', 'value': 'cherry'},
                            ],
                            style={'width': '50%'}  # Optional: adjust the width of the dropdown
                        ),
                        html.Div(
                            [
                                dbc.Label("For Option A, indicate rescue/s to sponsor", html_for="example-email"),
                                dbc.Input(type="email", id="example-email"),
                            ],
                            className="mb-3", style={'width': '50%'}
                        ),
                        html.Div(
                            [
                                dbc.Label("Payment Amount", html_for="example-email"),
                                dbc.Input(type="email", id="example-email"),
                            ],
                            className="mb-3", style={'width': '50%'}
                        ),
                        html.P("Mode of Payment"),
                        
                        # Payment Mode Dropdown
                        dcc.Dropdown(
                            id='payment-dropdown',  # Unique ID for the Dropdown
                            options=[
                                {'label': 'Cash', 'value': 'cash'},
                                {'label': 'Gcash', 'value': 'gcash'},
                                {'label': 'Credit Card', 'value': 'creditcard'},
                            ],
                            style={'width': '50%'}  # Optional: adjust the width of the dropdown
                        ),
                    ],
                    # Left column will take up 8/12 grid (large part of the screen)
                    width=8, 
                ),
                
                # Column for the image
                dbc.Col(
                    [
                        html.Img(
                            src="https://placedog.net/700/900?random=2",  # Path to the image file
                            style={"width": "100%", "height": "auto"}  # Ensure the image fits in the column
                            ),
                        dbc.Button(
                            "Register", 
                            id="register-button", 
                            color="primary", 
                            href="/register",
                            style={"marginTop": "20px"}  # Add some space between the image and the button
                        )
                    ],
                    
                    # Right column will take up 4/12 grid (smaller part of the screen)
                    width=4, 
                ),
            ]
        ),
    ],
    style={
        "paddingTop": "200px",
        "paddingLeft": "250px",
        "paddingRight": "250px",
        "paddingBottom": "200px",
        "backgroundColor": "#FAF3EB"
    }
)