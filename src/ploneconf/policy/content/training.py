# -*- coding: utf-8 -*-
# from plone.app.textfield import RichText
from plone.autoform import directives

# from plone.namedfile import field as namedfile
# from plone.supermodel.directives import fieldset
# from z3c.form.browser.radio import RadioFieldWidget
from zope import schema
from plone.dexterity.content import Item
from plone.supermodel import model
from zope.interface import implementer
from ploneconf.policy.vocabularies import TRAINING_CLASS_DURATION_TYPES
from ploneconf.policy.vocabularies import LEVEL_TYPES
from ploneconf.policy.vocabularies import AUDIENCE_TYPES
from ploneconf.policy import _


class ITraining(model.Schema):
    """ Marker interface and Dexterity Python Schema for Training
    """

    duration = schema.Choice(
        title=_('Duration'),
        description=u'',
        required=True,
        source=TRAINING_CLASS_DURATION_TYPES,
    )

    level = schema.Choice(
        title=_('Duration'), description=u'', required=True, source=LEVEL_TYPES
    )
    audience = schema.Set(
        title=_('Audience'),
        description=u'',
        required=True,
        value_type=schema.Choice(source=AUDIENCE_TYPES),
    )


@implementer(ITraining)
class Training(Item):
    """
    """
