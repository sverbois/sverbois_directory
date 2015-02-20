# -*- coding: utf-8 -*-

from kotti.security import get_principals

def populate_users():

    principals = get_principals()
    if u'sverbois' not in principals:
        principals[u'sverbois'] = {
            'name': u'sverbois',
            'password': u'sverbois',
            'title': u"Sébastien Verbois",
            'email': u'sebastien.verbois@not.here',
            'groups': [u'role:editor'],
        }

def populate_groups():

    principals = get_principals()
    if u'group:readers' not in principals:
        principals[u'group:readers'] = {
            'name': u'group:readers',
            'title': u"Readers",
            'groups': [u'role:viewer'],
        }

def populate():

    populate_users()
    populate_groups()