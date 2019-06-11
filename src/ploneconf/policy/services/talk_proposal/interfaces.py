# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from zope import schema
from zope.interface import Interface
from ploneconf.policy.content.talk import ITalk
from ploneconf.policy import _
from plone.autoform import directives
from plone.namedfile import field as namedfile


class ITalkProposalSchema(ITalk):
    """
    """

    name = schema.TextLine(
        title=_('Your name'), description=u'', required=True
    )
    email = schema.TextLine(
        title=_('Email'), description=_(u'Insert your email.'), required=True
    )

    bio = schema.Text(title=_('Bio'), description=u'', required=False)

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

    privacy = schema.Bool(
        title=_(u'label_privacy', default=u'Terms and conditions'),
        description=u'We want you to know exactly how our service works and '
        u'why we need your registration details. Please state that you have '
        u'read and agreed to these terms before you continue.',
        required=True,
    )

    directives.mode(slides_url='hidden')
    directives.mode(slides_embed='hidden')
    directives.mode(video_embed='hidden')
    directives.mode(room='hidden')
    directives.mode(start='hidden')
    directives.mode(end='hidden')
