# -*- coding: utf-8 -*-
from plone.app.event.base import default_timezone
from plone.app.textfield import RichText as RichTextField
from plone.app.z3cform.widget import DatetimeFieldWidget
from plone.app.z3cform.widget import RichTextFieldWidget
from plone.autoform import directives
from plone.dexterity.content import Item
from plone.supermodel import model
from ploneconf.policy import _
from ploneconf.policy.vocabularies import AUDIENCE_TYPES
from ploneconf.policy.vocabularies import LEVEL_TYPES
from ploneconf.policy.vocabularies import TRAINING_CLASS_DURATION_TYPES
from ploneconf.policy.vocabularies import TRAINING_CLASS_ROOMS
from zope import schema
from zope.interface import implementer


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
        title=_('Level'), description=u'', required=True, source=LEVEL_TYPES
    )
    audience = schema.Set(
        title=_('Audience'),
        description=u'',
        required=True,
        value_type=schema.Choice(source=AUDIENCE_TYPES),
    )
    room = schema.Choice(
        title=_('Room'),
        description=u'',
        required=True,
        source=TRAINING_CLASS_ROOMS,
    )
    start = schema.Datetime(title=u'Start', required=False)
    directives.widget(
        'start',
        DatetimeFieldWidget,
        default_timezone=default_timezone,
        klass=u'event_start',
    )

    end = schema.Datetime(title=u'End', required=False)
    directives.widget(
        'end',
        DatetimeFieldWidget,
        default_timezone=default_timezone,
        klass=u'event_end',
    )
    docs_link = schema.TextLine(
        title=_('Documentation link'),
        description=u'Insert a link to an online documentation.',
        required=False,
    )

    what_learn = RichTextField(
        title=_(u'What you will learn'), description=u'', required=False
    )
    directives.widget('what_learn', RichTextFieldWidget)

    prerequisites = RichTextField(
        title=_(u'Prerequisites'), description=u'', required=False
    )
    directives.widget('prerequisites', RichTextFieldWidget)

    things_to_bring = RichTextField(
        title=_(u'Things to bring'), description=u'', required=False
    )
    directives.widget('things_to_bring', RichTextFieldWidget)


@implementer(ITraining)
class Training(Item):
    """
    """
