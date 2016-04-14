import os
import datetime
import time

from controllers import utils
from controllers import sites

from models import models
from modules.calendar.service import CalendarService

CALENDAR_TEMPLATES = os.path.normpath('/modules/calendar/templates')

class Calendar(utils.BaseHandler):
    URL = '/calendar'
    
    def get(self):
        user = self.personalize_page_and_get_user()
        
        if user is not None:
            student = models.Student.get_enrolled_student_by_user(user)

            if student is not None:
                events = CalendarService.get_all_events()

                path = sites.abspath(self.app_context.get_home_folder(), CALENDAR_TEMPLATES)
                template = self.get_template('calendar_view.html', additional_dirs=[path])
                self.response.out.write(template.render(self.template_value, events=events))
            else:
                self.response.out.write("You are not registered")
                
        else:
            self.redirect('/')