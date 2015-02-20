# -*- coding: utf-8 -*-

from __future__ import absolute_import

from fanstatic import Group
from fanstatic import Library
from fanstatic import Resource


library = Library("sverbois_directory", "static")

css = Resource(
    library,
    "styles.css")
js = Resource(
    library,
    "scripts.js")

css_and_js = Group([css, js])
