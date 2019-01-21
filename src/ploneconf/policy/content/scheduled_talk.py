# -*- coding: utf-8 -*-
from plone.app.z3cform.widget import RelatedItemsFieldWidget
from plone.autoform import directives as form
from plone.dexterity.content import Item
from plone.supermodel import model
from z3c.relationfield.schema import RelationChoice
from zope import schema
from zope.interface import implementer

from ploneconf.policy import _


class IScheduledTalk(model.Schema):
    """ Marker interface and Dexterity Python Schema for Person
    """

    title = schema.TextLine(
        title=_('Title'),
        description=_(
            u'If you don\'t set a title, will be used the talk title.'
        ),
        required=False,
    )

    room = schema.Choice(
        title=_('Room'),
        description=u'',
        required=True,
        vocabulary='ploneconf.vocabularies.Rooms',
    )

    talk = RelationChoice(
        title=u'Related talk',
        vocabulary='plone.app.vocabularies.Catalog',
        required=True,
    )

    form.widget(
        'talk',
        RelatedItemsFieldWidget,
        vocabulary='plone.app.vocabularies.Catalog',
        pattern_options={'selectableTypes': ['Talk'], 'basePath': '/talks'},
    )


@implementer(IScheduledTalk)
class ScheduledTalk(Item):
    """
    """
