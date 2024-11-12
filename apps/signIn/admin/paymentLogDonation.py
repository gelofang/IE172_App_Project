import dash
import dash_bootstrap_components as dbc
from dash import dcc, html

from app import app
from apps.sideNavbar import adminSideNavbar as aSN

# Personal Information Tables
transactInfo = {
    "Transaction Number": "",
    "Client Name": "",
    "Client ID": "",
    "Transaction Type": ""
}

paymentInfo = {
    "Transaction ID": "",
    "Sponsored Rescues": "",
    "Sponsorship Frequency": "",
    "Payment Amount": "",
    "Payment Mode": "",
    "Proof of Payment": ""
}


# Function to generate a dbc.Table from a dictionary
def create_table(data_dict, fixed_width="150px"):
    table_rows = [html.Tr([html.Th(key, style={"width":fixed_width}), html.Td(value)]) for key, value in data_dict.items()]
    return dbc.Table([html.Tbody(table_rows)], bordered=True)

layout = html.Div(
    [
        aSN.adminSidebar(),
        html.Div(
            [
                dbc.Row(
                    [
                        dbc.Col(html.H2("View Transaction XXXXXX", style={"color": "#dba514", "font-weight": "bold"}), width="auto"),
                        dbc.Col(
                            dbc.Button("Back", color="primary", href="/paymentLog", style={"width": "100px"}),  # Adjusted width for button
                            width="auto",
                            style={"textAlign": "right", },
                        ),
                    ],
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.H4("Transaction Information"),
                                create_table(transactInfo),
                            ],
                            width=6
                        ),
                        dbc.Col(
                            [
                                html.H4("Payment Information"),
                                create_table(paymentInfo),
                            ],
                            width=6
                        ),
                    ],
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.H4("Verification"),
                                html.P("Would you like to tag this transaction as verified?"),
                                dbc.Button("Verify", color="primary", href="/paymentLog", style={"width": "100px"})
                            ],
                            width=6
                        ),
                    ],
                )
            ],
            className="customer-admin-menu"
        )
    ]
)
