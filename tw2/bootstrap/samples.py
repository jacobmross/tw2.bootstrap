"""
Here you can create samples of your widgets by providing default parameters,
inserting them in a container widget, mixing them with other widgets, etc...
These samples will appear in the WidgetBrowser

See http://toscawidgets.org/documentation/WidgetBrowser for more information
"""

import tw2.core as twc
from tw2.forms.samples import DemoChildren

import tw2.bootstrap.widgets as twb


class DemoHorizontalForm(twb.HorizontalForm):
    legend = 'Hi, I\'m form!'
    title = twb.TextField(validator=twc.Required)

    label = twb.LabelField(value="I am a LabelField")

    class link_to(twb.LinkField):
        label = "For more information"
        link = "http://twitter.github.com/bootstrap/base-css.html#$"
        text = "Twitter Bootstrap CSS $"

    # TODO -- uncomment this once we've got twb.SingleSelectField
    #priority = SingleSelectField(options=['', 'Normal', 'High'])
    space = twb.Spacer
    description = twb.TextArea
    buttons = [twb.SubmitButton, twb.ResetButton]

    def generate_output(self, displays_on):
        """ We override this method *only* to forcefully invalidate the widget
        for the demo.  We just want to show want the CSS looks like for a form
        with an error in the input.
        """

        if hasattr(self, '_validated'):
            return super(DemoHorizontalForm, self).generate_output(displays_on)

        try:
            DemoHorizontalForm.validate(dict(
                #title="This is absent, and therefore fails."
                link_to="forms",
                label="I am a LabelField",
                description="A description could go here...",
            ))
        except twc.ValidationError, e:
            return e.widget.display()


class DemoButton(twb.Button):
    pass


class DemoSubmitButton(twb.SubmitButton):
    pass


class DemoLinkField(twb.LinkField):
    link = "http://twitter.github.com/bootstrap/base-css.html#$"
    text = "Twitter Bootstrap CSS $"
    value = "forms"


class DemoCalendarDatePicker(twb.CalendarDatePicker):
    style = 'component'


class DemoCalendarTimePicker(twb.CalendarTimePicker):
    style = 'dropdown'
    defaultTime = None
    value = "14:00"

