# -*- coding: utf-8 -*-
from plone.restapi.controlpanels import RegistryConfigletPanel
from plone.restapi.services import Service
from plone.restapi.types import utils
from ploneconf.policy import _
from Products.CMFPlone.browser.interfaces import IContactForm
from zope.component import adapter
from zope.interface import implementer
from zope.interface import implementer, Interface, Attribute
from zope.publisher.interfaces import IPublishTraverse


@implementer(IPublishTraverse)
class ContactFormGet(Service):
    def __init__(self, context, request):
        super(ContactFormGet, self).__init__(context, request)

    def reply(self):
        form = self.serialize_form()
        if form is None:
            self.request.response.setStatus(404)
            return
        self.content_type = "application/json+schema"
        return form

    def get_jsonschema(self):
        return {
            "fieldsets": [
                {
                    "fields": ["name", "from", "subject", "message"],
                    "id": "default",
                    "title": "Default",
                }
            ],
            "properties": {
                "message": {
                    "description": "Please enter the message you want to send.",
                    "minLength": 0,
                    "title": "Message",
                    "type": "string",
                    "widget": "textarea",
                },
                "from": {
                    "description": "Please enter your e-mail address.",
                    "title": "From",
                    "type": "string",
                },
                "name": {
                    "description": "Please enter your full name.",
                    "title": "Name",
                    "type": "string",
                },
                "subject": {
                    "description": "",
                    "title": "Subject",
                    "type": "string",
                },
            },
            "required": ["name", "from", "subject"],
            "type": "object",
        }

    def serialize_form(self):
        json_schema = self.get_jsonschema()
        json_data = {}

        # JSON schema
        return {
            '@id': '{}/contact-form'.format(self.context.portal_url()),
            'title': _('Contact form'),
            'schema': json_schema,
            'data': json_data,
        }
