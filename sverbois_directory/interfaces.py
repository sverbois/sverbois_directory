# -*- coding: utf-8 -*-

from zope.interface import Interface


class IBasicWorkflow(Interface):
    """Marker interface for content classes that want to use
       a workflow with private/internal/public states."""


class IInheritWorkflow(Interface):
    """Marker interface for objects that want to use
       permissions of their parent."""