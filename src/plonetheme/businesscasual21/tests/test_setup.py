# -*- coding: utf-8 -*-
"""Setup tests for this package."""
import unittest

from plone import api
from plone.app.testing import TEST_USER_ID, setRoles

from plonetheme.businesscasual21.testing import (  # noqa: E501
    PLONETHEME_BUSINESSCASUAL21_INTEGRATION_TESTING,
)

try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that plonetheme.businesscasual21 is properly installed."""

    layer = PLONETHEME_BUSINESSCASUAL21_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        if get_installer:
            self.installer = get_installer(self.portal, self.layer["request"])
        else:
            self.installer = api.portal.get_tool("portal_quickinstaller")

    def test_product_installed(self):
        """Test if plonetheme.businesscasual21 is installed."""
        self.assertTrue(
            self.installer.is_product_installed("plonetheme.businesscasual21")
        )

    def test_browserlayer(self):
        """Test that IPlonethemeBusinesscasual21Layer is registered."""
        from plone.browserlayer import utils

        from plonetheme.businesscasual21.interfaces import (
            IPlonethemeBusinesscasual21Layer,
        )

        self.assertIn(IPlonethemeBusinesscasual21Layer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = PLONETHEME_BUSINESSCASUAL21_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        if get_installer:
            self.installer = get_installer(self.portal, self.layer["request"])
        else:
            self.installer = api.portal.get_tool("portal_quickinstaller")
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        self.installer.uninstall_product("plonetheme.businesscasual21")
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if plonetheme.businesscasual21 is cleanly uninstalled."""
        self.assertFalse(
            self.installer.is_product_installed("plonetheme.businesscasual21")
        )

    def test_browserlayer_removed(self):
        """Test that IPlonethemeBusinesscasual21Layer is removed."""
        from plone.browserlayer import utils

        from plonetheme.businesscasual21.interfaces import (
            IPlonethemeBusinesscasual21Layer,
        )

        self.assertNotIn(IPlonethemeBusinesscasual21Layer, utils.registered_layers())
