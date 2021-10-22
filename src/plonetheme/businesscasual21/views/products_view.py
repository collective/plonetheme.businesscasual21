# -*- coding: utf-8 -*-

# from plonetheme.businesscasual21 import _
from Products.Five.browser import BrowserView

# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class ProductsView(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('products_view.pt')

    def __call__(self):
        # Implement your own actions:
        return self.index()
