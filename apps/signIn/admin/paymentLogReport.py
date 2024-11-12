import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
import plotly.graph_objects as go

from app import app
from apps.sideNavbar import adminSideNavbar as aSN

# Sample data for the line graph
x_data = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]
y_data = [20, 30, 25, 35, 35]

# Create the line graph
fig = go.Figure(
    data=go.Scatter(x=x_data, y=y_data, mode="lines+markers", line=dict(color="cyan"))
)
fig.update_layout(
    xaxis_title=None,
    yaxis_title=None,
    margin=dict(l=20, r=20, t=20, b=20),
    height=400,
)

layout = html.Div(
    [
        aSN.adminSidebar(),
        html.Div(
            [
                dbc.Row(
                    [
                        dbc.Col(html.H2("Transaction Report", style={"color": "#dba514", "font-weight": "bold"}), width="auto"),
                        dbc.Col(
                            dbc.Button("Back", color="primary", href="/paymentLog", style={"width": "100px"}),  # Adjusted width for button
                            width="auto",
                            style={"textAlign": "right", },
                        )
                    ],
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.Label("Total Cash Inflow"),
                                html.Div(
                                    id="total-cash-inflow-display",
                                    children="$0",  # Default placeholder text
                                    style={
                                        "border": "1px solid #ccc",
                                        "padding": "10px",
                                        "background-color": "#f9f9f9",
                                        "border-radius": "5px",
                                        "width": "40%",
                                        "text-align": "center",
                                    },
                                )
                            ]
                        ),
                        dbc.Col(
                            dbc.DropdownMenu(
                                label="Period",
                                children=[
                                    dbc.DropdownMenuItem("Monthly"),
                                    dbc.DropdownMenuItem("Quarterly"),
                                    dbc.DropdownMenuItem("Yearly"),
                                ],
                            )
                        )
                    ],
                    style={"margin-bottom": "20px"},
                ),
                html.Div(
                    [
                        html.Label("Historic Cash Inflow"),
                        dcc.Graph(figure=fig),
                    ],
                    style={"margin-bottom": "20px"},
                ),
            ],
            className="customer-admin-menu"
        )
    ]
)
