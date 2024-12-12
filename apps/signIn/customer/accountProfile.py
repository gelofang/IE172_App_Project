import dash
import dash_bootstrap_components as dbc
from dash import dcc, html

from app import app
from apps.navbars import customerSideNavbar as cSN

# Personal Information Tables
table_1 = {
    "Last Name": "De La Cruz",
    "First Name": "Juan",
    "Middle Name": "Xander",
    "Suffix": "XIV"
}

table_2 = {
    "Street Address": "63 Sunshine St.",
    "Barangay": "94",
    "City/Municipality": "Quezon City",
    "Province": "Metro Manila"
}

table_3 = {
    "Contact Number": "09999999999",
    "Email Address": "antok@gmail.com",
    "Facebook Link": "fb.com/antoking",
    "Instagram Link": "ig.com/antoking"
}

table_4 = {
    "Date of Birth": "January 1, 2000",
    "Source of Income": "Stocks"
}

# Dwelling Information Table
table_5 = {
    "Type of Dwelling": "Apartment",
    "Dwelling Ownership": "Self-Owned",
    "Are Pets Allowed": "Yes"
}

# Function to generate a dbc.Table from a dictionary
def create_table(data_dict):
    table_rows = [html.Tr([html.Th(key), html.Td(value)]) for key, value in data_dict.items()]
    return dbc.Table([html.Tbody(table_rows)], bordered=True)

layout = html.Div(
    [
        cSN.customerSidebar(),
        html.Div(
            [
                dbc.Row(
                    [
                        dbc.Col(html.H2("Account Information"), width="auto"),
                        dbc.Col(
                            dbc.Button("Edit", color="primary", href="/accountProfile/edit/personal", style={"width": "100px"}),  # Adjusted width for button
                            width="auto",
                            style={"textAlign": "right", },
                            className="d-flex align-items-center justify-content-end"
                        ),
                    ],
                ),
                dbc.Row(
                    [
                        # Left column for Personal Information
                        dbc.Col(
                            [
                                html.H4("Personal Information"),
                                create_table(table_1),
                                html.Br(),
                                create_table(table_2),
                                html.Br(),
                                create_table(table_3),
                                html.Br(),
                                create_table(table_4),
                            ],
                            width=6
                        ),
                        # Right column for Dwelling Information
                        dbc.Col(
                            [
                                html.H4("Dwelling Information"),
                                create_table(table_5),
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

className="customer-admin-menu"