import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.exceptions import PreventUpdate

from app import app

# instead of app.layout, we just use the variable "layout" here
# We cannot really modify the "app" variable here, we only do it in index.py

# Layout definition
layout = html.Div(
    [
        # Heading
        html.H1("Enter your User Credentials", style={'textAlign': 'center'}),

        # Email input section
        html.Div(
            [
                dbc.Label("Email", html_for="example-email"),
                dbc.Input(type="email", id="example-email", placeholder="Enter email"),
            ],
            className="mb-3",
        ),

        # Password input section
        html.Div(
            [
                dbc.Label("Password", html_for="example-password"),
                dbc.Input(type="password", id="example-password", placeholder="Enter password"),
                # Forgot password link
                html.A("Forgot Password?", href="/forgot-password", style={'float': 'right', 'marginTop': '10px'}),
            ],
            className="mb-3",
        ),

        # Continue button with green background
        dbc.Button("Continue", color="success", style={"marginTop": "20px"}),

        # Sign-up prompt
        html.Div(
            [
                html.P("Don't have an account?", style={'textAlign': 'center'}),
                html.A("Sign Up", href="/register", style={'textAlign': 'center', 'display': 'block'}),
            ],
            style={'marginTop': '20px', 'textAlign': 'center'}
        ),
    ],
    style={
        "paddingTop": "200px",
        "paddingLeft": "150px",
        "paddingRight": "150px",
        "paddingBottom": "200px",
        "backgroundColor": "#FAF3EB"
    }
)