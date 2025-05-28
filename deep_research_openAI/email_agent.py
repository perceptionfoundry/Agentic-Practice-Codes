import os
from typing import Dict

import sendgrid
from sendgrid.helpers.mail import Email, Mail,Content, To
from agents import Agent, function_tool


@function_tool
def send_email(subject: str, html_body: str) -> Dict[str:str]:
    sg = sendgrid.SendGridAPIClient(api_key=os.environ.get("SENDGRID_API_KEY"))
    from_email = Email(email="shahaider@gmail.com")
    to_mail = Email("shah@abc.com")
    content = Content("text/html", html_body)
    mail = Mail(from_email,to_mail,subject,content)
    mail_json = mail.get()
    response = sg.client.mail.send.post(request_body=mail_json)
    print("Email response", response.status_code)
    return {"status":"sucess"}

INSTRUCTION = """You are able to send a nicely formatted HTML email based on a detailed report.
you will be provided with a detailed report. you should use your tool to send one email, providing the
report converted into clean, well presented HTML with an appropriate subject line.
"""    

email_agent = Agent(
    name="EmailAgent",
    instructions=INSTRUCTION,
    model="gpt-4o-mini",
    tools=[send_email]
)