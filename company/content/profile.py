from five import grok

from z3c.form import group, field
from zope import schema
from zope.interface import invariant, Invalid, Interface
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from plone.dexterity.content import Container
from plone.directives import dexterity, form
from plone.app.textfield import RichText
from plone.namedfile.field import NamedImage, NamedFile
from plone.namedfile.field import NamedBlobImage, NamedBlobFile
from plone.namedfile.interfaces import IImageScaleTraversable

from z3c.relationfield.schema import RelationList, RelationChoice
from plone.formwidget.contenttree import ObjPathSourceBinder

#from plone.memoize import ram
from plone import api
from plone.indexer import indexer
from plone.app.multilingual.interfaces import ILanguage

from Products.CMFDefault.utils import checkEmailAddress
from Products.CMFDefault.exceptions import EmailAddressInvalid

from company.content import MessageFactory as _


def checkEmail(value):
    try:
        checkEmailAddress(value)
    except EmailAddressInvalid:
        raise Invalid(_(u"Invalid email address."))
    return True


class IProfile(form.Schema, IImageScaleTraversable):
    """
    Profile for company site
    """

    # Basic information fieldset
    form.fieldset(
        'BasicInfo',
        label=_(u"Basic Information"),
        fields=['title', 'description', 'logo'],
        description=_(u"Tabs for product description."),
    )

    title = schema.TextLine(
        title=_(u'Company name'),
        required=True,
    )

    description = schema.Text(
        title=_(u'Company description'),
        required=False,
    )

    logo = NamedBlobImage(
        title=_(u'Logo image'),
        required=False,
    )

    # Contact fieldset
    form.fieldset(
        'Contact',
        label=_(u"Contact"),
        fields=['address', 'phoneNo', 'servicePhone', 'faxNo', 'emailAddr', 'googleMap'],
    )

    address = schema.TextLine(
        title=_(u'Company address'),
        required=False,
    )

    phoneNo = schema.TextLine(
        title=_(u'Phone No.'),
        required=False,
    )

    servicePhone = schema.TextLine(
        title=_(u'Service phone'),
        description=_(u'0800 or other custom service phone number, if have.'),
        required=False,
    )

    faxNo = schema.TextLine(
        title=_(u'Fax No.'),
        required=False,
    )

    emailAddr = schema.TextLine(
        title=_(u'Eamil'),
        required=False,
        constraint=checkEmail,
    )

    googleMap = schema.Text(
        title=_('Google Map'),
        description=_(u'Google map embeded script code'),
        required=False,
    )

    # External Resources
    form.fieldset(
        'External',
        label=_(u"External Resources"),
        fields=['facebook', 'googlePlus', 'twitter', 'linkedin',
                'fbMessage', 'disqus', 'addthis',
                'webAnalyticsCode', 'metaCode'],
    )

    facebook = schema.URI(
        title=_(u'Facebook url'),
        required=False,
    )

    googlePlus = schema.URI(
        title=_(u'Google+ url'),
        required=False,
    )

    twitter = schema.URI(
        title=_(u'Twitter url'),
        required=False,
    )

    linkedin = schema.URI(
        title=_(u'LinkedIn url'),
        required=False,
    )

    fbMessage = schema.Text(
        title=_(u'facebook Massage'),
        required=False,
    )

    disqus = schema.Text(
        title=_(u'Disqus Massage'),
        required=False,
    )

    addthis = schema.Text(
        title=_(u'Addthis share code'),
        required=False,
    )

    webAnalyticsCode = schema.Text(
        title=_(u'Web master code'),
        description=_(u'Google analytics, bin analytics or other script code'),
        required=False
    )

    metaCode = schema.Text(
        title=_(u'Meta code'),
        description=_('Google master or other Verification code, will show in head section'),
        required=False,
    )

    # Other information fieldset
    form.fieldset(
        'Other',
        label=_(u"Other"),
        fields=['usingPrivate', 'privatePolicy', 'copyright',],
    )

    usingPrivate = schema.Bool(
        title=_(u'Show private page'),
        description=_(u'if check, private policy page will show in http://webhostname/language/@@private_page'),
        default=False,
        required=False,
    )

    privatePolicy = RichText(
        title=_(u'Private policy'),
        required=False,
    )

    copyright = RichText(
        title=_(u'Copyright information'),
        required=False,
    )


class Profile(Container):
    grok.implements(IProfile)


class SampleView(grok.View):
    """ sample view class """

    grok.context(IProfile)
    grok.require('zope2.View')
    grok.name('view')


class GetProfile(grok.View):

    grok.context(Interface)
    grok.require('zope2.View')

    def render(self):
        context = self.context
        catalog = self.context.portal_catalog
        try:
            language = ILanguage(context).get_language()
        except:
            self.profile = catalog({'Type':'Profile'})[0]
            return self.profile
        self.profile = catalog({'Type':'Profile','Language':language})[0]
        return self.profile


@indexer(IProfile)
def address_indexer(obj):
    return obj.address
grok.global_adapter(address_indexer, name='address')

@indexer(IProfile)
def phoneNo_indexer(obj):
    return obj.phoneNo 
grok.global_adapter(phoneNo_indexer, name='phoneNo')

@indexer(IProfile)
def servicePhone_indexer(obj):
    return obj.servicePhone
grok.global_adapter(servicePhone_indexer, name='servicePhone')

@indexer(IProfile)
def faxNo_indexer(obj):
    return obj.faxNo
grok.global_adapter(faxNo_indexer, name='faxNo')

@indexer(IProfile)
def emailAddr_indexer(obj):
    return obj.emailAddr
grok.global_adapter(emailAddr_indexer, name='emailAddr')

@indexer(IProfile)
def googleMap_indexer(obj):
    return obj.googleMap
grok.global_adapter(googleMap_indexer, name='googleMap')

@indexer(IProfile)
def facebook_indexer(obj):
    return obj.facebook
grok.global_adapter(facebook_indexer, name='facebook')

@indexer(IProfile)
def googlePlus_indexer(obj):
    return obj.googlePlus
grok.global_adapter(googlePlus_indexer, name='googlePlus')

@indexer(IProfile)
def twitter_indexer(obj):
    return obj.twitter
grok.global_adapter(twitter_indexer, name='twitter')

@indexer(IProfile)
def linkedin_indexer(obj):
    return obj.linkedin
grok.global_adapter(linkedin_indexer, name='linkedin')

@indexer(IProfile)
def fbMessage_indexer(obj):
    return obj.fbMessage
grok.global_adapter(fbMessage_indexer, name='fbMessage')

@indexer(IProfile)
def disqus_indexer(obj):
    return obj.disqus
grok.global_adapter(disqus_indexer, name='disqus')

@indexer(IProfile)
def addthis_indexer(obj):
    return obj.addthis
grok.global_adapter(addthis_indexer, name='addthis')

@indexer(IProfile)
def webAnalyticsCode_indexer(obj):
    return obj.webAnalyticsCode
grok.global_adapter(webAnalyticsCode_indexer, name='webAnalyticsCode')

@indexer(IProfile)
def metaCode_indexer(obj):
    return obj.metaCode
grok.global_adapter(metaCode_indexer, name='metaCode')

@indexer(IProfile)
def usingPrivate_indexer(obj):
    return obj.usingPrivate
grok.global_adapter(usingPrivate_indexer, name='usingPrivate')

@indexer(IProfile)
def privatePolicy_indexer(obj):
    return obj.privatePolicy.raw
grok.global_adapter(privatePolicy_indexer, name='privatePolicy')

@indexer(IProfile)
def copyright_indexer(obj):
    return obj.copyright.raw
grok.global_adapter(copyright_indexer, name='copyright')
