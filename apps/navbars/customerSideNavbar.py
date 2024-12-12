# Usual Dash dependencies
import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate
from app import app
# Let us import the app object in case we need to define
# callbacks here

def customerSidebar():
    navlink_style = {'margin-right': '1em'}
    customerSidebar = html.Div(
        [
            html.Div(
                [
                    html.Img(src="/assets/icons/user (2).png", height="100px"),
                    html.H5("First Name", style={"fontWeight": "bold"}),
                    html.H6("Last Name", style={"fontWeight": "bold"})
                ],
                className="navbar-logo"
            ),
            html.Hr(),
            dbc.Nav(
                [
                    dbc.NavLink(
                        [
                            html.Img(id="accountProfile-icon", src="/assets/icons/user-filled.png", height="21px", style={"margin-right": "8px"}),
                            "Account Profile",
                        ],
                        href="/accountProfile", style=navlink_style, className="customer-admin-sideNavLink", id="accountProfile-link", 
                    ),
                    dbc.NavLink(
                        [
                            html.Img(id="adoptionApp-icon", src="/assets/icons/form-filled.png", height="21px", style={"margin-right": "5px"}),
                            "Adoption Application"
                        ],
                        href="/adoptionApp", style=navlink_style, className="customer-admin-sideNavLink", id="adoptionApp-link"
                    ),
                    dbc.NavLink(
                        [
                            html.Img(id="paymentHistory-icon", src="/assets/icons/transaction-history-outline.png", height="21px", style={"margin-right": "5px"}),
                            "Payment History"
                        ],
                        href="/paymentHistory", style=navlink_style, className="customer-admin-sideNavLink", id="paymentHistory-link"
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
            Output("accountProfile-link", "className"),
            Output("adoptionApp-link", "className"),
            Output("paymentHistory-link", "className"),
            Output("accountProfile-icon", "src"),
            Output("adoptionApp-icon", "src"),
            Output("paymentHistory-icon", "src"),
        ],
        [Input("url", "pathname")]
    )
    def update_active_class_and_icons(pathname):
        active_class = "custom-navlink active"
        inactive_class = "custom-navlink"

        # Default icons
        icons = {
            "accountProfile": "/assets/icons/user-filled.png",
            "adoptionApp": "/assets/icons/form-filled.png",
            "paymentHistory": "/assets/icons/transaction-history-filled.png",
        }

        # Active icons
        active_icons = {
            "accountProfile": "/assets/icons/user-outline.png",
            "adoptionApp": "/assets/icons/form-outline.png",
            "paymentHistory": "/assets/icons/transaction-history-outline.png",
        }

        # Determine which link is active
        return [
            active_class if pathname.startswith("/accountProfile") else inactive_class,
            active_class if pathname.startswith("/adoptionApp") else inactive_class,
            active_class if pathname.startswith("/paymentHistory") else inactive_class,
            
            active_icons["accountProfile"] if pathname.startswith("/accountProfile") else icons["accountProfile"],
            active_icons["adoptionApp"] if pathname.startswith("/adoptionApp") else icons["adoptionApp"],
            active_icons["paymentHistory"] if pathname.startswith("/paymentHistory") else icons["paymentHistory"],
        ]
    
    return customerSidebar