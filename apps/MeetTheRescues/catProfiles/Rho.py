import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.exceptions import PreventUpdate

from app import app

# instead of app.layout, we just use the variable "layout" here
# We cannot really modify the "app" variable here, we only do it in index.py
layout = html.Div(
    [
        html.Div("< Back"),
        html.Div(
            [
                dbc.Carousel(
                    items=
                    [
                        {"key": "1", "src": "/static/images/slide1.svg"},
                        {"key": "2", "src": "/static/images/slide2.svg"},
                        {"key": "3", "src": "/static/images/slide3.svg"},
                        ],
                        controls=True,
                        indicators=False,
                ),
                html.Div([
                    html.H1("Rho"),
                    html.H4("Gender: Female"),
                    html.H4("Age: Adult"),
                    html.H4("Breed: Orange Cat"),
                    html.H4("Medical Condition: being a silly little kitten"),
                    html.H4("Description: I live in the Vet Clinic"),
                    dbc.Button("Adopt", color='dark', href="/register", style={'margin': '0 10px'}),
                    dbc.Button("Donate", color='dark', href="/register", style={'margin': '0 10px'})
                        ]
                    )
            ], className="profile-box",
        )
    ], style={"marginTop":"200px","marginLeft":"150px","marginRight":"150px","backgroundColor":"#FAF3EB"}
)