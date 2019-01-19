# -*- coding: utf-8 -*-
from ploneconf.policy.content.person import IPerson  # NOQA E501
from ploneconf.policy.testing import PLONECONF_POLICY_INTEGRATION_TESTING  # noqa
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest




class PersonIntegrationTest(unittest.TestCase):

    layer = PLONECONF_POLICY_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_ct_person_schema(self):
        fti = queryUtility(IDexterityFTI, name='Person')
        schema = fti.lookupSchema()
        self.assertEqual(IPerson, schema)

    def test_ct_person_fti(self):
        fti = queryUtility(IDexterityFTI, name='Person')
        self.assertTrue(fti)

    def test_ct_person_factory(self):
        fti = queryUtility(IDexterityFTI, name='Person')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IPerson.providedBy(obj),
            u'IPerson not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_person_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='Person',
            id='person',
        )

        self.assertTrue(
            IPerson.providedBy(obj),
            u'IPerson not provided by {0}!'.format(
                obj.id,
            ),
        )

    def test_ct_person_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Person')
        self.assertTrue(
            fti.global_allow,
            u'{0} is not globally addable!'.format(fti.id)
        )
