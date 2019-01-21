# -*- coding: utf-8 -*-
from plone import api
from ploneconf.policy.interfaces import IPloneconfPolicySettings
from zope.interface import implementer
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary

PRESENTATION_DURATION_TYPES = SimpleVocabulary(
    [
        SimpleTerm(value=u'LongTalk', title=u'Long Talk'),
        SimpleTerm(value=u'ShortTalk', title=u'Short Talk'),
        SimpleTerm(value=u'Demo', title=u'Demo'),
    ]
)

TRAINING_CLASS_DURATION_TYPES = SimpleVocabulary(
    [
        SimpleTerm(value=u'HalfDay', title=u'1/2 day'),
        SimpleTerm(value=u'OneDay', title=u'1 day'),
        SimpleTerm(value=u'TwoDay', title=u'2 day'),
    ]
)

LEVEL_TYPES = SimpleVocabulary(
    [
        SimpleTerm(value=u'Beginner', title=u'Beginner'),
        SimpleTerm(value=u'Intermediate', title=u'Intermediate'),
        SimpleTerm(value=u'Expert', title=u'Expert'),
    ]
)

AUDIENCE_TYPES = SimpleVocabulary(
    [
        SimpleTerm(value=u'User', title=u'User'),
        SimpleTerm(value=u'Integrator', title=u'Integrator'),
        SimpleTerm(value=u'Designer', title=u'Designer'),
        SimpleTerm(value=u'Developer', title=u'Developer'),
    ]
)


@implementer(IVocabularyFactory)
class Rooms(object):
    """
    """

    def __call__(self, context):

        terms = [
            SimpleTerm(value=x, token=x, title=x)
            for x in api.portal.get_registry_record(
                'conference_rooms', interface=IPloneconfPolicySettings
            )
        ]

        return SimpleVocabulary(terms)


RoomsVocabulary = Rooms()
