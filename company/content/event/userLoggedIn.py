from five import grok
from zope.interface import Interface
from plone import api
from Products.PlonePAS.events import UserInitialLoginInEvent, UserLoggedInEvent


@grok.subscribe(UserLoggedInEvent)
def userLoggedIn(event):
    catalog = api.portal.get_tool(name='portal_catalog')
    if 'Contributor' not in api.user.get_roles(user=event.object):
        return
    brain = catalog({'Type':'Profile'})
    if len(brain) > 0:
        return

    portal = api.portal.get()
    with api.env.adopt_roles(['Manager']):
        profile = api.content.create(container=portal,
            type='company.content.profile', id='index_html', title='Welcome')
