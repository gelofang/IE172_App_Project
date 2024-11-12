import webbrowser

import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

# Importing your app variable from app.py so we can use it
from app import app
from apps import headnfootTemplate as hft
from apps import home
from apps.adopt import adopt
from apps.companyInfo import contactUs, faqs, ourStory
from apps.donate import donate
from apps.MeetTheRescues import meetTheRescues, mtrCat, mtrDog
from apps.MeetTheRescues.dogProfiles import Alpha
from apps.MeetTheRescues.catProfiles import Rho
from apps.register import register
from apps.payment import payment
from apps.signIn import signIn
from apps.signIn.customer import accountProfile, adoptionApp, paymentHistory
from apps.signIn.customer.accountProfileEdit import accountProfileEdit, accountProfileEditDwelling, accountProfileEditPassword
from apps.signIn.admin import paymentLog, paymentLogAdoption, paymentLogDonation, paymentLogReport, rescueManagement, rescueManagementAdd, rescueManagementEdit, viewAdoptions, viewAdoptionsComplete
#from apps.headnfootTemplate import create_footer

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div(
    [
        hft.create_header(),
        dcc.Location(id='url', refresh=True),
        html.Div(id='page_content'),
        hft.create_footer()
    ],
    style={
        'display': 'flex',
        'flexDirection': 'column', 
        'height': '100vh',          
        'justifyContent': 'space-between',
    }
)

@app.callback(
    [
        Output('page_content', 'children')
    ],
    [
        Input('url', 'pathname')
    ]
)
def displaypage (pathname):
    
    # This code block extracts the id of the triggered input
    ctx = dash.callback_context
    if ctx.triggered:
        eventid = ctx.triggered[0]['prop_id'].split('.')[0]   
    else:
        raise PreventUpdate

        
    # This code block executes action based on the value of eventid
    if eventid == 'url':
        if pathname == '/' or pathname == '/home':
            returnlayout = home.layout

        elif pathname == '/adopt':
            returnlayout = adopt.layout
        
        elif pathname == '/donate':
            returnlayout = donate.layout
            
        elif pathname == '/payment':
            returnlayout = payment.layout

        elif pathname == '/meettherescues':
            returnlayout = meetTheRescues.layout
        elif pathname == '/meettherescues/dogs':
            returnlayout = mtrDog.layout
        elif pathname == '/meettherescues/dogs/Alpha':
            returnlayout = Alpha.layout
        elif pathname == '/meettherescues/cats':
            returnlayout = mtrCat.layout
        elif pathname == '/meettherescues/cats/Rho':
            returnlayout = Rho.layout

        elif pathname == '/ourstory':
            returnlayout = ourStory.layout

        elif pathname == '/faqs':
            returnlayout = faqs.layout

        elif pathname == '/contactus':
            returnlayout = contactUs.layout
        
        elif pathname == '/signin':
            returnlayout = signIn.layout

        elif pathname == '/register':
            returnlayout = register.layout

        #CUSTOMER SIDE BRANCH
        elif pathname == '/accountProfile':
            returnlayout = accountProfile.layout
        elif pathname == '/accountProfile/edit/personal':
            returnlayout = accountProfileEdit.layout
        elif pathname == '/accountProfile/edit/dwelling':
            returnlayout = accountProfileEditDwelling.layout
        elif pathname == '/accountProfile/edit/password':
            returnlayout = accountProfileEditPassword.layout

        elif pathname == '/adoptionApp':
            returnlayout = adoptionApp.layout

        elif pathname == '/paymentHistory':
            returnlayout = paymentHistory.layout
        
        #ADMIN SIDE BRANCH
        elif pathname == '/viewAdoptions':
            returnlayout = viewAdoptions.layout
        elif pathname == '/viewAdoptions/fullview':
            returnlayout = viewAdoptionsComplete.layout

        elif pathname == '/rescuesManagement':
            returnlayout = rescueManagement.layout
        elif pathname == '/rescuesManagement/add':
            returnlayout = rescueManagementAdd.layout
        elif pathname == '/rescuesManagement/edit':
            returnlayout = rescueManagementEdit.layout            
        
        elif pathname == '/paymentLog':
            returnlayout = paymentLog.layout
        elif pathname == '/paymentLog/donation':
            returnlayout = paymentLogDonation.layout
        elif pathname == '/paymentLog/adoption':
            returnlayout = paymentLogAdoption.layout
        elif pathname == '/paymentLog/generateReport':
            returnlayout = paymentLogReport.layout
            

        else:
            returnlayout = 'error404'
    
    else: 
        raise PreventUpdate
    
    return [returnlayout]

if __name__ == '__main__':
    webbrowser.open('http://127.0.0.1:8050/', new=0, autoraise=True)
    app.run_server(debug=False)
