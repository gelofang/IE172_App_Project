from urllib.parse import parse_qs, urlparse

import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

from app import app
from apps.navbars import adminSideNavbar as aSN
from dbconnect import getDataFromDB, modifyDB


layout = html.Div(
    [
        aSN.adminSidebar(),
        dbc.Alert(id='rescueprofile_alert', is_open=False), # For feedback purposes
        html.Div(
            [
                dbc.Row(
                    [
                        dbc.Col(html.H2("Add a Rescue", style={"color": "#dba514", "font-weight": "bold"}), width="auto"),
                        dbc.Col(
                            dbc.Button("Back", color="primary", href="/rescuesManagement", style={"width": "100px"}),  # Adjusted width for button
                            width="auto",
                            style={"textAlign": "right", },
                        )
                    ],
                ),
                dbc.Row(
                    [
                        #Left Column
                        dbc.Col(
                            [
                                html.H6('Rescue Name'),
                                dbc.Input(id="input-rescue-name", type='text'),
                                html.Br(),
                                html.H6('Category'),
                                dbc.Input(id="input-category", type='text'),
                                html.Br(),
                                html.H6('Gender'),
                                dbc.Input(id="input-gender", type='text'),
                                html.Br(),
                                html.H6('Age'),
                                dbc.Input(id="input-age", type='text'),
                                html.Br(),
                                html.H6('Breed'),
                                dbc.Input(id="input-breed", type='text'),
                                html.Br(),
                                html.H6('Rescue Status'),
                                dbc.DropdownMenu(
                                    label="Menu",
                                    children=[
                                        dbc.DropdownMenuItem("In Care"),
                                        dbc.DropdownMenuItem("Critical Condition"),
                                        dbc.DropdownMenuItem("Passed On"),
                                        dbc.DropdownMenuItem("Adopted"),
                                    ],
                                )
                            ],
                            width=6
                        ),

                        #Right Column
                        dbc.Col(
                            [
                                html.H6('Medical Condition'),
                                dbc.Input(id="input-medCon", type='text'),
                                html.Br(),
                                html.H6('Description'),
                                dbc.Input(id="input-desc", type='text'),
                                html.Br(),
                                html.H6('Images/s'),
                                dbc.Button("add file goes here", color='light', href="/rescuesManagement/add", className="home-banner-button"),                       
                            ],
                            width=6
                        ),
                    ]
                ),
                dbc.Button("Update", id='rescueprofile_submit', color='primary', href="/rescuesManagement", style={'margin': '0 10px'}, n_clicks=0),
                dbc.Modal( # Modal = dialog box; feedback for successful saving.
                    [
                        dbc.ModalHeader(
                            html.H4('Save Success')
                        ),
                        dbc.ModalBody(
                            'Message here! Edit me please!'
                        ),
                        dbc.ModalFooter(
                            dbc.Button(
                                "Proceed",
                                href='/rescuesManagement' # Clicking this would lead to a change of pages
                            )
                        )
                    ],
                    centered=True,
                    id='rescueprofile_successmodal',
                    backdrop='static' # Dialog box does not go away if you click at the background
                )
            ], className="customer-admin-menu"
        ), 
    ],
)

        
@app.callback(
    [
        Output('rescueprofile_alert', 'color'),
        Output('rescueprofile_alert', 'children'),
        Output('rescueprofile_alert', 'is_open'),
        Output('rescueprofile_successmodal', 'is_open'),
    ],
    [Input('rescueprofile_submit', 'n_clicks')],
    [
        State('input-rescue-name', 'value'),
        State('input-category', 'value'),
        State('input-gender', 'value'),
        State('input-age', 'value'),
        State('input-breed', 'value'),
        State('input-medCon', 'value'),
        State('input-desc', 'value'),
    ],
)
def rescueprofile_saveprofile(submitbtn, rescueName, category, gender, age, breed, medCon, background):
    ctx = dash.callback_context
    if ctx.triggered:
        eventid = ctx.triggered[0]['prop_id'].split('.')[0]
        if eventid == 'rescueprofile_submit' and submitbtn:
            alert_open = False
            modal_open = False
            alert_color = ''
            alert_text = ''

            if not rescueName:
                alert_open = True
                alert_color = 'danger'
                alert_text = 'Please supply the name of the rescue.'
            elif not category:
                alert_open = True
                alert_color = 'danger'
                alert_text = 'Please supply the rescue category (cat or dog).'
            elif not gender:
                alert_open = True
                alert_color = 'danger'
                alert_text = 'Please indicate the gender of the rescue.'
            elif not age:
                alert_open = True
                alert_color = 'danger'
                alert_text = 'Please supply the age of the rescue.'
            elif not breed:
                alert_open = True
                alert_color = 'danger'
                alert_text = 'Please supply the breed.'
            elif not medCon:
                alert_open = True
                alert_color = 'danger'
                alert_text = 'Please supply the medical condition.'
            elif not background:
                alert_open = True
                alert_color = 'danger'
                alert_text = 'Please supply a description of the rescue.'
            else:
                try:
                    age = int(age)
                except ValueError:
                    alert_open = True
                    alert_color = 'danger'
                    alert_text = 'Age must be a valid number.'
                    return [alert_color, alert_text, alert_open, modal_open]

                sql = '''
                    INSERT INTO rescues (rescue_name, gender, age, breed, background, med_condition, category)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                '''
                values = [rescueName, gender, age, breed, background, medCon, category]

                print(f"Inserting data: {values}")
                modifyDB(sql, values)
                
                modal_open = True

            return [alert_color, alert_text, alert_open, modal_open]

        else:
            raise PreventUpdate
    else:
        raise PreventUpdate
