# -*- coding: utf-8 -*-

from kotti.events import ObjectInsert, ObjectUpdate
from kotti.events import subscribe

from .resources import Person

@subscribe(ObjectInsert, Person)
@subscribe(ObjectUpdate, Person)
def person_handler(event):
    person = event.object
    person.title = person.fullname
    person.owner = None
    person.in_navigation = False

