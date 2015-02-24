# -*- coding: utf-8 -*-

import colander
import deform
import uuid
from colanderalchemy import SQLAlchemySchemaNode
from kotti.util import title_to_name
from kotti.resources import IDocument
from kotti.views.edit import ContentSchema
from kotti.views.form import AddFormView
from kotti.views.form import EditFormView
from pyramid.view import view_config

from sverbois_directory import _
from .fanstatic import css_and_js
from .resources import Person, Directory


def check_edit_permission(schema, context, request):
    for child in schema.children:
        if hasattr(child, 'edit_permission'):
            if not request.has_permission(child.edit_permission, context):
                del schema[child.name]
    return schema


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
        title=_(u"Birthday"))
    diver = colander.SchemaNode(
        colander.Boolean(),
        default=False,
        title=_(u"Diver"),
        edit_permission='manage')


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
    def schema_factory(self):
        #schema = PersonSchema()
        schema = SQLAlchemySchemaNode(Person, includes=['firstname', 'lastname', 'birthday', 'diver'])
        return check_edit_permission(schema, self.context, self.request)


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
