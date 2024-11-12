import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, dash_table
from dash.exceptions import PreventUpdate

from app import app
from apps.sideNavbar import customerSideNavbar as cSN

data = [
    {
        "APPLICATION ID": "00001",
        "APPLICATION DATE": "10-31-2024",
        "NAME OF RESCUE": "DOG 1",
        "INTERVIEW SCHEDULE": "11-01-2024 13:00:00",
        "INTERVIEW STATUS": "PENDING",
        "PAYMENT": "Payment",
        "APPLICATION STATUS": "PENDING"
    }
]

layout=html.Div(
    [
        cSN.customerSidebar(),
        dbc.Col(
            [
                html.H3("VIEW MY APPLICATIONS", style={"color": "#fcbf49", "margin-top": "20px"}),
                    dbc.Table(
                        # Table header
                        [
                            html.Thead(
                                html.Tr([
                                    html.Th("APPLICATION ID"),
                                    html.Th("APPLICATION DATE"),
                                    html.Th("NAME OF RESCUE"),
                                    html.Th("INTERVIEW SCHEDULE"),
                                    html.Th("INTERVIEW STATUS"),
                                    html.Th("PAYMENT"),
                                    html.Th("APPLICATION STATUS")
                                ]),
                                style={"backgroundColor": "white", "color": "black"}
                            ),
                            # Table body with a single row of sample data
                            html.Tbody(
                                html.Tr([
                                    html.Td("00001"),
                                    html.Td("10-31-2024"),
                                    html.Td("DOG 1"),
                                    html.Td("11-01-2024 13:00:00"),
                                    html.Td("PENDING"),
                                    html.Td(dbc.Button("Payment", href="/payment", className="btn btn-warning")),
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

