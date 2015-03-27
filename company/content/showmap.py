from plone.autoform.interfaces import IFormFieldProvider
from plone.dexterity.interfaces import IDexterityContent
from plone.supermodel import model
from zope import schema
from plone.directives import form
from zope.component import adapts
from zope.interface import alsoProvides, implements

from company.content import MessageFactory as _


class IShowMap(model.Schema):
    """
       Marker/Form interface for ShowMap
    """
    form.fieldset(
        'Show Map',
        label=_(u"Show map"),
        fields=['showMap',],
    )

    showMap = schema.Bool(
        title=_(u'Show Map'),
        description=_(u'If want show map, check it, set script code in Profile'),
        default=False,
        required=False,
    )


alsoProvides(IShowMap, IFormFieldProvider)

def context_property(name):
    def getter(self):
        return getattr(self.context, name)
    def setter(self, value):
        setattr(self.context, name, value)
    def deleter(self):
        delattr(self.context, name)
    return property(getter, setter, deleter)


class ShowMap(object):
    """
       Adapter for ShowMap
    """
    implements(IShowMap)
    adapts(IDexterityContent)

    def __init__(self,context):
        self.context = context

    # -*- Your behavior property setters & getters here ... -*-
    showMap = context_property('showMap')
