# -*- coding: utf-8 -*-
from plone.app.textfield import RichText
from plone.dexterity.content import Item
from plone.namedfile import field as namedfile
from plone.supermodel import model
from zope.interface import implementer

from plonetheme.businesscasual21 import _

# from plone.autoform import directives
# from plone.supermodel.directives import fieldset
# from z3c.form.browser.radio import RadioFieldWidget
# from zope import schema


class IProduct(model.Schema):
    """Marker interface and Dexterity Python Schema for Product"""

    # Make sure you import: plone.namedfile.field as namedfile
    photo = namedfile.NamedBlobImage(
        title=_(
            u"Photo",
        ),
        description=_(
            u"",
        ),
        required=False,
    )

    # Make sure to import: from plone.app.textfield import RichText
    text = RichText(
        title=_(
            u"Text",
        ),
        description=_(
            u"",
        ),
        default=u"",
        required=False,
    )


@implementer(IProduct)
class Product(Item):
    """Content-type class for IProduct"""
