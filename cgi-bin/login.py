#!/usr/bin/env python3
import cgi
import html
import os
import funct
import http.cookies
import json

cookie = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))
form = cgi.FieldStorage()
ref = form.getvalue('ref')
login = form.getvalue('login')
password = form.getvalue('pass')
USERS = 'cgi-bin/users'

try:
	with open(USERS, "r") as user:
		pass
except IOError:
	print("Can't load users DB")

def login_page(error):
	if error == "error":
		printError = "<b style='color: red'>Somthing wrong :( I'm sad about this, but try again!</b></br></br>"
	else:
		printError = "<b style='color: red'>First you need to login.</b></br></br>"	
		
	funct.head("Login page")
	
	print('<center><form name="auth" action="login.py" class="form-horizontal" method="post">')
	print(printError)
	print('<label for="login"> Login: </label>  <input type="text" name="login" class="form-control">')
	print('<label for="pass"> Pass: </label>   <input type="password" name="pass" class="form-control">')
	print('<input type="hidden" value="%s" name="ref">' % ref)
	print('<button type="submit" name="Login" value="Enter">Sign Up</button>')
	print('</form></center>')

if login is None:		
	login_page("n")

if login is not None and password is not None:
	for f in open(USERS, 'r'):
		users = json.loads(f)	
		if login in users['login'] and password == users['password']:
			print("Set-cookie: login=%s; expires=Wed May 18 03:33:20 2033; path=/cgi-bin/; httponly" % login)
			print("Set-cookie: FirstName=%s; expires=Wed May 18 03:33:20 2033; path=/cgi-bin/; httponly" % users['firstName'])
			print("Set-cookie: LastName=%s; expires=Wed May 18 03:33:20 2033; path=/cgi-bin/; httponly" % users['lastName'])
			if ref is None:
				ref = "index.html"		
			print("Content-type: text/html\n")
			print('<html><head><title>Redirecting</title><meta charset="UTF-8">')
			print('<link href="/style.css" rel="stylesheet">')
			print('<meta http-equiv="refresh" content="0; url=%s">' % ref)
		else:
			login_page("error")
			break

funct.footer()



