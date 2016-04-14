from modules.calendar.model import EventDAO, EventDTO

class CalendarService(object):
    @classmethod
    def create_event(cls, name, description, date):
        EventDAO.create(name, description, date)