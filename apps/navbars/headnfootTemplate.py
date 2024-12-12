import dash
import dash_bootstrap_components as dbc
from dash import dcc, html

def create_header():
    header = html.Div(children=[
            html.Header(children=[
                html.Img(
                    src = "assets/PawssionProjectLogo.png",
                    style={'width': '400px',
                           'maxWidth': '400px',
                           'height': 'auto',
                           'margin': '20px 0'}
                ),
                dbc.Nav(children=[
                        dbc.Nav(children=[
                        html.Div([dbc.Button("Adopt", href="/adopt", className="btn-custom mx-1")]),
                        dbc.NavItem(dbc.NavLink("Donate", href="/donate", style={'color':'black'})),
                        dbc.NavItem(dbc.NavLink("Meet the Rescues", href="/meettherescues", style={'color':'black'})),
                        dbc.NavItem(dbc.NavLink("Our Story",  href="/ourstory", style={'color':'black'})),
                        dbc.NavItem(dbc.NavLink("FAQs", href="/faqs", style={'color':'black'})),
                        dbc.NavItem(dbc.NavLink("Hi, [Hooman]", href="/rescuesManagement", style={'color':'#556B2F', 'font-weight':'bold'})),
                        html.Div([dbc.Button("Logout", color='dark', href="/signin", style={'margin': '0 10px'})])
                    ],
                    navbar=True,
                    style={'justifyContent': 'center','display': 'flex','padding':'40px'} 
                                )
                               ]
                )
            ],
            style={
                'position': 'fixed',
                'top': '0',
                'left': '0',
                'right': '0',
                'backgroundColor': '#F7EFCF',
                'boxShadow': '0 2px 5px rgba(0,0,0,0.1)',
                'justifyContent': 'center',
                'display': 'flex',
                'marginBottom':'21vh'
            }
            )
        ],
        style={'z-index':'999'}
    )
    return header
    
    

def create_footer():
    footer = html.Div(children=[
        html.Footer(
            html.Div(children=[
                    html.P("Pawssion Project Foundation Inc.", style={'textAlign': 'center'}),
                    html.P("Bulacan Shelter: 1429 Paradise 1, Purok 7 Tungkong Mangga, SJDM, Bulacan", style={'textAlign': 'center'}),
                    html.P("Bacolod Shelter: Balay Pawssion, Google Maps: M2JV+5W, Bacolod, Negros Occidental", style={'textAlign': 'center'}),
                    html.P("info@pawssionproject.org", style={'textAlign': 'center'})
                ],
                style={
                    'padding': '20px',
                    'backgroundColor': '#343434',
                    'borderTop': '1px solid #dee2e6',
                    'color':'white',
                    }
                ),
                style={'marginTop': 'auto'}
            )   
        ],
        style={'display': 'flex', 'flexDirection': 'column', 'minHeight': '100vh', 'z-index':'9'},
    )
    return footer
