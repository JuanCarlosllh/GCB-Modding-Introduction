from modules.calendar.model import EventDAO, EventDTO

class CalendarService(object):
    @classmethod
    def create_event(self, name, description, date):
        EventDAO.create(name, description, date)
     
    @classmethod
    def get_events(self):
        return EventDAO.get_all()