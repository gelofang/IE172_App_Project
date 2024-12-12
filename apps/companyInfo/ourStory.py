import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.exceptions import PreventUpdate

from app import app

# instead of app.layout, we just use the variable "layout" here
# We cannot really modify the "app" variable here, we only do it in index.py
layout = html.Div(
    style={"paddingTop":"200px","paddingLeft":"150px","paddingRight":"150px","paddingBottom":"200px","backgroundColor":"#FAF3EB"},
    children=[
        html.H2("50 dogs on death row. To be executed by gunshot. What would you do?", style={}),
        html.P("One brave woman refused to just stand by, and that is how Pawssion Project was born. Founded in October 2018 by Malou Perez, Pawssion Project Foundation Inc. is a non-profit organization dedicated to the rescue, rehabilitation and rehoming abused, abandoned and neglected animals. Pawssion Project began in Bacolod, armed simply with a lot of hope, courage and the unwavering support of a few good friends. After that first pound rescue, numerous reports poured in one after another, which eventually led to the opening of a second shelter in Bulacan in mid 2019. Since then, the journey has led Pawssion Project to more than 2000 rescues, and thankfully over 1000 rehomed animals."),
        html.Div(id="3-volunteer-images"),
        html.P("However, the problem is far greater than what Pawssion Project and other animal welfare organizations alone can surmount. Dogs continue to be executed in city pounds, and the number of strays and neglected pets are rising dramatically. But we believe that WE CAN ALL DO SOMETHING to help improve animal welfare in our country. Do not close your eyes to animal cruelty, help spread awareness that there is a law against it (RA8485). Be a responsible pet owner and encourage others to do the same. Promote neutering of pets to help control overpopulation. Adopt, foster, sponsor, volunteer, donate or advocate. Every little action counts."),
        html.P("The road to better animal welfare is long, and we at Pawssion Project will continue on our journey to be the voice of our helpless furry friends. But we need all the help we can get. Will you join us?"),

        html.Div([
            html.Div([
                html.H1("Our Mission", style={}),
                html.P("To rescue, rehabilitate, and rehome abused, abandoned and neglected animals."),
            ]),
            html.Div([
                html.H1("Our Vision", style={}),
                html.P("The creation of animal-friendly communities that foster kindness to all living creatures with the goal of achieving the Five Freedoms for all stray animals."),
            ])
        ]),

        html.Div([
            html.Div(className="two-images"),
            html.Div([
                html.H1("COME VISIT US!", style={}),
                html.P("Bacolod Shelter: Balay Pawssion, Hacienda Feliza, Brgy. Granada, Bacolod City"),
                html.P("Bulacan Shelter: 1429 Paradise 1, Purok 7 Tungkong Mangga, SJDM, Bulacan"),
            ])
        ]),

        html.Div([
            html.H1("Our Initiatives", style={}),
            html.Div([
                html.Div([
                    html.H1("STRAY FEEDING", style={}),
                    html.P("Feeding strays helps the homeless and voiceless animals survive. It also inspires people to be kind. It makes us realize how much power we have to change the lives both of animals and people. Have strayfeeding become part of your routine."),
                ]),
                html.Div([
                    html.H1("SPAY & NEUTER", style={}),
                    html.P("We have always acknowledged that rescuing is just a band aid solution. This is why Pawssion Project firmly believes that KAPON is really the SOLUTION. Help save lives by sponsoring the neuter cost of a rescue!"),
                ]),
                html.Div([
                    html.H1("RELIEF DRIVE", style={}),
                    html.P("We believe that spreading kindness and love, especially in times of emergencies and calamities, should be prioritized, and everything else will follow. So, we also make it a point to extend assistance to humans as well."),
                ]),
            ])
        ]),
    ]
)