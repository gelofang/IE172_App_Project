import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.exceptions import PreventUpdate

from app import app
from apps.adopt import adopt

# instead of app.layout, we just use the variable "layout" here
# We cannot really modify the "app" variable here, we only do it in index.py
layout = html.Div(
    [
        dbc.Row(
        dbc.Col(html.A("HOME", href="/home", className="back-link"), width="auto"),
        className="back-row"
    ),
    dbc.Row(
        dbc.Col(html.H1("APPLICATION FORM SUBMITTED", className="text-warning text-center"), className="title-row"),
    ),
    dbc.Row(
        dbc.Col([
            html.P("Hi Hooman! Thank you for your interest in giving a furever home to one of our rescues. "
                   "We have a lot of rescue dogs and cats ready for adoption both at the BULACAN SHELTER "
                   "and the BACOLOD SHELTER. Our adoption process is super easy!", className="text-center"),

        ]),
    ),
    html.P(
                    "Thank you very much and we can't wait to see you soon, future Pawssion Project Fur Parent! 🙂",
                    className="text-center font-weight-bold",
    ),
], className="p-4")