#!/usr/bin/env python3
import cgi

form = cgi.FieldStorage()
login = form.getfirst("Login", "не задано")
password = form.getfirst("Password", "не задано")
head = """<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Hello page</title>
        </head>
        <body>"""

print("Content-type: text/html\n")
print(head)

print("<h1>Process your data</h1>")
print("<p>Login: {}</p>".format(login))
print("<p>Password: {}</p>".format(password))

print("""</body>
        </html>""")
