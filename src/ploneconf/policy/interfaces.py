# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from zope import schema
from zope.interface import Interface

from ploneconf.policy import _


class IPloneconfPolicyLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class IPloneconfPolicySettings(Interface):
    """
    """

    conference_rooms = schema.List(
        title=_(u'Conference rooms'),
        default=[],
        missing_value=[],
        value_type=schema.TextLine(),
    )
