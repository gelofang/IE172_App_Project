# Usual Dash dependencies
import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate
from app import app
# Let us import the app object in case we need to define
# callbacks here

def adminSidebar():
    navlink_style = {'margin-right': '1em'}
    customerSidebar = html.Div(
        [
            html.Div(
                [
                    html.Img(src="/assets/icons/user (2).png", height="100px"),
                    html.H5("First Name", style={"fontWeight": "bold"}),
                    html.H6("Last Name", style={"fontWeight": "bold"}),
                    html.P("Title")
                ],
                className="navbar-logo"
            ),
            html.Hr(),
            dbc.Nav(
                [
                    dbc.NavLink(
                        [
                            html.Img(id="rescuesManagement-icon", src="/assets/icons/user-filled.png", height="21px", style={"margin-right": "8px"}),
                            "Rescues Management"
                        ],
                        href="/rescuesManagement", style=navlink_style, className="custom-navlink", id="rescuesManagement-link"
                    ),
                    dbc.NavLink(
                        [
                            html.Img(id="viewAdoptions-icon", src="/assets/icons/form-filled.png", height="21px", style={"margin-right": "5px"}),
                            "Adoption Applications"
                        ],
                        href="/viewAdoptions", style=navlink_style, className="custom-navlink", id="viewAdoptions-link"
                    ),
                    dbc.NavLink(
                        [
                            html.Img(id="paymentLog-icon", src="/assets/icons/transaction-history-outline.png", height="21px", style={"margin-right": "5px"}),
                            "Payment Logs"
                        ],
                        href="/paymentLog", style=navlink_style, className="custom-navlink", id="paymentLog-link"
                    ),

                ],
                vertical=True,
                pills=True,
            ),
        ],
        className="customer-admin-sideNavbar"
    )

    # Callback to update active class and icons
    @app.callback(
        [
            Output("rescuesManagement-link", "className"),
            Output("viewAdoptions-link", "className"),
            Output("paymentLog-link", "className"),
            Output("rescuesManagement-icon", "src"),
            Output("viewAdoptions-icon", "src"),
            Output("paymentLog-icon", "src"),
        ],
        [
            Input("url", "pathname")
        ]
    )
    def update_active_class_and_icons(pathname):
        active_class = "custom-navlink active"
        inactive_class = "custom-navlink"

        # Default icons
        icons = {
            "rescuesManagement": "/assets/icons/user-filled.png",
            "viewAdoptions": "/assets/icons/form-filled.png",
            "paymentLog": "/assets/icons/transaction-history-filled.png",
        }

        # Active icons
        active_icons = {
            "rescuesManagement": "/assets/icons/user-outline.png",
            "viewAdoptions": "/assets/icons/form-outline.png",
            "paymentLog": "/assets/icons/transaction-history-outline.png",
        }

        # Determine which link is active
        return [
            active_class if pathname.startswith("/rescuesManagement") else inactive_class,
            active_class if pathname.startswith("/viewAdoptions") else inactive_class,
            active_class if pathname.startswith("/paymentHistory") else inactive_class,
            
            active_icons["rescuesManagement"] if pathname.startswith("/rescuesManagement") else icons["rescuesManagement"],
            active_icons["viewAdoptions"] if pathname.startswith("/viewAdoptions") else icons["viewAdoptions"],
            active_icons["paymentLog"] if pathname.startswith("/paymentLog") else icons["paymentLog"],
        ]
    
    return customerSidebar