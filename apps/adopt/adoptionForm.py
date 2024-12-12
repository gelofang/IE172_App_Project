import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.exceptions import PreventUpdate

from app import app

# instead of app.layout, we just use the variable "layout" here
# We cannot really modify the "app" variable here, we only do it in index.py
layout = html.Div(
    [
        # Header section
        dbc.Row(
            dbc.Col(html.H1("APPLICATION FORM", className="text-warning text-left", style={ 'margin-top':'1px'})),
         ),
        # Paragraph describing the form
        dbc.Row(
            dbc.Col(html.P("Household Information", style={'textAlign': 'left', "font-weight": "bold", "font-family": "Roboto", 'marginBottom': '40px'}),
        )),    
        # Main form
        dbc.Row(
            dbc.Col([           
                dbc.CardGroup([
                    dbc.Label("Number of household members*", className="mt-3"),
                    dbc.Select(id="household-members", options=[{"label": str(i), "value": i} for i in range(1, 11)], required=True)
                ]),

                # Line break after the select box
                html.Br(),

                # Supportive radio buttons (in a separate row)
                dbc.Row([
                    dbc.Col([
                        dbc.Label("Are all members of the household supportive in adopting?*", className="mt-3"),
                    ])
                ]),

                dbc.Row([
                    dbc.Col([
                        dbc.RadioItems(
                            options=[
                                {"label": "Yes", "value": "yes"},
                                {"label": "No", "value": "no"}
                            ],
                            id="supportive",
                            inline=True,
                        ),
                    ], width=12),
                ]),

                # Move radio buttons (in a separate row)
                dbc.Row([
                    dbc.Col([
                        dbc.Label("Are you planning to move in the future?*", className="mt-3"),
                    ])
                ]),

                dbc.Row([
                    dbc.Col([
                        dbc.RadioItems(
                            options=[
                                {"label": "Yes", "value": "yes"},
                                {"label": "No", "value": "no"}
                            ],
                            id="move",
                            inline=True,
                        ),
                    ], width=12),
                ]),

            ], width=8)
        ),


        # Footer with Back and Next buttons
        dbc.Row(
            dbc.Col([
                dbc.Button("BACK", color="secondary", href='/adopt', outline=True, className="btn-back mx-1", style={'font-family': 'Roboto','margin-top': '10px'}),
                dbc.Button("NEXT", href="/adopt/adoptionForm2", className="btn-custom mx-1", style={'font-family': 'Roboto','margin-top': '10px'})
            ], width="auto", className="d-flex justify-content-end mt-auto")
        ),
    ], className="p-4")