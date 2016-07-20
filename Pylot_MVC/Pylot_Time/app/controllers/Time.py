"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from time import strftime, localtime
from system.core.controller import *

class Time(Controller):
    def __init__(self, action):
        super(Time, self).__init__(action)
        """
            This is an example of loading a model.
            Every controller has access to the load_model method.
        """
        self.load_model('WelcomeModel')
        self.db = self._app.db

        """

        This is an example of a controller method that will load a view for the client

        """

    def index(self):
		current_time = strftime("%b %d, %Y %I:%M %p", localtime())
		return self.load_view('index.html', time = current_time)
