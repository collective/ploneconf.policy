# -*- coding: utf-8 -*-
from plone.app.z3cform.widget import RelatedItemsFieldWidget
from plone.autoform import directives as form
from plone.dexterity.content import Container
from plone.supermodel import model
from z3c.relationfield.schema import RelationChoice
from zope import schema
from zope.interface import implementer

from ploneconf.policy import _


class ITimeSlot(model.Schema):
    """ Marker interface and Dexterity Python Schema for Person
    """


@implementer(ITimeSlot)
class TimeSlot(Container):
    """
    """
