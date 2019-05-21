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

    def get_jsonschema(self, schema):
        fieldsets = utils.get_fieldsets(self.context, self.request, schema)
        schema_fieldsets = utils.get_fieldset_infos(fieldsets)
        # Build JSON schema properties
        properties = utils.get_jsonschema_properties(
            self.context, self.request, fieldsets
        )

        # Determine required fields
        required = []
        for field in utils.iter_fields(fieldsets):
            if field.field.required:
                required.append(field.field.getName())

        # Include field modes
        for field in utils.iter_fields(fieldsets):
            if field.mode:
                properties[field.field.getName()]['mode'] = field.mode

        return {
            'type': 'object',
            'properties': properties,
            'required': required,
            'fieldsets': schema_fieldsets,
        }

    def serialize_form(self):
        schema = IContactForm
        json_schema = self.get_jsonschema(schema=schema)
        json_data = {}

        # JSON schema
        return {
            '@id': '{}/contact-form'.format(self.context.portal_url()),
            'title': _('Contact form'),
            'schema': json_schema,
            'data': json_data,
        }
