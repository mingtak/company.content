from five import grok
from plone.directives import dexterity
from zope.interface import Interface
from plone.app.contenttypes.interfaces import IDocument, INewsItem, IEvent
from company.content import MessageFactory as _


grok.templatedir('content_type_view_template')


class Content_Type_View(dexterity.DisplayForm):
    grok.context(Interface)
    grok.require('zope2.View')
    grok.name('content_type_view')
