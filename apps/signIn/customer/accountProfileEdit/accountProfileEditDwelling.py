import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.dependencies import Input, Output, State

from app import app
from apps.sideNavbar import customerSideNavbar as cSN


layout = html.Div(
    [
        cSN.customerSidebar(),
        dbc.Container([
            html.H2("UPDATE ACCOUNT"),
            html.H4("Dwelling Information"),
    
    # Type of Dwelling
        dbc.Row([
            dbc.Label("Type of Dwelling*", className="mb-2"),
            dbc.Col(
                dbc.DropdownMenu(
                    label="Select Dwelling Type",
                    id="dwelling-type-dropdown",
                    children=[
                        dbc.DropdownMenuItem("Condo Unit", id="dwelling-condo"),
                        dbc.DropdownMenuItem("Apartment/Townhouse", id="dwelling-apartment"),
                        dbc.DropdownMenuItem("Bungalow/Single-storey House", id="dwelling-bungalow"),
                        dbc.DropdownMenuItem("Multi-Storey House", id="dwelling-multi-storey"),
                    ],
                    className="mb-3"
                )
            )
        ]),

        # Dwelling Ownership
        dbc.Row([
            dbc.Label("Dwelling Ownership*", className="mb-2"),
            dbc.Col(
                dbc.DropdownMenu(
                    label="Select Ownership Status",
                    id="ownership-dropdown",
                    children=[
                        dbc.DropdownMenuItem("Owned", id="ownership-owned"),
                        dbc.DropdownMenuItem("Renting", id="ownership-renting"),
                    ],
                    className="mb-3"
                )
            )
        ]),

        # Pets Allowed (conditional)
        dbc.Row([
            dbc.Label("If renting, are pets allowed?*", className="mb-2"),
            dbc.Col(
                dbc.DropdownMenu(
                    label="Select Option",
                    id="pets-allowed-dropdown",
                    children=[
                        dbc.DropdownMenuItem("Yes", id="pets-yes"),
                        dbc.DropdownMenuItem("No", id="pets-no"),
                        dbc.DropdownMenuItem("N/A", id="pets-na"),
                    ],
                    className="mb-3",
                    disabled=False  # Initially disabled until 'Renting' is selected
                )
            )
        ]),

        # Buttons
        dbc.Row([
            dbc.Col(dbc.Button("BACK", href='/accountProfile/edit/personal',color="secondary", className="me-2"), width="auto"),
            dbc.Col(dbc.Button("NEXT", href='/accountProfile/edit/password', color="primary"), width="auto")
        ])
    ], className="customer-admin-menu")

    ]
)


