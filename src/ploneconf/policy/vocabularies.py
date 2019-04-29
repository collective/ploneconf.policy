# -*- coding: utf-8 -*-
from datetime import timedelta
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

TALK_TOPICS = SimpleVocabulary(
    [
        SimpleTerm(value=u'Plone', title=u'Plone'),
        SimpleTerm(value=u'Pyramid', title=u'Pyramid'),
        SimpleTerm(value=u'Guillotina', title=u'Guillotina'),
        SimpleTerm(value=u'Volto', title=u'Volto'),
        SimpleTerm(value=u'use-case', title=u'Use case'),
        SimpleTerm(value=u'Python', title=u'Python'),
        SimpleTerm(value=u'Frontend', title=u'Frontend'),
        SimpleTerm(value=u'Javascript', title=u'Javascript'),
        SimpleTerm(value=u'Design', title=u'Design'),
        SimpleTerm(value=u'db', title=u'Database'),
        SimpleTerm(value=u'Mobile', title=u'Mobile'),
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


class AvailablSlotsBase(object):
    def get_slots_by_delta(self, start, end, delta):
        i = 0
        terms = [
            SimpleTerm(
                value='',
                token='-- select a value --',
                title='-- select a value --',
            )
        ]
        while start < end:
            new_start = start + timedelta(minutes=(delta))
            terms.append(
                SimpleTerm(
                    value='{0}|{1}'.format(
                        start.isoformat(), new_start.isoformat()
                    ),
                    token='{0}|{1}'.format(
                        start.isoformat(), new_start.isoformat()
                    ),
                    title='{0} - {1}'.format(
                        start.strftime('%H:%M'), new_start.strftime('%H:%M')
                    ),
                )
            )
            start = new_start
            i += 1
        return terms


@implementer(IVocabularyFactory)
class AvailableShortSlots(AvailablSlotsBase):
    """
    """

    def __call__(self, context):
        terms = self.get_slots_by_delta(
            start=context.start, end=context.end, delta=20
        )
        return SimpleVocabulary(terms)


AvailableShortSlotsVocabulary = AvailableShortSlots()


@implementer(IVocabularyFactory)
class AvailableLongSlots(AvailablSlotsBase):
    """
    """

    def __call__(self, context):
        terms = self.get_slots_by_delta(
            start=context.start, end=context.end, delta=40
        )
        return SimpleVocabulary(terms)


AvailableLongSlotsVocabulary = AvailableLongSlots()


@implementer(IVocabularyFactory)
class UnscheduledTalks(object):
    """
    """

    def __call__(self, context):
        talks = api.content.find(portal_type='Talk', start=0)
        terms = [self.getTalkTerm(brain) for brain in talks]
        return SimpleVocabulary(terms)

    def getTalkTerm(self, brain):
        talk = brain.getObject()
        speakers = [
            x.to_object.Title() for x in getattr(talk, 'related_people')
        ]
        title = '{title} ({speaker})'.format(
            title=talk.title, speaker=', '.join(speakers)
        )
        return SimpleTerm(title=title, value=brain.UID, token=brain.UID)


UnscheduledTalksVocabulary = UnscheduledTalks()
