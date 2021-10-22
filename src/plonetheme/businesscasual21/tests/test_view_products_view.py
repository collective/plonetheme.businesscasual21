# -*- coding: utf-8 -*-
import unittest

from plone import api
from plone.app.testing import TEST_USER_ID, setRoles
from zope.component import getMultiAdapter
from zope.component.interfaces import ComponentLookupError

from plonetheme.businesscasual21.testing import (
    PLONETHEME_BUSINESSCASUAL21_FUNCTIONAL_TESTING,
    PLONETHEME_BUSINESSCASUAL21_INTEGRATION_TESTING,
)


class ViewsIntegrationTest(unittest.TestCase):

    layer = PLONETHEME_BUSINESSCASUAL21_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        api.content.create(self.portal, "Folder", "other-folder")
        api.content.create(self.portal, "Collection", "products")

    def test_products_view_is_registered(self):
        view = getMultiAdapter(
            (self.portal["products"], self.portal.REQUEST), name="products-view"
        )
        self.assertTrue(view.__name__ == "products-view")
        # self.assertTrue(
        #     'Sample View' in view(),
        #     'Sample View is not found in products-view'
        # )

    def test_products_view_not_matching_interface(self):
        with self.assertRaises(ComponentLookupError):
            getMultiAdapter(
                (self.portal["other-folder"], self.portal.REQUEST), name="products-view"
            )


class ViewsFunctionalTest(unittest.TestCase):

    layer = PLONETHEME_BUSINESSCASUAL21_FUNCTIONAL_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
