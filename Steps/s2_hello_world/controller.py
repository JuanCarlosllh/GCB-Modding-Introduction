from controllers import utils

class Calendar(utils.BaseHandler):
    URL = '/calendar'
    
    def get(self):
        self.response.out.write("Hello World!")