import dash
import dash_bootstrap_components as dbc
from dash import dcc, html

layout = html.Div(
    [
        # Header section
        html.H1("Create an Account", style={'textAlign': 'center', 'marginBottom': '20px'}),

        # Paragraph describing the form
        html.P("Personal Information", style={'textAlign': 'center', 'marginBottom': '40px'}),

        # Registration form with grouped rows
        dbc.Form(
            [
                # Row 1: Last Name, First Name, Middle Name, Suffix
                dbc.Row(
                    [
                        dbc.Col(dbc.Form([dbc.Label("Last Name", html_for="last-name"),
                                               dbc.Input(type="text", id="last-name", placeholder="Enter Last Name", required=True)]), width=3),
                        dbc.Col(dbc.Form([dbc.Label("First Name", html_for="first-name"),
                                               dbc.Input(type="text", id="first-name", placeholder="Enter First Name", required=True)]), width=3),
                        dbc.Col(dbc.Form([dbc.Label("Middle Name", html_for="middle-name"),
                                               dbc.Input(type="text", id="middle-name", placeholder="Enter Middle Name")]), width=3),
                        dbc.Col(dbc.Form([dbc.Label("Suffix (e.g., Jr., III)", html_for="suffix"),
                                               dbc.Input(type="text", id="suffix", placeholder="Enter Suffix")]), width=3),
                    ],
                    className="mb-3"
                ),

                # Row 2: Address fields (Lot No./Bldg./Street Address, Barangay, City/Municipality, Province)
                dbc.Row(
                    [
                        dbc.Col(dbc.Form([dbc.Label("Lot No./Bldg./Street Address", html_for="address"),
                                               dbc.Input(type="text", id="address", placeholder="Enter Address", required=True)]), width=6),
                        dbc.Col(dbc.Form([dbc.Label("Barangay", html_for="barangay"),
                                               dbc.Input(type="text", id="barangay", placeholder="Enter Barangay", required=True)]), width=3),
                        dbc.Col(dbc.Form([dbc.Label("City/Municipality", html_for="city"),
                                               dbc.Input(type="text", id="city", placeholder="Enter City/Municipality", required=True)]), width=3),
                        dbc.Col(dbc.Form([dbc.Label("Province", html_for="province"),
                                               dbc.Input(type="text", id="province", placeholder="Enter Province", required=True)]), width=3),
                    ],
                    className="mb-3"
                ),

                # Row 3: Contact Number, Primary Email Address, Birthdate
                dbc.Row(
                    [
                        dbc.Col(dbc.Form([dbc.Label("Contact Number", html_for="contact-number"),
                                               dbc.Input(type="tel", id="contact-number", placeholder="Enter Contact Number", required=True)]), width=4),
                        dbc.Col(dbc.Form([dbc.Label("Primary Email Address", html_for="email"),
                                               dbc.Input(type="email", id="email", placeholder="Enter Email", required=True)]), width=4),
                        dbc.Col(dbc.Form([dbc.Label("Birthdate", html_for="birthdate"),
                                               dbc.Input(type="date", id="birthdate", required=True)]), width=4),
                    ],
                    className="mb-3"
                ),

                # Row 4: Facebook Link, Instagram Link
                dbc.Row(
                    [
                        dbc.Col(dbc.Form([dbc.Label("Facebook Link", html_for="facebook"),
                                               dbc.Input(type="url", id="facebook", placeholder="Enter Facebook Link")]), width=6),
                        dbc.Col(dbc.Form([dbc.Label("Instagram Link", html_for="instagram"),
                                               dbc.Input(type="url", id="instagram", placeholder="Enter Instagram Link")]), width=6),
                    ],
                    className="mb-3"
                ),

                # Row 5: Occupation or Source of Income
                dbc.Row(
                    [
                        dbc.Col(dbc.Form([dbc.Label("Occupation or Source of Income", html_for="occupation"),
                                               dbc.Input(type="text", id="occupation", placeholder="Enter Occupation or Source of Income", required=True)]), width=12),
                    ],
                    className="mb-3"
                ),
            ],
            style={"marginBottom": "30px"}
        ),

        # Buttons at the bottom-right
        html.Div(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            dbc.Button("Back", color="secondary", href="/previous-page", style={'width': '100px'}),
                            width="auto",
                        ),
                        dbc.Col(
                            dbc.Button("Next", color="primary", href="/next-page", style={'width': '100px'}),
                            width="auto",
                        ),
                    ],
                    justify="end",  # Align the buttons to the right
                    style={'paddingTop': '20px'},
                )
            ],
            style={"textAlign": "right"}
        )
    ],
    style={
        "paddingTop": "200px",
        "paddingLeft": "150px",
        "paddingRight": "150px",
        "paddingBottom": "200px",
        "backgroundColor": "#FAF3EB"
    }
)
