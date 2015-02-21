# -*- coding: utf-8 -*-

from pyramid.i18n import TranslationStringFactory
from kotti.security import set_roles, set_sharing_roles, set_user_management_roles
from kotti.security import _DEFAULT_ROLES, Principal

_ = TranslationStringFactory('sverbois_directory')

roles = _DEFAULT_ROLES.copy()
roles.update({
    u'role:webmaster': Principal(name=u'role:webmaster', title=_(u'Webmaster')),
})
set_roles(roles)
set_sharing_roles([u'role:viewer', u'role:editor', u'role:owner', u'role:webmaster'])
set_user_management_roles([u'role:viewer', u'role:editor', u'role:webmaster', u'role:admin'])


def kotti_configure(settings):
    settings['pyramid.includes'] += ' sverbois_directory'
    settings['kotti.fanstatic.view_needed'] += ' sverbois_directory.fanstatic.css_and_js'
    settings['kotti.available_types'] += '  sverbois_directory.resources.Directory sverbois_directory.resources.Person'
    settings['kotti.use_workflow'] = 'sverbois_directory:workflows.zcml'
    settings['kotti.populators'] += ' sverbois_directory.populate.populate'
    settings['kotti.alembic_dirs'] += ' sverbois_directory:alembic'


def includeme(config):
    config.add_translation_dirs('sverbois_directory:locale')
    config.add_static_view('static-sverbois-directory', 'sverbois_directory:static')
    config.scan(__name__)
