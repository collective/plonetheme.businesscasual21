# -*- coding: utf-8 -*-

from plone.app.contenttypes.browser.collection import CollectionView
# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
# from plonetheme.businesscasual21 import _


class ProductsView(CollectionView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('products_view.pt')

    def __call__(self):
        # Implement your own actions:
        return self.index()
