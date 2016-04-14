from controllers import utils
from models import models

class Calendar(utils.BaseHandler):
    URL = '/calendar'
    
    def get(self):
        user = self.personalize_page_and_get_user()
        
        if user is not None:
            student = models.Student.get_enrolled_student_by_user(user)

            if student is not None:
                self.response.out.write("Hello! " + student.name)
            else:
                self.response.out.write("You are not registered")
                
        else:
            self.redirect('/')