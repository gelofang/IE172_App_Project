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
            dbc.Col(html.P("Other Information", style={'textAlign': 'left', "font-weight": "bold", "font-family": "Roboto", 'marginBottom': '40px'}),
        )),
    
                # How did you find out about Pawssion Project
                dbc.CardGroup(
                    [
                        dbc.Label("How did you find out about Pawssion Project and our Adoption Program?", className="fw-bold"),
                        dbc.Input(type="text", placeholder="Enter your response", required=True),
                    ]
                ),
                
                # What made you consider adopting a rescue?
                dbc.CardGroup(
                    [
                        dbc.Label("What made you consider adopting a rescue?", className="fw-bold"),
                        dbc.Input(type="text", placeholder="Enter your response", required=True),
                    ]
                ),
                
                # Valid ID upload
                dbc.CardGroup(
                    [
                        dbc.Label("Please upload a copy of your Valid I.D.", className="fw-bold"),
                        dbc.Input(type="file", required=True),
                    ]
                ),
                
                # Date-Time Picker for Interview Availability
                dbc.CardGroup(
                    [
                        dbc.Label("Share your available time for a 1-hour Interview:", className="fw-bold mb-4"),
                        
                        # Date and Time Pickers stacked vertically
                        dbc.Col(
                            [
                                dbc.Label("Select Date"),
                                dcc.DatePickerSingle(
                                    id='date-picker',
                                    placeholder="Select a date",
                                    display_format='MM/DD/YYYY',
                                    style={"width": "100%"}
                                ),
                            ],
                            width=12,
                            className="mb-3"
                        ),
                        dbc.Col(
                            [
                                dbc.Label("Select Time"),
                                dcc.Input(
                                    id='time-picker',
                                    type='text',
                                    placeholder="e.g., 2:00 PM",
                                    debounce=True,
                                    style={"margin-left": '5px', 'width': "25%"}
                                ),
                            ],
                            width=12,
                            className="mb-3"
                        ),
                    ]
                ),

                # Footer with Back and Next buttons
        dbc.Row(
            dbc.Col([
                dbc.Button("BACK", color="secondary", href='/adopt/adoptionForm2', outline=True, className="btn-back mx-1", style={'font-family': 'Roboto','margin-top': '10px'}),
                dbc.Button("SUBMIT", href="/adopt/adoptionFormComplete", className="btn-custom mx-1", style={'font-family': 'Roboto','margin-top': '10px'})
            ], width="auto", className="d-flex justify-content-end mt-auto")
        ),
    ], className="p-4")