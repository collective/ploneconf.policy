# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from ploneconf.policy.testing import PLONECONF_POLICY_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that ploneconf.policy is properly installed."""

    layer = PLONECONF_POLICY_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if ploneconf.policy is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'ploneconf.policy'))

    def test_browserlayer(self):
        """Test that IPloneconfPolicyLayer is registered."""
        from ploneconf.policy.interfaces import (
            IPloneconfPolicyLayer)
        from plone.browserlayer import utils
        self.assertIn(
            IPloneconfPolicyLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = PLONECONF_POLICY_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['ploneconf.policy'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if ploneconf.policy is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'ploneconf.policy'))

    def test_browserlayer_removed(self):
        """Test that IPloneconfPolicyLayer is removed."""
        from ploneconf.policy.interfaces import \
            IPloneconfPolicyLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            IPloneconfPolicyLayer,
            utils.registered_layers())
