import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.exceptions import PreventUpdate

from app import app

# instead of app.layout, we just use the variable "layout" here
# We cannot really modify the "app" variable here, we only do it in index.py
layout = html.Div(
    [   
        html.Div(
            [
                html.Div(
                    [
                        html.Div(
                            html.H1("Join the Pawssion Project!")
                        ),
                        html.Div(
                            html.H2("Our mission is to rescue.")
                        ),
                        html.Div(
                            html.H2("Our dream is that one day, we won't have to.")
                        ),
                        html.Div(
                            [dbc.Button("Help The Cause", color='light', href="/signin", className="home-banner-button")],className="banner-button-body"
                        ),
                    ], className="home-banner-text"
                )
            ],
            className="home-banner-main"),
        html.Div(
            [
                html.Div(
                    [
                        html.H1("Adopt"),
                        html.P("Many of our Adoptables from our Bulacan and Bacolod Shelters have been rescued from death row, from local pounds or from abusive environments. By choosing to adopt, you are giving them the chance to find a new home and to feel the love and security they deserve.")
                    ], className="home-column", style={'backgroundColor':'#FFFFFF'}
                ),
                html.Div(
                    [
                        html.H1("Donate"),
                        html.P("As a non-profit organization, Pawssion Project operates and relies heavily on donations from the community. We are always called upon to rescue animals suffering from abandonment, abuse, injury or neglect and none of it is possible without your support.")
                    ],
                    className="home-column", style={'backgroundColor':'#000000','color':'#FFFFFF'}
                )
            ], className="columns"
        )
    ], style={"paddingTop":"133px"}
)