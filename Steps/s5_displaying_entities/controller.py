import datetime
import time

from controllers import utils
from models import models
from modules.calendar.service import CalendarService

class Calendar(utils.BaseHandler):
    URL = '/calendar'
    
    def get(self):
        user = self.personalize_page_and_get_user()
        
        if user is not None:
            student = models.Student.get_enrolled_student_by_user(user)

            if student is not None:
                
                events = CalendarService.get_events()
                for event in events:
                    self.response.out.write(event.name + " " + str(event.date) + ": "+ event.description + "<br >")
                    
            else:
                self.response.out.write("You are not registered")
                
        else:
            self.redirect('/')