import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.exceptions import PreventUpdate

from app import app

# instead of app.layout, we just use the variable "layout" here
# We cannot really modify the "app" variable here, we only do it in index.py
layout = html.Div(
    [
        html.H1("Frequently Asked Questions"),
        html.Div(
            [
                html.Div(
                    [
                        html.H2("Where are your shelters located?"),
                        html.P("Our Shelters are located in Bacolod City, Negros Occidental, and San Jose del Monte, Bulacan. ")
                    ]
                ),
                html.Div(
                    [
                        html.H2("What are your Official Social Media Accounts?"),
                        html.Ul(
                            [
                                html.Li("Instagram – @pawssionproject"),
                                html.Li("Facebook – facebook.com/PAWSsionProject"),
                                html.Li("YouTube – youtube.com/c/PawssionProject"),
                                html.Li("Twitter – @pawssionproject"),
                                html.Li("TikTok – @pawssionproject"),
                                html.Li("Lyka – @pawssionproject"),
                            ]
                        ),
                    ]
                ),
                html.Div(
                    [
                        html.H2("What is your Adoption Process?"),
                        html.P("Our adoption process consists of 3 simple steps!"),
                        html.Ol(
                            [
                                html.Li("You may start by finding a list of our rescues at: Meet the Rescues"),
                                html.Li("Once you feel ready to welcome a new family member to your home, you may fill out our Adoption Form through the ADOPT function. An Adoption Coordinator will then contact you for an interview."),
                                html.Li("Once you pass our screening process, you may schedule a shelter visit to meet our loving rescues, and take home your new best friend the same day!"),
                            ]
                        )
                    ]
                ),
                html.Div(
                    [
                        html.H2("What are the Requirements to adopt?"),
                        html.P("We do not have specific requirements, just that you pass our detailed Adoption Screening Process. Rest assured that all details you share with the team will be kept confidential and will only be used to assess your compatibility with our Rescues."),
                        html.P("But all we really ask from potential adopters is a lifetime commitment to consider our rescues as part of the family. This means ensuring their well-being at all times, and providing them with a loving environment for life.")
                    ]
                ),
                html.Div(
                    [
                        html.H2("Is there an Adoption Fee?"),
                        html.P("Please note that starting Jan 2022, we will be implementing a PHP1,000 ADOPTION FEE to help with the upkeep of the shelter and also to cover what we have spent for the rescues’ rehabilitation. We also want to make sure that our adopters have the capacity to meet the needs of our rescues, who we all treat as family.")
                    ]                
                ),
                html.Div(
                    [
                        html.H2("What name should I indicate upon transferring to your Bank Accounts?"),
                        html.P("You may indicate “Pawssion Project Foundation Inc.” for our Union Bank account. For BPO and BPI, you may input 'Ma. Lourdes Perez.'")
                    ]
                ),
                html.Div(
                    [
                        html.H2("Do you rescue?"),
                        html.P("At this time, our rescue operations are on hold as we strive to improve shelter conditions, and continue with the rehabilitation of more than 500 rescues under our care. However, we are more than willing to provide assistance as much as we can, considering there is already a concrete plan for the animal in need (i.e., who will shoulder the expenses, and where to bring the animal upon rescue and after being cleared at the vet). Kindly please provide us with details, so we may know how to assist you further")
                    ]
                ),
                html.Div(
                    [
                        html.H2("How can I report an Animal Cruelty Case?"),
                        html.P("For cases of animal abuse, please seek assistance from your barangay/PNP/NBI or call 911 to report the incident. Secure evidence such as photos and videos and find witnesses willing to testify and file an official complaint to help move the case forward and ensure justice."),
                        html.P("Pawssion Project is not a government agency and does not have the authority to persecute suspects. Because animal cruelty and pet neglect are criminal offenses, they must be reported to the authorities."),
                        html.P("More details from PAWS: https://paws.org.ph/cruelty-pet-neglect/")
                    ]
                ),
                html.Div(
                    [
                        html.H2("Can I surrender my pets?"),
                        html.P("We strongly discourage pet surrenders since pet abandonment and irresponsible pet ownership are the root causes of stray overpopulation. Thousands of abandoned pets/strays are euthanized every single day. For this reason, we strongly encourage exerting all possible efforts to keep your pets or rehome them to trusted individuals, since they truly should be regarded as part of the family. And family means nobody gets left behind.")
                    ]
                )
            ]
        ),
    ],
    style={"paddingTop":"200px","paddingLeft":"150px","paddingRight":"150px","paddingBottom":"200px","backgroundColor":"#FAF3EB"}
)