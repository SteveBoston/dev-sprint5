# This is whre you can start you python file for your week1 web app
# Name: Steve Gallagher

import flask
import functools

		

def login_required(method):
	@functools.wraps(method)
	def wrapper(*args, **kwargs):
		if 'username' in flask.session:
			return method(*args, **kwargs)
		else:
			flask.flash("You must be logged in to see this page.")
			return flask.redirect(flask.url_for('login'))
	return wrapper


