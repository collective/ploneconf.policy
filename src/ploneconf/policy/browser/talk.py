from Products.Five import BrowserView


class View(BrowserView):
    def get_speakers(self):
        if not self.context.related_people:
            return []
        return [
            x.to_object for x in self.context.related_people if x.to_object
        ]
