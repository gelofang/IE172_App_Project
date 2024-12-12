import dash
import dash_bootstrap_components as dbc
from dash import dcc, html

from app import app
from apps.navbars import adminSideNavbar as aSN

# Personal Information Tables
name = {
    "Last Name": "De La Cruz",
    "First Name": "Juan",
    "Middle Name": "Xander",
    "Suffix": "XIV"
}

address = {
    "Street Address": "63 Sunshine St.",
    "Barangay": "94",
    "City/Municipality": "Quezon City",
    "Province": "Metro Manila"
}

contacts = {
    "Contact Number": "09999999999",
    "Email Address": "antok@gmail.com",
    "Facebook Link": "fb.com/antoking",
    "Instagram Link": "ig.com/antoking"
}

misc = {
    "Date of Birth": "January 1, 2000",
    "Source of Income": "Stocks"
}

# Dwelling Information Table
dwelling = {
    "Type of Dwelling": "Apartment",
    "Dwelling Ownership": "Self-Owned",
    "Are Pets Allowed": "Yes"
}

petInfo = {
    "Pet Name":"Alpha",
    "Gender":"Male",
    "Age":"3",
    "Breed":"Alaskan Malamute",
    "Medical Condition":"Sleepy eepy",
    "Description":"He does his best"
}

householdInfo = {
    "Number of Household Members":"3",
    "All Members are supportive of adopting":"Yes",
    "Planning to Move":"No"
}

prelimMotivation = {
    "Best Description of Adopter":"Ok"
}

pawProjFoster = {
    "Reason for Fostering":"Companionship",
    "Has Experience":"Yes",
    "Willing to Shoulder Medical Expenses":"Yes"
}

noticeAdoptionFee = {
    "Aware and Agree?":"Yes"
}

adoptionInfo = {
    "WHO IS RESPONSIBLE FOR PET CARE?":"",
    "PET AS GIFT?":"",
    "OWNERSHIP EXPERIENCE":"",
    "VET CLINIC":"",
    "ALL PETS IN THE LAST FIVE YEARS":"",
    "STILL OWN ALL? IF NOT, WHAT HAPPENED?":""
}

otherInfo = {
    "HOW DID YOU FIND OUT ABOUT PAWSSION":"",
    "PROJECT AND ADOPTION PROGRAM?":"",
    "WHAT MADE YOU CONSIDER ADOPTING?":"",
    "COPY OF VALID ID":"",
    "AVAILABLE TIMES FOR ADOPTION INTERVIEW":""
}

# Function to generate a dbc.Table from a dictionary
def create_table(data_dict, fixed_width="150px"):
    table_rows = [html.Tr([html.Th(key, style={"width":fixed_width}), html.Td(value)]) for key, value in data_dict.items()]
    return dbc.Table([html.Tbody(table_rows)], bordered=True)

layout = html.Div(
    [
        aSN.adminSidebar(),
        html.Div(
            [
                dbc.Row(
                    [
                        dbc.Col(html.H2("Account Information", style={"color": "#dba514", "font-weight": "bold"}), width="auto"),
                        dbc.Col(
                            dbc.Button("Back", color="primary", href="/viewAdoptions", style={"width": "100px"}),  # Adjusted width for button
                            width="auto",
                            style={"textAlign": "right", },
                        ),
                    ],
                ),
                dbc.Row(
                    [
                        # Left column for Personal Information
                        dbc.Col(
                            [
                                html.H4("Adopter Personal Information"),
                                create_table(name),
                                create_table(address),
                                create_table(contacts),
                                create_table(misc),
                                html.H4("Preliminary Motivation"),
                                create_table(prelimMotivation),
                                html.H4("Pawssion Project Foster Volunteer"),
                                create_table(pawProjFoster),
                                html.H4("Notice on Adoption Fee"),
                                create_table(noticeAdoptionFee),
                            ],
                            width=6
                        ),
                        # Right column for Dwelling Information
                        dbc.Col(
                            [
                                html.H4("Adopter Dwelling Information"),
                                create_table(dwelling),
                                html.H4("Chosen Pet Information"),
                                create_table(petInfo),
                                html.H4("Household Information"),
                                create_table(householdInfo),
                                html.H4("Pawssion Project Foster Volunteer"),
                                create_table(pawProjFoster),
                                html.H4("Notice on Adoption Fee"),
                                create_table(noticeAdoptionFee),
                            ],
                            width=6
                        ),
                    ],
                ),
                dbc.Row(
                    [
                        html.H4("Adoption and Pet Care Information"),
                        create_table(adoptionInfo),
                        html.H4("Other Information"),
                        create_table(otherInfo),
                    ]
                )

            ],
            className="customer-admin-menu"
        )
    ]
)