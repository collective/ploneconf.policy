# -*- coding: utf-8 -*-
from plone.app.event.base import default_timezone
from plone.app.z3cform.widget import DatetimeFieldWidget
from plone.autoform import directives
from plone.dexterity.content import Item
from plone.supermodel import model
from ploneconf.policy.vocabularies import AUDIENCE_TYPES
from ploneconf.policy.vocabularies import LEVEL_TYPES
from ploneconf.policy.vocabularies import PRESENTATION_DURATION_TYPES
from ploneconf.policy.vocabularies import TALK_TOPICS
from z3c.form.browser.checkbox import CheckBoxFieldWidget
from zope import schema
from zope.interface import implementer

from ploneconf.policy import _


class ITalk(model.Schema):
    """ Marker interface and Dexterity Python Schema for Talk
    """

    title = schema.TextLine(
        title=_('Talk'), description=u'Title of talk.', required=True
    )
    description = schema.Text(
        title=_('Description'),
        description=u'Please provide a description of your talk. This text '
        u'will be shown in talks overview and details, so try to arouse '
        u'curiosity of attendants.',
        required=True,
    )

    duration = schema.Choice(
        title=_('Duration'),
        description=u'Choose the talk length. Short will be 20 minutes and '
        u'Long will be 40 minutes. Remember that a short talk doesn\'t mean '
        u'it\'s a worst talk.',
        required=True,
        source=PRESENTATION_DURATION_TYPES,
    )

    level = schema.Choice(
        title=_('Level'),
        description=u'What should be the technical level needed to understand'
        u'this talk? This is useful for people to choose what talks to attend '
        u'or not based on their skills.',
        required=True,
        source=LEVEL_TYPES,
    )
    audience = schema.List(
        title=_('Audience'),
        description=u'What kind of people should be interested listening this'
        u' talk?',
        required=True,
        value_type=schema.Choice(source=AUDIENCE_TYPES),
    )
    topic = schema.List(
        title=_('Topic'),
        description=u'Choose one or more topics related to your talk.'
        u'This will help us to create a better talks schedule.',
        required=True,
        value_type=schema.Choice(source=TALK_TOPICS),
    )
    directives.widget('topic', CheckBoxFieldWidget)

    other_topics = schema.TextLine(
        title=_('Other topics'),
        description=_(
            u'If you selected "Other", please insert your topics here.'
        ),
        required=False,
    )
    slides_url = schema.TextLine(
        title=_('Slides'), description=_(u'Url of slides.'), required=False
    )
    slides_embed = schema.Text(
        title=_('Embed code for slides'), description=u'', required=False
    )

    video_embed = schema.Text(
        title=_('Video embed code'),
        description=_('Embed code for video recording.'),
        required=False,
    )

    room = schema.Choice(
        title=_('Room'),
        description=u'',
        required=False,
        vocabulary='ploneconf.vocabularies.Rooms',
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

    is_keynote = schema.Bool(title=u'Is keynote', required=False)


@implementer(ITalk)
class Talk(Item):
    """
    """
