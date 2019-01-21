# -*- coding: utf-8 -*-
from plone.app.content.interfaces import INameFromTitle
from zope.interface import Interface
from zope.component import adapter
from zope.interface import implementer

import logging

logger = logging.getLogger(__name__)


class INameFromTalk(Interface):
    """ Interface to adapt to INameFromTitle """

    pass


@implementer(INameFromTitle)
@adapter(INameFromTalk)
class NameFromTalk(object):
    """ Adapter to INameFromTitle """

    def __init__(self, context):
        self.context = context

    def __new__(cls, context):
        instance = super(NameFromTalk, cls).__new__(cls)
        talk_ref = getattr(context, 'talk', None)

        if talk_ref:
            talk = talk_ref.to_object
            instance.title = getattr(talk, 'title', '')
            if not getattr(context, 'title', ''):
                context.title = getattr(talk, 'title', '')
        return instance
