import os
from models import custom_modules
from modules.calendar.controller import Calendar

custom_module = None

def register_module():

    namespaced_handlers = [(Calendar.URL, Calendar)]
    global_routes = []

    global custom_module

    custom_module = custom_modules.Module(
        'Calendar',
        'Calendar module',
        global_routes, namespaced_handlers)
    return custom_module