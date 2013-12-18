# This is whre you can start you python file for your week1 web app
# Name: Steve Gallagher

import flask, flask.views
import os
import utils


class Music(flask.views.MethodView):
	@utils.login_required
	def get(self):
		songs = os.listdir('static/music')
		return flask.render_template('music.html', songs=songs)
	

