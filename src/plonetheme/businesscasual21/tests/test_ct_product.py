# -*- coding: utf-8 -*-
import unittest

from plone import api
from plone.app.testing import TEST_USER_ID, setRoles
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject, queryUtility

from plonetheme.businesscasual21.content.product import IProduct  # NOQA E501
from plonetheme.businesscasual21.testing import (  # noqa
    PLONETHEME_BUSINESSCASUAL21_INTEGRATION_TESTING,
)


class ProductIntegrationTest(unittest.TestCase):

    layer = PLONETHEME_BUSINESSCASUAL21_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        self.parent = self.portal

    def test_ct_product_schema(self):
        fti = queryUtility(IDexterityFTI, name="Product")
        schema = fti.lookupSchema()
        self.assertEqual(IProduct, schema)

    def test_ct_product_fti(self):
        fti = queryUtility(IDexterityFTI, name="Product")
        self.assertTrue(fti)

    def test_ct_product_factory(self):
        fti = queryUtility(IDexterityFTI, name="Product")
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IProduct.providedBy(obj),
            u"IProduct not provided by {0}!".format(
                obj,
            ),
        )

    def test_ct_product_adding(self):
        setRoles(self.portal, TEST_USER_ID, ["Contributor"])
        obj = api.content.create(
            container=self.portal,
            type="Product",
            id="product",
        )

        self.assertTrue(
            IProduct.providedBy(obj),
            u"IProduct not provided by {0}!".format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn("product", parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn("product", parent.objectIds())

    def test_ct_product_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ["Contributor"])
        fti = queryUtility(IDexterityFTI, name="Product")
        self.assertTrue(
            fti.global_allow, u"{0} is not globally addable!".format(fti.id)
        )
