# from django.shortcuts import render
# from django.shortcuts import get_object_or_404
# from django.views.decorators.csrf import csrf_exempt
from json import encoder
from django.http import HttpResponse
from rest_framework.views import APIView
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import socket
import json



class start(APIView):
    def post(self, request):
        response = json.dumps({
            "success": True,
            "data": "Successfully called v1 API ! Call /test/ to test and /send/ to send"
        })
        return HttpResponse(response, content_type='text/json')
    
    def get(self, request):
        url = request.build_absolute_uri('/')[:-1].strip("/")
        response = """<html>
                        <head>
                                <link rel="preconnect" href="https://fonts.googleapis.com">
                                <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                                <link href="https://fonts.googleapis.com/css2?family=Roboto&display=swap" rel="stylesheet">
                                <title> Mail API </title>
                        <style>
                                html{
                                        font-family: 'Roboto', sans-serif;
                                        padding: 1em;
                                }
                                h2{
                                        margin-bottom: 2em;
                                        padding-left: 1em;
                                }
                                #credits{
                                        position: fixed;
                                        bottom: 0;
                                        left: 0;
                                        padding: 0 0 1em 1em;
                                        color: #999
                                }
                        </style>
                        <div>
                            <u>TEST:</u>
                            <br>
                            <b>&nbsp&nbsp&nbsp&nbspPOST</b> """+url+"""/v1/test/<br>
                            &nbsp&nbsp&nbsp&nbsp{<br>
                            &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp"server_username" : "sender@domain.tld",<br>
                            &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp"server_password" : "SuperSecurePassword",<br>
                            &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp"server_name" : "mail.domain.tld",<br>
                            &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp"server_port" : "587",<br>
                            &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp"mail_from" : "YourName",<br>
                            &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp"mail_to" : "recipient@domain.tld",<br>
                            &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp"mail_subject" : "YourSubject",<br>
                            &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp"mail_body" : "Here is my HTML body !"<br>
                            &nbsp&nbsp&nbsp&nbsp}
                            &nbsp&nbsp&nbsp&nbsp
                        </div>
                        <br>
                        <div>
                            <u>SEND:</u>
                            <br>
                            <b>&nbsp&nbsp&nbsp&nbspPOST</b> """+url+"""/v1/send/<br>
                            &nbsp&nbsp&nbsp&nbsp{<br>
                            &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp"server_username" : "sender@domain.tld",<br>
                            &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp"server_password" : "SuperSecurePassword",<br>
                            &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp"server_name" : "mail.domain.tld",<br>
                            &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp"server_port" : "587",<br>
                            &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp"mail_from" : "YourName",<br>
                            &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp"mail_to" : "recipient@domain.tld",<br>
                            &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp"mail_subject" : "YourSubject",<br>
                            &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp"mail_body" : "Here is my HTML body !"<br>
                            &nbsp&nbsp&nbsp&nbsp}
                            &nbsp&nbsp&nbsp&nbsp
                        </div>
                        <br>
                        <div>
                            <u>Using CURL:</u><br>
                            <code>
                                curl -X POST """+url+"""/v1/send/ -d '{"server_username" : "sender@domain.tld", "server_password" : "SuperSecurePassword", "server_name" : "mail.domain.tld", "server_port" : "587", "mail_from" : "YourName", "mail_to" : "recipient@domain.tld", "mail_subject" : "YourSubject", "mail_body" : "Here is my HTML body !"}'
                            </code>
                        </div>
                        <i id="credits">Porvided by <a href='https://github.com/Ebenolt'> @ebenolt </a></i>
                    </html>"""
        return HttpResponse(response, content_type='text/html')

class test(APIView):
    def get(self, request):
        url = request.build_absolute_uri('/')[:-1].strip("/")
        response = """<html>
                        <head>
                                <link rel="preconnect" href="https://fonts.googleapis.com">
                                <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                                <link href="https://fonts.googleapis.com/css2?family=Roboto&display=swap" rel="stylesheet">
                                <title> Mail API </title>
                        <style>
                                html{
                                        font-family: 'Roboto', sans-serif;
                                        padding: 1em;
                                }
                                h2{
                                        margin-bottom: 2em;
                                        padding-left: 1em;
                                }
                                #credits{
                                        position: fixed;
                                        bottom: 0;
                                        left: 0;
                                        padding: 0 0 1em 1em;
                                        color: #999
                                }
                        </style>
                        <div>
                            <u>TEST:</u>
                            <br>
                            <b>&nbsp&nbsp&nbsp&nbspPOST</b> """+url+"""/v1/test/<br>
                            &nbsp&nbsp&nbsp&nbsp{<br>
                            &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp"server_username" : "sender@domain.tld",<br>
                            &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp"server_password" : "SuperSecurePassword",<br>
                            &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp"server_name" : "mail.domain.tld",<br>
                            &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp"server_port" : "587",<br>
                            &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp"mail_from" : "YourName",<br>
                            &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp"mail_to" : "recipient@domain.tld",<br>
                            &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp"mail_subject" : "YourSubject",<br>
                            &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp"mail_body" : "Here is my HTML body !"<br>
                            &nbsp&nbsp&nbsp&nbsp}
                            &nbsp&nbsp&nbsp&nbsp
                        </div>
                        <br>
                        <div>
                            <u>SEND:</u>
                            <br>
                            <b>&nbsp&nbsp&nbsp&nbspPOST</b> """+url+"""/v1/send/<br>
                            &nbsp&nbsp&nbsp&nbsp{<br>
                            &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp"server_username" : "sender@domain.tld",<br>
                            &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp"server_password" : "SuperSecurePassword",<br>
                            &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp"server_name" : "mail.domain.tld",<br>
                            &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp"server_port" : "587",<br>
                            &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp"mail_from" : "YourName",<br>
                            &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp"mail_to" : "recipient@domain.tld",<br>
                            &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp"mail_subject" : "YourSubject",<br>
                            &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp"mail_body" : "Here is my HTML body !"<br>
                            &nbsp&nbsp&nbsp&nbsp}
                            &nbsp&nbsp&nbsp&nbsp
                        </div>
                        <br>
                        <div>
                            <u>Using CURL:</u><br>
                            <code>
                                curl -X POST """+url+"""/v1/send/ -d '{"server_username" : "sender@domain.tld", "server_password" : "SuperSecurePassword", "server_name" : "mail.domain.tld", "server_port" : "587", "mail_from" : "YourName", "mail_to" : "recipient@domain.tld", "mail_subject" : "YourSubject", "mail_body" : "Here is my HTML body !"}'
                            </code>
                        </div>
                        <i id="credits">Porvided by <a href='https://github.com/Ebenolt'> @ebenolt </a></i>
                    </html>"""
        return HttpResponse(response, content_type='text/html')

    def post(self, request):
        try:
            payload = json.loads(request.body)
            requirements = ["server_username", "server_password", "server_name", "server_port", "mail_from", "mail_to", "mail_subject", "mail_body"]
            response = json.dumps({
                "success": True,
                "data": "Successfull test, all requirements are OK !"
            })
            for req in requirements:
                if not(req in payload.keys()):
                    response = json.dumps({
                        "success": False,
                        "data": "Missing parameters",
                        "required": {
                            "server_username" : "sender@domain.tld",
                            "server_password" : "SuperSecurePassword",
                            "server_name" : "mail.domain.tld",
                            "server_port" : "587",
                            "mail_from" : "YourName",
                            "mail_to" : "recipient@domain.tld",
                            "mail_subject" : "YourSubject",
                            "mail_body" : "Here<br>is<br>my<br>body (in HTML) !"
                        }
                    })

        except:
            response = json.dumps({
                "success": False,
                "data": "Missformated JSON",
                "required": {
                    "server_username" : "sender@domain.tld",
                    "server_password" : "SuperSecurePassword",
                    "server_name" : "mail.domain.tld",
                    "server_port" : "587",
                    "mail_from" : "YourName",
                    "mail_to" : "recipient@domain.tld",
                    "mail_subject" : "YourSubject",
                    "mail_body" : "Here<br>is<br>my<br>body (in HTML) !"
                }
            })
        return HttpResponse(response, content_type='text/json')



class sendmail(APIView):
    def get(self, request):
        url = request.build_absolute_uri('/')[:-1].strip("/")
        response = """<html>
                        <head>
                                <link rel="preconnect" href="https://fonts.googleapis.com">
                                <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                                <link href="https://fonts.googleapis.com/css2?family=Roboto&display=swap" rel="stylesheet">
                                <title> Mail API </title>
                        <style>
                                html{
                                        font-family: 'Roboto', sans-serif;
                                        padding: 1em;
                                }
                                h2{
                                        margin-bottom: 2em;
                                        padding-left: 1em;
                                }
                                #credits{
                                        position: fixed;
                                        bottom: 0;
                                        left: 0;
                                        padding: 0 0 1em 1em;
                                        color: #999
                                }
                        </style>
                        <div>
                            <u>TEST:</u>
                            <br>
                            <b>&nbsp&nbsp&nbsp&nbspPOST</b> """+url+"""/v1/test/<br>
                            &nbsp&nbsp&nbsp&nbsp{<br>
                            &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp"server_username" : "sender@domain.tld",<br>
                            &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp"server_password" : "SuperSecurePassword",<br>
                            &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp"server_name" : "mail.domain.tld",<br>
                            &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp"server_port" : "587",<br>
                            &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp"mail_from" : "YourName",<br>
                            &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp"mail_to" : "recipient@domain.tld",<br>
                            &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp"mail_subject" : "YourSubject",<br>
                            &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp"mail_body" : "Here is my HTML body !"<br>
                            &nbsp&nbsp&nbsp&nbsp}
                            &nbsp&nbsp&nbsp&nbsp
                        </div>
                        <br>
                        <div>
                            <u>SEND:</u>
                            <br>
                            <b>&nbsp&nbsp&nbsp&nbspPOST</b> """+url+"""/v1/send/<br>
                            &nbsp&nbsp&nbsp&nbsp{<br>
                            &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp"server_username" : "sender@domain.tld",<br>
                            &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp"server_password" : "SuperSecurePassword",<br>
                            &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp"server_name" : "mail.domain.tld",<br>
                            &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp"server_port" : "587",<br>
                            &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp"mail_from" : "YourName",<br>
                            &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp"mail_to" : "recipient@domain.tld",<br>
                            &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp"mail_subject" : "YourSubject",<br>
                            &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp"mail_body" : "Here is my HTML body !"<br>
                            &nbsp&nbsp&nbsp&nbsp}
                            &nbsp&nbsp&nbsp&nbsp
                        </div>
                        <br>
                        <div>
                            <u>Using CURL:</u><br>
                            <code>
                                curl -X POST """+url+"""/v1/send/ -d '{"server_username" : "sender@domain.tld", "server_password" : "SuperSecurePassword", "server_name" : "mail.domain.tld", "server_port" : "587", "mail_from" : "YourName", "mail_to" : "recipient@domain.tld", "mail_subject" : "YourSubject", "mail_body" : "Here is my HTML body !"}'
                            </code>
                        </div>
                        <i id="credits">Porvided by <a href='https://github.com/Ebenolt'> @ebenolt </a></i>
                    </html>"""
        return HttpResponse(response, content_type='text/html')
    def post(self, request):
        try:
            payload = json.loads(request.body)
            requirements = ["server_username", "server_password", "server_name", "server_port", "mail_from", "mail_to", "mail_subject", "mail_body"]
            for req in requirements:
                if not(req in payload.keys()):
                    response = json.dumps({
                        "success": False,
                        "data": "Missing parameters",
                        "required": {
                            "server_username" : "sender@domain.tld",
                            "server_password" : "SuperSecurePassword",
                            "server_name" : "mail.domain.tld",
                            "server_port" : "587",
                            "mail_from" : "YourName",
                            "mail_to" : "recipient@domain.tld",
                            "mail_subject" : "YourSubject",
                            "mail_body" : "Here<br>is<br>my<br>body (in HTML) !"
                        }
                    })
                    return HttpResponse(response, content_type='text/json')
        except:
            response = json.dumps({
                "success": False,
                "data": "Missformated JSON",
                "required": {
                    "server_username" : "sender@domain.tld",
                    "server_password" : "SuperSecurePassword",
                    "server_name" : "mail.domain.tld",
                    "server_port" : "587",
                    "mail_from" : "YourName",
                    "mail_to" : "recipient@domain.tld",
                    "mail_subject" : "YourSubject",
                    "mail_body" : "Here<br>is<br>my<br>body (in HTML) !"
                }
            })
            return HttpResponse(response, content_type='text/json')
        try:
            msg=MIMEMultipart()
            msg['From'] = payload["mail_from"]+" <"+payload["server_username"]+">"
            msg['To'] = payload["mail_to"]
            msg['Subject'] = payload["mail_subject"]


            mailbody = payload["mail_body"]
            msg.attach(MIMEText(mailbody,'html'))

            mailcontent=msg.as_string()

            server = smtplib.SMTP(payload["server_name"], payload["server_port"])
            server.starttls()
            server.login(payload["server_username"], payload["server_password"])
            server.sendmail(payload["server_username"],payload["mail_to"], mailcontent)
            server.quit()
            response = json.dumps({
                "success": True,
                "data": "Successfull call, mail sent !"
            })
        except:
            response = json.dumps({
                "success": False,
                "data": "Connection to server failed"
            })

        return HttpResponse(response, content_type='text/json')
