# -*- coding: utf-8 -*-
# from plone.app.textfield import RichText
from plone.autoform import directives
from plone.schema import Email

# from plone.namedfile import field as namedfile
# from plone.supermodel.directives import fieldset
# from z3c.form.browser.radio import RadioFieldWidget
from zope import schema
from plone.app.textfield import RichText as RichTextField
from plone.app.z3cform.widget import RichTextFieldWidget
from plone.dexterity.content import Item
from plone.supermodel import model
from zope.interface import implementer

from ploneconf.policy import _


class IPerson(model.Schema):
    """ Marker interface and Dexterity Python Schema for Person
    """

    # bio = RichTextField(title=_(u'Bio'), description=u'', required=False)
    # directives.widget('bio', RichTextFieldWidget)
    title = schema.TextLine(title=_('Name'), description=u'', required=True)
    bio = schema.Text(title=_('Bio'), description=u'', required=True)

    twitter = schema.TextLine(
        title=_('Twitter account'),
        description=_(u'Insert your Twitter account name.'),
        required=False,
    )

    github = schema.TextLine(
        title=_('Github account'),
        description=_(u'Insert your Github account name.'),
        required=False,
    )
    email = Email(
        title=_('Email'), description=_(u'Insert your email.'), required=False
    )


@implementer(IPerson)
class Person(Item):
    """
    """
