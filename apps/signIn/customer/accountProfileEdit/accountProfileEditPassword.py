import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.dependencies import Input, Output, State

from app import app
from apps.navbars import customerSideNavbar as cSN


layout = html.Div(
    [
        cSN.customerSidebar(),
        dbc.Container(
            [
                html.H2("UPDATE ACCOUNT"),
                html.H4("Prompt Your Account Key"),
                dbc.Row(
                    [
                        dbc.Label("Password*", html_for="password", width=12, className="mb-2"),
                        dbc.Col(
                            dbc.Input(type="password", id="password", placeholder="Enter password", className="mb-3"),
                            width=12
                        )
                    ]
                ),
                dbc.Row(
                    [
                        dbc.Label("Re-enter Password*", html_for="re-password", width=12, className="mb-2"),
                        dbc.Col(
                            dbc.Input(type="password", id="re-password", placeholder="Re-enter password", className="mb-3"),
                            width=12
                        )
                    ]
                ),
    
                # Buttons
                dbc.Row(
                    [
                        dbc.Col(dbc.Button("BACK", href='/accountProfile/edit/dwelling', color="secondary", className="me-2"), width="100px"),
                        dbc.Col(dbc.Button("UPDATE", href='/accountProfile', color="primary"), width="100px")
                    ],
                    justify="end"
                )
            ],
            className="customer-admin-menu"
        )
    ]
)
