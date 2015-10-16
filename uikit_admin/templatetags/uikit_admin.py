from django import template
from django.forms.forms import BoundField
from django.utils.html import format_html

register = template.Library()


@register.filter
def uka_form_row_stacked(element, classes=None):
    label = BoundField.label_tag(element, "", {'class': 'uk-form-label'})
    if classes is not None:
        element = element.as_widget(attrs={'class': classes})
    html = format_html('<div class="uk-form-row">{}<div class="uk-form-row">{}</div></div>', label, element)
    return html


@register.filter
def uka_form_row_stacked_button(text, classes=None):
    if classes is None:
        classes = ''
    html = format_html(
        '<div class="uk-form-row"><div class="uk-form-row"><button class="uk-button {}">{}</button></div></div>',
        classes, text)
    return html
