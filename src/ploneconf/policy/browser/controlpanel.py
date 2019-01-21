# -*- coding: utf-8 -*-
from plone.app.registry.browser import controlpanel
from ploneconf.policy import _
from ploneconf.policy.interfaces import IPloneconfPolicySettings


class PloneconfControlpanel(controlpanel.RegistryEditForm):
    schema = IPloneconfPolicySettings
    id = u'PloneconfControlpanel'
    label = _(u'Ploneconf Controlpanel')


class PloneconfControlpanelControlPanel(controlpanel.ControlPanelFormWrapper):
    form = PloneconfControlpanel
