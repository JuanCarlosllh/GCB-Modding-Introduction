from google.appengine.ext import db
from models import entities

class Event(db.Model):
    name = db.StringProperty()
    description = db.StringProperty()
    date = db.DateProperty()
    
class EventDTO(object):
    def __init__(self, event):
        self.id = event.key().name()
        self.name = event.name
        self.description = event.description
        self.date = event.date
        
class EventDAO():
    @classmethod
    def get_all(cls):
        eventList = Event.all()
        if eventList:
            return [EventDTO(event) for event in eventList]
        else:
            return []
        
        
    @classmethod
    def create(cls, name, description, date):
        event = Event()
        event.name = name
        event.description = description
        event.date = date
        event.put()