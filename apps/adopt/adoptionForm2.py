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
        # Header section
        dbc.Row(
            dbc.Col(html.H1("APPLICATION FORM", className="text-warning text-left", style={ 'margin-top':'1px'})),
         ),
        # Paragraph describing the form
        dbc.Row(
            dbc.Col(html.P("Adoption & Pet Care Information", style={'textAlign': 'left', "font-weight": "bold", "font-family": "Roboto", 'marginBottom': '40px'}),
        )),
        
        # Name of rescue
        dbc.Row(
            [
                dbc.Label("Name of rescue you want to adopt*", className="form-label"),
                dbc.Input(type="text", placeholder="Enter name of rescue"),
            ],
            className="mb-3",
        ),

        # Pet's care responsibility
        dbc.Row(
            [
                dbc.Label("Who will be responsible for the pet’s care?*", className="form-label"),
                dbc.Input(type="text", placeholder="Enter responsible person's name"),
            ],
            className="mb-3",
        ),

        # Adopt as a gift
        dbc.Row(
            [
                dbc.Label("Do you plan to adopt this pet as a gift?*", className="form-label"),
                dbc.RadioItems(
                    options=[
                        {"label": "Yes", "value": "Yes"},
                        {"label": "No", "value": "No"},
                    ],
                    inline=True,
                ),
            ],
            className="mb-3",
        ),

        # Ownership experience
        dbc.Row(
            [
                dbc.Label("Which of the following best describes your ownership experience*", className="form-label"),
                dbc.Select(
                    options=[
                        {"label": "First-time pet owner", "value": "First-time"},
                        {"label": "Experienced pet owner", "value": "Experienced"},
                        {"label": "Professional pet caregiver", "value": "Professional"},
                    ]
                ),
            ],
            className="mb-3",
        ),

        # Veterinary clinic name
        dbc.Row(
            [
                dbc.Label("Name of veterinary clinic that you intend to bring your pet for check-ups*", className="form-label"),
                dbc.Input(type="text", placeholder="Enter clinic name"),
            ],
            className="mb-3",
        ),

        # List of past pets
        dbc.Row(
            [
                dbc.Label("List of all the pets you have owned in the past 5 years (e.g., 3 Persian cats, 1 Golden Retriever, 1 Husky)*", className="form-label"),
                dbc.Input(type="text", placeholder="Enter list of past pets"),
            ],
            className="mb-3",
        ),

        # Ownership of previous pets
        dbc.Row(
            [
                dbc.Label("Do you still own all of them? If not, kindly indicate what happened and cause of death for each.*", className="form-label"),
                dbc.Input(type="text", placeholder="Enter details of previous pets"),
            ],
            className="mb-3",
        ),

# Footer with Back and Next buttons
        dbc.Row(
            dbc.Col([
                dbc.Button("BACK", color="secondary", href='/adopt/adoptionForm', outline=True, className="btn-back mx-1", style={'font-family': 'Roboto','margin-top': '10px'}),
                dbc.Button("NEXT", href="/adopt/adoptionForm3", className="btn-custom mx-1", style={'font-family': 'Roboto','margin-top': '10px'})
            ], width="auto", className="d-flex justify-content-end mt-auto")
        ),
    ], className="p-4")