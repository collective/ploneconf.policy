# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from zope import schema
from zope.interface import Interface
from ploneconf.policy.content.talk import ITalk
from ploneconf.policy import _
from plone.autoform import directives
from plone.schema import Email
from plone.namedfile import field as namedfile


class ITalkProposalSchema(ITalk):
    """
    """

    name = schema.TextLine(
        title=_('Your name'), description=u'', required=True
    )
    email = Email(
        title=_('Email'), description=_(u'Insert your email.'), required=False
    )

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

    # image = namedfile.NamedBlobImage(
    #     title=_(u'label_leadimage', default=u'Lead Image'),
    #     description=u'',
    #     required=False,
    # )

    directives.mode(slides_url='hidden')
    directives.mode(slides_embed='hidden')
    directives.mode(video_embed='hidden')
    directives.mode(room='hidden')
    directives.mode(start='hidden')
    directives.mode(end='hidden')

