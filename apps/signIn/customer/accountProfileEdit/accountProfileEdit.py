import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.dependencies import Input, Output, State

from app import app
from apps.navbars import customerSideNavbar as cSN

sample_data = {
    "last_name": "De La Cruz",
    "first_name": "Juan",
    "middle_name": "Xander",
    "suffix": "XIV",
    "street_address": "63 Sunshine St.",
    "barangay": "94",
    "city": "Quezon City",
    "province": "Metro Manila",
    "contact_number": "09999999999",
    "email": "antok@gmail.com",
    "facebook": "N/A",
    "instagram": "N/A",
    "dob": "2000-01-01",
    "income": "Stocks",
}

layout = html.Div(
    [
        cSN.customerSidebar(),
        dbc.Container([
        dbc.Row([
            dbc.Col([
                # Form Heading
                html.H2("UPDATE ACCOUNT", style={"color": "#dba514", "font-weight": "bold"}),
                html.Hr(),
                html.H4("Personal Information", style={"font-weight": "bold"}),

                # Form Fields
                dbc.Form([
                    dbc.Row([
                        dbc.Col(dbc.Label("Last Name*", html_for="input-last-name"), width=3),
                        dbc.Col(dbc.Input(id="input-last-name", value=sample_data["last_name"], placeholder="Enter Last Name"), width=7),
                    ], className="mb-2"),
                    dbc.Row([
                        dbc.Col(dbc.Label("First Name*", html_for="input-first-name"), width=3),
                        dbc.Col(dbc.Input(id="input-first-name", value=sample_data["first_name"], placeholder="Enter First Name"), width=7),
                    ], className="mb-2"),
                    dbc.Row([
                        dbc.Col(dbc.Label("Middle Name*", html_for="input-middle-name"), width=3),
                        dbc.Col(dbc.Input(id="input-middle-name", value=sample_data["middle_name"], placeholder="Enter Middle Name"), width=7),
                    ], className="mb-2"),
                    dbc.Row([
                        dbc.Col(dbc.Label("Suffix (e.g., Jr., III)", html_for="input-suffix"), width=3),
                        dbc.Col(dbc.Input(id="input-suffix", value=sample_data["suffix"], placeholder="Enter Suffix"), width=7),
                    ], className="mb-2"),
                    dbc.Row([
                        dbc.Col(dbc.Label("Lot No./Bldg./Street Address*", html_for="input-street-address"), width=3),
                        dbc.Col(dbc.Input(id="input-street-address", value=sample_data["street_address"], placeholder="Enter Address"), width=7),
                    ], className="mb-2"),
                    dbc.Row([
                        dbc.Col(dbc.Label("Barangay*", html_for="input-barangay"), width=3),
                        dbc.Col(dbc.Input(id="input-barangay", value=sample_data["barangay"], placeholder="Enter Barangay"), width=7),
                    ], className="mb-2"),
                    dbc.Row([
                        dbc.Col(dbc.Label("City/Municipality*", html_for="input-city"), width=3),
                        dbc.Col(dbc.Input(id="input-city", value=sample_data["city"], placeholder="Enter City/Municipality"), width=7),
                    ], className="mb-2"),
                    dbc.Row([
                        dbc.Col(dbc.Label("Province*", html_for="input-province"), width=3),
                        dbc.Col(dbc.Input(id="input-province", value=sample_data["province"], placeholder="Enter Province"), width=7),
                    ], className="mb-2"),
                    dbc.Row([
                        dbc.Col(dbc.Label("Contact Number*", html_for="input-contact-number"), width=3),
                        dbc.Col(dbc.Input(id="input-contact-number", value=sample_data["contact_number"], placeholder="Enter Contact Number"), width=7),
                    ], className="mb-2"),
                    dbc.Row([
                        dbc.Col(dbc.Label("Primary Email Address*", html_for="input-email"), width=3),
                        dbc.Col(dbc.Input(id="input-email", type="email", value=sample_data["email"], placeholder="Enter Email Address"), width=7),
                    ], className="mb-2"),
                    dbc.Row([
                        dbc.Col(dbc.Label("Birthdate*", html_for="input-dob"), width=3),
                        dbc.Col(dbc.Input(id="input-dob", type="date", value=sample_data["dob"]), width=7),
                    ], className="mb-2"),
                    dbc.Row([
                        dbc.Col(dbc.Label("Facebook Link*", html_for="input-facebook"), width=3),
                        dbc.Col(dbc.Input(id="input-facebook", value=sample_data["facebook"], placeholder="Put N/A if not applicable"), width=7),
                    ], className="mb-2"),
                    dbc.Row([
                        dbc.Col(dbc.Label("Instagram Link*", html_for="input-instagram"), width=3),
                        dbc.Col(dbc.Input(id="input-instagram", value=sample_data["instagram"], placeholder="Put N/A if not applicable"), width=7),
                    ], className="mb-2"),
                    dbc.Row([
                        dbc.Col(dbc.Label("Occupation or Source of Income*", html_for="input-income"), width=3),
                        dbc.Col(dbc.Input(id="input-income", value=sample_data["income"], placeholder="Enter Occupation or Source of Income"), width=7),
                    ], className="mb-2"),
                ]),

                # Navigation Buttons
                dbc.Row([
                    dbc.Col(dbc.Button("Back", href="/accountProfile",id="back-button", color="secondary"), width="auto"),
                    dbc.Col(dbc.Button("Next", href="/accountProfile/edit/dwelling",id="next-button", color="success"), width="auto")
                ], className="mt-3", justify="end")
            ], width=9)
        ])
    ], className="customer-admin-menu")

    ]
)

@app.callback(
    Output("input-last-name", "value"),  # Placeholder output for demo purposes
    [Input("back-button", "n_clicks"), Input("next-button", "n_clicks")],
    prevent_initial_call=True
)
def handle_navigation(back_clicks, next_clicks):
    ctx = dash.callback_context
    if ctx.triggered:
        button_id = ctx.triggered[0]["prop_id"].split(".")[0]
        if button_id == "back-button":
            # Handle the "Back" button click action
            pass
        elif button_id == "next-button":
            # Handle the "Next" button click action
            pass
    return sample_data["last_name"]
