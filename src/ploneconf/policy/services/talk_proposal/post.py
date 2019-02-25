# -*- coding: utf-8 -*-
from datauri import DataURI
from plone import api
from plone.i18n.normalizer.interfaces import IIDNormalizer
from plone.namedfile.file import NamedBlobImage
from plone.registry.interfaces import IRegistry
from plone.restapi.deserializer import json_body
from plone.restapi.services import Service
from plone.restapi.services.content.utils import add
from plone.restapi.services.content.utils import create
from ploneconf.policy.content.person import IPerson
from ploneconf.policy.content.talk import ITalk
from Products.CMFPlone.interfaces.controlpanel import IMailSchema
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.MailHost.interfaces import IMailHost
from z3c.relationfield import RelationValue
from zExceptions import BadRequest
from zExceptions import Unauthorized
from zope.component import getUtility
from zope.event import notify
from zope.interface import alsoProvides
from zope.intid.interfaces import IIntIds
from zope.lifecycleevent import ObjectCreatedEvent
from zope.schema import getFields

import plone.protect.interfaces


class TalkProposalPost(Service):
    """Creates a new talk proposal.
    """

    def reply(self):
        data = json_body(self.request)
        # Disable CSRF protection
        if 'IDisableCSRFProtection' in dir(plone.protect.interfaces):
            alsoProvides(
                self.request, plone.protect.interfaces.IDisableCSRFProtection
            )
        speaker = self.create_speaker(data)
        if isinstance(speaker, dict):
            # error occurred
            return speaker
        talk = self.create_talk(data=data, speaker=speaker)
        if isinstance(talk, dict):
            # error occurred
            return talk
        self.send_mail(data=data, speaker=speaker, talk=talk)
        self.request.response.setStatus(204)

    def create_talk(self, data, speaker):
        if 'talks' not in self.context.keys():
            raise Exception(
                'Unable to create a talk proposal. '
                'Folder "talks" not available.'
            )
        title = data.get('title', None)
        container = self.context['talks']
        talk = self.create_obj(
            data=data, type_='Talk', title=title, container=container
        )
        talk_fields = getFields(ITalk)
        for k, v in data.items():
            if k in talk_fields.keys():
                setattr(talk, k, v)
        intids = getUtility(IIntIds)
        to_id = intids.getId(speaker)
        talk.related_people = [RelationValue(to_id)]
        notify(ObjectCreatedEvent(talk))
        talk = add(container, talk, rename=False)
        return talk

    def create_speaker(self, data):
        if 'people' not in self.context.keys():
            raise Exception(
                'Unable to create a talk proposal. '
                'Folder "people" not available.'
            )
        title = data.get('name', None)
        container = self.context['people']
        speaker = self.create_obj(
            data=data, type_='Person', title=title, container=container
        )
        if isinstance(speaker, dict):
            # error occurred
            return speaker
        speaker_fields = getFields(IPerson)
        for k, v in data.items():
            if k == 'title':
                # skip, we use name as title
                continue
            if k in speaker_fields.keys():
                setattr(speaker, k, v)

        image = self.get_speaker_image(data)
        if image:
            speaker.image = image
        notify(ObjectCreatedEvent(speaker))
        speaker = add(container, speaker, rename=False)
        return speaker

    def get_speaker_image(self, data):
        image_b64 = data.get('image', None)
        if not image_b64:
            return None
        image = DataURI(image_b64)
        return NamedBlobImage(
            data=image.data, filename=image.name, contentType=image.mimetype
        )

    def create_obj(self, data, type_, title, container=None):
        if not container:
            container = self.context
        normalizer = getUtility(IIDNormalizer)
        id_ = normalizer.normalize(title)

        try:
            obj = create(container, type_=type_, id_=id_, title=title)
        except Unauthorized as exc:
            self.request.response.setStatus(403)
            return dict(error=dict(type='Forbidden', message=str(exc)))
        except BadRequest as exc:
            self.request.response.setStatus(400)
            return dict(error=dict(type='Bad Request', message=str(exc)))
        return obj

    def send_mail(self, data, speaker, talk):
        mail_template = ViewPageTemplateFile('notify_mail_template.pt')

        registry = getUtility(IRegistry)
        mail_settings = registry.forInterface(IMailSchema, prefix='plone')
        from_address = mail_settings.email_from_address
        email_charset = mail_settings.email_charset
        site = api.portal.get()
        host = getUtility(IMailHost)

        # Cook from template
        message = mail_template(
            self,
            send_to_address=from_address,
            send_from_address=from_address,
            data=data,
            speaker=speaker,
            talk=talk,
        )

        message = message.encode(email_charset)
        host.send(
            message,
            mto=from_address,
            mfrom=from_address,
            subject='{0} - New talk submission'.format(site.title),
            charset='utf-8',
        )
