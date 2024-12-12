import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, dash_table
from dash.exceptions import PreventUpdate

from app import app
from apps.navbars import customerSideNavbar as cSN

data = [
    {
        "TRANSACTION ID": "00001",
        "TRANSACTION TYPE": "DONATION-A",
        "DATE OF PAYMENT": "10-31-24",
        "AMOUNT PAID": "PX,XXX.00",
        "PAYMENT METHOD": "GCASH",
        "PAYMENT STATUS": "PENDING",
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
                                    html.Th("TRANSACTION ID"),
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
                                    html.Td("DONATION-A"),
                                    html.Td("10-31-24"),
                                    html.Td("PX,XXX.00"),
                                    html.Td("GCash"),
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