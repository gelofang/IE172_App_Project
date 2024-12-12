import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.exceptions import PreventUpdate

from app import app

# instead of app.layout, we just use the variable "layout" here
# We cannot really modify the "app" variable here, we only do it in index.py
layout = html.Div(
    [
        dbc.Row(
        dbc.Col(html.A("< BACK", href="/home", className="back-link"), width="auto"),
        className="back-row"
    ),
    dbc.Row(
        dbc.Col(html.H1("ADOPTION APPLICATION", className="text-warning text-center"), className="title-row"),
    ),
    dbc.Row(
        dbc.Col([
            html.P("Hi Hooman! Thank you for your interest in giving a furever home to one of our rescues. "
                   "We have a lot of rescue dogs and cats ready for adoption both at the BULACAN SHELTER "
                   "and the BACOLOD SHELTER. Our adoption process is super easy!", className="intro-text"),

            html.H2("Adoption Process:", className="process-title mt-4"),
            html.Ol([
                html.Li("Fill out this form and wait to be contacted by the team. Please give us at least 1 WEEK to do our initial screening."),
                html.Li("Go through an interview via Zoom or Facebook Messenger with one of our volunteers."),
                html.Li("Visit the shelter, pay the Adoption Fee (₱1000) and bring home your new best fur friend (once you pass the interview).")
            ], className="process-steps"),

            html.P("Undecided about adopting but you want to learn more about what it takes to be a fur parent? "
                   "Go ahead and fill out this form and one of our volunteers will reach out to you to help assess "
                   "if you’re well-equipped to take on one of our rescues.", className="info-text mt-4"),

            html.P("IMPORTANT: Our Shelters are located in BULACAN and BACOLOD. Adopters should be willing to travel "
                   "to our Shelters to meet and pick-up the Rescue they want to adopt.", className="important-text mt-4 text-black"),

            html.P("Please also note that starting January 2022, we will already be implementing a PHP1,000 ADOPTION FEE "
                   "to help with the upkeep of the shelter and also to cover what we have spent for the rescues’ rehabilitation. "
                   "We also want to make sure that our adopters have the capacity to meet the needs of our rescues, "
                   "who we all treat as family.", className="important-text mt-4 text-black")
        ])
    ),
    dbc.Row(
        dbc.Col(
            dbc.Button("GET STARTED", href="/adopt/adoptionForm", className="btn-custom mx-1", style={'font-family': 'Roboto'}),
            className="text-center"
        )
    )
], className="p-4")