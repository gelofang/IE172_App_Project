import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.exceptions import PreventUpdate

from app import app

link = {'color': 'blue'}
# instead of app.layout, we just use the variable "layout" here
# We cannot really modify the "app" variable here, we only do it in index.py
layout = html.Div(
    [
        html.H1("Contact Us"),
        html.P(
            [
                "For questions and general inquiries you can email us at:",
                html.A("info@pawssionproject.org", href="mailto:info@pawssionproject.org", style=link),
                html.Br(),
                "For Adoption inquiries:",
                html.A("adoption@pawssionproject.org", href="mailto:adoption@pawssionproject.org", style=link),
                html.Br(),
                "For questions about our Sponsor-A-Rescue Program:",
                html.A("sponsorships@pawssionproject.org", href="mailto:sponsorships@pawssionproject.org", style=link),
                html.Br(),
                "If you’re interested in building a partnership with Pawssion Project:",
                html.A("partners@pawssionproject.org", href="mailto:partners@pawssionproject.org", style=link),
                html.Br(),
                "For urgent concerns, please send a message to our Facebook page for guidance on the appropriate next steps:"
            ]
        )
    ],
    style={"marginTop":"200px","marginLeft":"150px","marginRight":"150px","backgroundColor":"#FAF3EB"}
)