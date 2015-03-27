from plone.dexterity.browser.add import DefaultAddForm, DefaultAddView
from plone.dexterity.browser.edit import DefaultEditForm, DefaultEditView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from z3c.form.interfaces import HIDDEN_MODE


class AddForm(DefaultAddForm):
    template = ViewPageTemplateFile('template/addForm.pt')


class AddView(DefaultAddView):
    form = AddForm


class EditForm(DefaultEditForm):
    template = ViewPageTemplateFile('template/editForm.pt')


class EditView(DefaultEditView):
    form = EditForm


class EventAddForm(DefaultAddForm):
    template = ViewPageTemplateFile('template/addForm.pt')

    def updateWidgets(self):
        super(EventAddForm, self).updateWidgets()
        self.widgets['location'].mode = HIDDEN_MODE
        self.widgets['attendees'].mode = HIDDEN_MODE
        self.widgets['contact_email'].mode = HIDDEN_MODE
        self.widgets['event_url'].mode = HIDDEN_MODE


class EventAddView(DefaultAddView):
    form = EventAddForm


class EventEditForm(DefaultEditForm):
    template = ViewPageTemplateFile('template/editForm.pt')

    def updateWidgets(self):
        super(EventEditForm, self).updateWidgets()
        self.widgets['location'].mode = HIDDEN_MODE
        self.widgets['attendees'].mode = HIDDEN_MODE
        self.widgets['contact_email'].mode = HIDDEN_MODE
        self.widgets['event_url'].mode = HIDDEN_MODE

class EventEditView(DefaultEditView):
    form = EventEditForm

