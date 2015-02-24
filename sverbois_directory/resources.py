# -*- coding: utf-8 -*-

import sqlalchemy
from kotti.events import ObjectInsert, ObjectUpdate, subscribe
from kotti.resources import Content
from kotti.util import Link, LinkParent, LinkRenderer
from sqlalchemy import Column, ForeignKey
from zope.interface import implements

from sverbois_directory import _
from sverbois_directory.interfaces import IBasicWorkflow, IInheritWorkflow


class Person(Content):
    """A person in a directory"""

    implements(IInheritWorkflow)

    id = Column(sqlalchemy.Integer, ForeignKey('contents.id'), primary_key=True)
    firstname = Column(sqlalchemy.Unicode(128))
    lastname = Column(sqlalchemy.Unicode(128))
    birthday = Column(sqlalchemy.Date())
    diver = Column(
        sqlalchemy.Boolean(),
        info={'colanderalchemy': {'edit_permission': 'manage'}})

    type_info = Content.type_info.copy(
        name=u'Person',
        title=_(u'Person'),
        add_view=u'add_person',
        addable_to=[u'Directory'],
        edit_links=[
            Link('edit', title=_(u'Edit')),
            Link('delete', title=_(u'Delete'))
        ],
    )

    def __init__(self, firstname=None, lastname=None, birthday=None, **kwargs):
        super(Person, self).__init__(**kwargs)

        self.firstname = firstname
        self.lastname = lastname
        self.birthday = birthday

    @property
    def fullname(self):
        return self.firstname + u' ' + self.lastname


@subscribe(ObjectInsert, Person)
@subscribe(ObjectUpdate, Person)
def person_handler(event):
    person = event.object
    person.title = person.fullname
    person.owner = None
    person.in_navigation = False


class Directory(Content):
    """A directory of people"""

    implements(IBasicWorkflow)

    id = Column(sqlalchemy.Integer, ForeignKey('contents.id'), primary_key=True)

    type_info = Content.type_info.copy(
        name=u'Directory',
        title=_(u'Directory'),
        add_view=u'add_directory',
        addable_to=[u'Document'],
    )
