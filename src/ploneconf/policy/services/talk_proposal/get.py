# -*- coding: utf-8 -*-
from plone.restapi.services import Service
from plone.restapi.types import utils
from ploneconf.policy import _
from ploneconf.policy.services.talk_proposal.interfaces import (
    ITalkProposalSchema,
)
from zope.interface import implementer
from zope.publisher.interfaces import IPublishTraverse


@implementer(IPublishTraverse)
class TalkProposalGet(Service):
    def __init__(self, context, request):
        super(TalkProposalGet, self).__init__(context, request)

    def reply(self):
        form = self.serialize_form()
        if form is None:
            self.request.response.setStatus(404)
            return
        self.content_type = "application/json+schema"
        return form
        # return IJsonCompatible(ISerializeToJson(form)())

    def get_jsonschema_for_talk_proposal(self, schema):
        fieldsets = utils.get_fieldsets(self.context, self.request, schema)
        schema_fieldsets = utils.get_fieldset_infos(fieldsets)
        # Build JSON schema properties
        properties = utils.get_jsonschema_properties(
            self.context, self.request, fieldsets
        )
        properties['image'] = {
            "type": "string",
            "format": "data-url",
            "title": _("Image"),
        }
        # add image before privacy
        schema_fieldsets[0]['fields'].insert(
            len(schema_fieldsets[0]['fields']) - 1, 'image'
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
        schema = ITalkProposalSchema
        json_schema = self.get_jsonschema_for_talk_proposal(schema=schema)
        json_data = {}

        # JSON schema
        return {
            '@id': '{}/talk-proposal'.format(self.context.portal_url()),
            'title': _('Talk proposal'),
            'schema': json_schema,
            'data': json_data,
        }
