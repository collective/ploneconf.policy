# -*- coding: utf-8 -*-

from Products.Five import BrowserView
from plone import api


class View(BrowserView):
    """
    Returns a list of all talks in the website
    """

    def talks(self):
        return api.content.find(portal_type="Talk", sort_on="sortable_title")

    def get_speakers(self, talk):
        if not talk.related_people:
            return []
        return [x.to_object for x in talk.related_people if x.to_object]
