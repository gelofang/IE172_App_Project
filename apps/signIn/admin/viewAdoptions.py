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
                                dbc.Col(html.H3("VIEW ADOPTION APPLICATIONS", style={"color": "#fcbf49", "margin-top": "20px"})),
                                dbc.Col(
                                    dbc.InputGroup([
                                        dbc.Input(placeholder="Search for Adoption Entry", type="text"),
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
                                        html.Th("VIEW APPLICATION"),
                                        html.Th("APPLICATION DATE"),
                                        html.Th("NAME OF RESCUE"),
                                        html.Th("INTERVIEW SCHEDULE"),
                                        html.Th("INTERVIEW STATUS"),
                                        html.Th("PAYMENT STATUS"),
                                        html.Th("APPLICATION STATUS"),
                                    ]),
                                    style={"backgroundColor": "white", "color": "black"}
                                ),
                                # Table body with a single row of sample data
                                html.Tbody(
                                    html.Tr([
                                        html.Td("00001"),
                                        html.Td(
                                            dbc.Button("View", color='light', href="/viewAdoptions/fullview", className="home-banner-button")
                                        ),
                                        html.Td("10-31-24"),
                                        html.Td("Dog 1"),
                                        html.Td("11-01-2024 13:00:00"),
                                        html.Td(
                                            dbc.DropdownMenu(
                                                id="dwelling-type-dropdown",
                                                children=[
                                                    dbc.DropdownMenuItem("Ongoing", id="dwelling-condo"),
                                                    dbc.DropdownMenuItem("Finished", id="dwelling-apartment"),
                                                ],
                                                className="mb-3"
                                            )
                                        ),
                                        html.Td("PENDING"),
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