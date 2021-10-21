# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import (
    PLONE_FIXTURE,
    FunctionalTesting,
    IntegrationTesting,
    PloneSandboxLayer,
    applyProfile,
)
from plone.testing import z2

import plonetheme.businesscasual21


class PlonethemeBusinesscasual21Layer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.app.dexterity

        self.loadZCML(package=plone.app.dexterity)
        import plone.restapi

        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=plonetheme.businesscasual21)

    def setUpPloneSite(self, portal):
        applyProfile(portal, "plonetheme.businesscasual21:default")


PLONETHEME_BUSINESSCASUAL21_FIXTURE = PlonethemeBusinesscasual21Layer()


PLONETHEME_BUSINESSCASUAL21_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PLONETHEME_BUSINESSCASUAL21_FIXTURE,),
    name="PlonethemeBusinesscasual21Layer:IntegrationTesting",
)


PLONETHEME_BUSINESSCASUAL21_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(PLONETHEME_BUSINESSCASUAL21_FIXTURE,),
    name="PlonethemeBusinesscasual21Layer:FunctionalTesting",
)


PLONETHEME_BUSINESSCASUAL21_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        PLONETHEME_BUSINESSCASUAL21_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name="PlonethemeBusinesscasual21Layer:AcceptanceTesting",
)
