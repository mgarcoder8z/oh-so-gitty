"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *
import string, random

class Welcome(Controller):
    def __init__(self, action):
            super(Welcome, self).__init__(action)
    def index(self):
		try:
			if session['attempt']:
				pass
		except:
			session['attempt'] = 1
		session['random_word'] = ''.join(random.sample(string.ascii_uppercase, 14))
		return self.load_view('index.html')

    def process(self):
        session['attempt'] += 1
        return redirect('/')

    def reset(self):
        session.pop('attempt')
        session.pop('random_word')
        return redirect('/')
