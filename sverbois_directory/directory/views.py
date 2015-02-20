# -*- coding: utf-8 -*-

import colander
import deform
import uuid
from kotti.util import title_to_name
from kotti.resources import IDocument
from kotti.views.edit import ContentSchema
from kotti.views.form import AddFormView
from kotti.views.form import EditFormView
from pyramid.view import view_config

from sverbois_directory import _
from sverbois_directory.fanstatic import css_and_js
from .resources import Person, Directory


### PERSON ###

@view_config(name='view', context=Person, renderer='templates/person.pt', permission='view')
def person_view(context, request):
    return {}


class PersonSchema(colander.MappingSchema):

    firstname = colander.SchemaNode(
        colander.String(),
        title=_(u"Firstname"))
    lastname = colander.SchemaNode(
        colander.String(),
        title=_(u"Lastname"))
    birthday = colander.SchemaNode(
        colander.Date(),
        missing=None,
        widget=deform.widget.DateInputWidget(),
        title=_(u"birthday"))


@view_config(name=Person.type_info.add_view, context=Directory, permission='add',
             renderer='kotti:templates/edit/node.pt')
class PersonAddForm(AddFormView):
    schema_factory = PersonSchema
    add = Person
    item_type = _(u"Person")

    def find_name(self, appstruct):
        return uuid.uuid4().hex


@view_config(name='edit', context=Person, permission='edit',
             renderer='kotti:templates/edit/node.pt')
class PersonEditForm(EditFormView):
    schema_factory = PersonSchema


### DIRECTORY ###

@view_config(name='view', context=Directory, permission='view',
             renderer='templates/directory.pt')
def directory_view(context, request):
    return {}

class DirectorySchema(ContentSchema):
    pass

@view_config(name=Directory.type_info.add_view, context=IDocument, permission='add',
             renderer='kotti:templates/edit/node.pt')
class DirectoryAddForm(AddFormView):
    schema_factory = DirectorySchema
    add = Directory
    item_type = _(u"Directory")


@view_config(name='edit', context=Directory, permission='edit',
             renderer='kotti:templates/edit/node.pt')
class DirectoryEditForm(EditFormView):
    schema_factory = DirectorySchema
