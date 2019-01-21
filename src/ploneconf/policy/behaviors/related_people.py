# -*- coding: utf-8 -*-
from plone.app.dexterity import _
from plone.app.z3cform.widget import RelatedItemsFieldWidget
from plone.autoform import directives as form
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from z3c.relationfield.schema import RelationChoice
from z3c.relationfield.schema import RelationList
from zope.interface import provider


@provider(IFormFieldProvider)
class IRelatedPeople(model.Schema):
    """Behavior interface to make a Dexterity type support related people.
    """

    related_people = RelationList(
        title=_(u'Related People'),
        default=[],
        value_type=RelationChoice(
            title=u'Related', vocabulary='plone.app.vocabularies.Catalog'
        ),
        required=False,
    )
    form.widget(
        'related_people',
        RelatedItemsFieldWidget,
        vocabulary='plone.app.vocabularies.Catalog',
        pattern_options={'selectableTypes': ['Person']},
    )
