# -*- coding: utf-8 -*-
from plone.dexterity.content import Item
from plone.supermodel import model
from ploneconf.policy.vocabularies import AUDIENCE_TYPES
from ploneconf.policy.vocabularies import LEVEL_TYPES
from ploneconf.policy.vocabularies import PRESENTATION_DURATION_TYPES
from zope import schema
from zope.interface import implementer

from ploneconf.policy import _


class ITalk(model.Schema):
    """ Marker interface and Dexterity Python Schema for Talk
    """

    title = schema.TextLine(
        title=_('Title of talk'), description=u'', required=True
    )
    description = schema.Text(
        title=_('Description of talk'), description=u'', required=True
    )

    duration = schema.Choice(
        title=_('Duration'),
        description=u'',
        required=True,
        source=PRESENTATION_DURATION_TYPES,
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
    schedule_url = schema.TextLine(
        title=_('Schedule url'), description=u'', required=False
    )


@implementer(ITalk)
class Talk(Item):
    """
    """
