import os

from common import tags
from models import custom_modules

from modules.calendar.controller import Calendar

custom_module = None

RESOURCES_PATH = '/modules/calendar/resources/'

def register_module():

    namespaced_handlers = [(Calendar.URL, Calendar)]
    global_routes = [(os.path.join(RESOURCES_PATH, '.*'), tags.ResourcesHandler)]

    global custom_module

    custom_module = custom_modules.Module(
        'Calendar',
        'Calendar module',
        global_routes, namespaced_handlers)
    return custom_module