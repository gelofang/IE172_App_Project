import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.exceptions import PreventUpdate

from app import app

# instead of app.layout, we just use the variable "layout" here
# We cannot really modify the "app" variable here, we only do it in index.py
import dash
import dash_bootstrap_components as dbc
from dash import dcc, html

layout = html.Div(
    [
        # "< Back" link with a redirect to the previous page
        html.Div(
            [
                html.A("< Back", href="/meettherescues/dogs", style={"textDecoration": "none", "fontSize": "18px", "color": "#007bff"}),
            ],
            style={'marginBottom': '20px', 'textAlign': 'left'}
        ),

        # Profile box section with image carousel on the left and text on the right
        dbc.Row(
            [
                # Image Carousel on the left (taking 6 columns of the row)
                dbc.Col(
                    dbc.Carousel(
                        items=[
                            {"key": "1", "src": "https://placedog.net/300/200?random=1"},
                            {"key": "2", "src": "https://placedog.net/300/200?random=2"},
                            {"key": "3", "src": "https://placedog.net/300/200?random=3"},
                        ],
                        controls=True,
                        indicators=False,
                    ),
                    width=6,  # 6 columns of the row for the image carousel
                ),

                # Text information on the right (taking 6 columns of the row)
                dbc.Col(
                    html.Div(
                        [
                            html.H1("Alpha"),  # Name of the pet
                            html.H4("Gender: Male"),
                            html.H4("Age: Adult"),
                            html.H4("Breed: Pitbull"),
                            html.H4("Medical Condition: vaccinated and neutered, confined because of Suspected Chronic Kidney Disease"),
                            html.H4("Description: I live in the Vet Clinic"),
                            dbc.Button("Adopt", color='dark', href="/register", style={'margin': '0 10px'}),
                            dbc.Button("Donate", color='dark', href="/register", style={'margin': '0 10px'})
                        ]
                    ),
                    width=6,  # 6 columns of the row for the text section
                )
            ]
        ),
    ],
    style={"marginTop": "200px", "marginLeft": "150px", "marginRight": "150px", "paddingBottom": "200px", "backgroundColor": "#FAF3EB"}
)
