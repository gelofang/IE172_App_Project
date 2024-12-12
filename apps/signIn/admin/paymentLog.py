import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.exceptions import PreventUpdate

from app import app
from apps.navbars import adminSideNavbar as aSN

layout=html.Div(
    [
        aSN.adminSidebar(),
        html.Div(
            [
                dbc.Col(
                    [
                        dbc.Row(
                            [
                                dbc.Col(html.H3("Transaction History", style={"color": "#fcbf49", "margin-top": "20px"})),
                                dbc.Col(
                                    dbc.Button("GENERATE REPORT", color='light', href="/paymentLog/generateReport", className="home-banner-button")
                                ),
                                dbc.Col(
                                    dbc.InputGroup([
                                        dbc.Input(placeholder="Search for Transaction", type="text"),
                                        dbc.Button("FIND", color="success"),
                                    ]),
                                    width="auto"
                                ),
                            ], align="center"
                        ),
                        dbc.Table(
                            # Table header
                            [
                                html.Thead(
                                    html.Tr([
                                        html.Th("APPLICATION ID"),
                                        html.Th("VIEW PAYMENT"),
                                        html.Th("CLIENT NAME"),
                                        html.Th("TRANSACTION TYPE"),
                                        html.Th("DATE OF PAYMENT"),
                                        html.Th("AMOUNT PAID"),
                                        html.Th("PAYMENT METHOD"),
                                        html.Th("PAYMENT STATUS"),
                                    ]),
                                    style={"backgroundColor": "white", "color": "black"}
                                ),
                                # Table body with a single row of sample data
                                html.Tbody(
                                    html.Tr([
                                        html.Td("00001"),
                                        html.Td(
                                            dbc.Button("View", color='light', href="/paymentLog/donation", className="home-banner-button")
                                        ),
                                        html.Td("Maria Juana"),
                                        html.Td("Donation"),
                                        html.Td("11-01-2024"),
                                        html.Td("Php 1,000.00"),
                                        html.Td("GCASH"),
                                        html.Td("PENDING")
                                    ])
                                ),
                                html.Tbody(
                                    html.Tr([
                                        html.Td("00002"),
                                        html.Td(
                                            dbc.Button("View", color='light', href="/paymentLog/adoption", className="home-banner-button")
                                        ),
                                        html.Td("Maria Juana"),
                                        html.Td("Adoption"),
                                        html.Td("11-01-2024"),
                                        html.Td("Php 1,000.00"),
                                        html.Td("Cash"),
                                        html.Td("PENDING")
                                    ])
                                )
                            ],
                            bordered=True,
                            hover=True,
                            responsive=True,
                            striped=True,
                            style={"margin-top": "20px"}
                        )
                    ],
                    width=9,
                    className="customer-admin-menu"
                )
            ]
        )
    ]
)