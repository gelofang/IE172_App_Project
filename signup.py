import dash
from dash import dcc, html, Input, Output, State
import dash_bootstrap_components as dbc
import hashlib, webbrowser

from app import app
from apps.navbars import headnfootTemplate as hft

# App initialization
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
[
        hft.create_header(),
        dcc.Location(id='url', refresh=True),
        html.Div(id='page_content'),
        hft.create_footer()
    ],

# Define the navigation bar
navbar = dbc.NavbarSimple(
    brand="Signup App",
    color="primary",
    dark=True,
)

# Define role selection layout
role_selection_layout = html.Div([
    html.H3("Choose your Account Type", className="text-center my-4"),
    dbc.RadioItems(
        id="role-selection",
        options=[
            {"label": "Client", "value": "client"},
            {"label": "Admin", "value": "admin"}
        ],
        inline=True,
        className="text-center my-3",
    ),
     html.Div(
        dbc.Button("Next", id="role-next-button", color="primary", className="my-3"),
        className="d-flex justify-content-center",
    ),
    html.Div(id="role-selection-output"),
])

# Define layouts for Client and Admin signups
client_signup_layout = html.Div([
    html.H4("Client Signup", className="my-3"),
    dbc.Input(id="client-username", placeholder="Enter username", type="text", className="mb-3"),
    dbc.Input(id="client-password", placeholder="Enter password", type="password", className="mb-3"),
    dbc.Button("Signup", id="client-signup-button", color="primary", className="mb-3"),
    dbc.Button("Back", id="client-back-button", color="secondary", className="mb-3"),
    html.Div(id="client-signup-output", className="mt-3"),
])

admin_signup_layout = html.Div([
    html.H4("Admin Signup", className="my-3"),
    dbc.Input(id="admin-username", placeholder="Enter username", type="text", className="mb-3"),
    dbc.Input(id="admin-password", placeholder="Enter password", type="password", className="mb-3"),
    dbc.Button("Signup", id="admin-signup-button", color="success", className="mb-3"),
    dbc.Button("Back", id="admin-back-button", color="secondary", className="mb-3"),
    html.Div(id="admin-signup-output", className="mt-3"),
])

# Define the main app layout
app.layout = dbc.Container([
    navbar,
    html.Div(id="main-content", children=role_selection_layout),
], fluid=True)

# Callbacks
@app.callback(
    Output("main-content", "children"),
    [Input("role-next-button", "n_clicks"),
     Input("client-back-button", "n_clicks"),
     Input("admin-back-button", "n_clicks")],
    [State("role-selection", "value")]
)
def handle_navigation(role_next_clicks, client_back_clicks, admin_back_clicks, role):
    ctx = dash.callback_context
    if not ctx.triggered:
        return role_selection_layout

    triggered_id = ctx.triggered[0]["prop_id"].split(".")[0]

    if triggered_id == "role-next-button" and role:
        if role == "client":
            return client_signup_layout
        elif role == "admin":
            return admin_signup_layout
        return html.Div("Please select a role.", className="text-danger")

    if triggered_id in ["client-back-button", "admin-back-button"]:
        return role_selection_layout

    return role_selection_layout

@app.callback(
    Output("client-signup-output", "children"),
    [Input("client-signup-button", "n_clicks")],
    [State("client-username", "value"), State("client-password", "value")]
)
def handle_client_signup(n_clicks, username, password):
    if n_clicks:
        if username and password:
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            return f"Client signed up with username: {username} (Password Hash: {hashed_password})"
        return "Please provide both username and password."
    return ""

@app.callback(
    Output("admin-signup-output", "children"),
    [Input("admin-signup-button", "n_clicks")],
    [State("admin-username", "value"), State("admin-password", "value")]
)
def handle_admin_signup(n_clicks, username, password):
    if n_clicks:
        if username and password:
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            return f"Admin signed up with username: {username} (Password Hash: {hashed_password})"
        return "Please provide both username and password."
    return ""

# Run the app
if __name__ == "__main__":
    webbrowser.open('http://127.0.0.1:8050/', new=0, autoraise=True)
    app.run_server(debug=False)