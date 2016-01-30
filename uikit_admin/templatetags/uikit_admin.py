from django import template
from django.forms.forms import BoundField
from django.utils.html import format_html

register = template.Library()


@register.simple_tag
def uka_form_row_stacked(element, errors='', classes=''):
    class_margin_top = ''
    label = BoundField.label_tag(element, "", {'class': 'uk-form-label'})
    if errors:
        classes_tmp = classes + ' uk-form-danger'
        classes = classes_tmp
        class_margin_top = 'uk-margin-top'
    element = element.as_widget(attrs={'class': classes})  # to remove (be done in js)
    html_error = format_html('<div class="uk-text-danger {}">{}</div>', class_margin_top, errors)
    html = format_html(
        '<div class="uk-form-row">{}<div class="uk-form-controls">{}</div>{}</div>', label, element, html_error)
    return html


@register.simple_tag
def uka_form_row_stacked_button(text, classes=None):
    if classes is None:
        classes = ''
    html = format_html(
        '<div class="uk-form-row"><div class="uk-form-controls"><button class="uk-button {}">{}</button></div></div>',
        classes, text)
    return html


@register.simple_tag
def uka_button(text, classes=None, type=None, name=None):
    if classes is None:
        classes = ''
    if type is None:
        type = ''
    if name is None:
        name = ''
    html = format_html(
        '<button class="uk-button {}" type="{}" name="{}">{}</button>',
        classes, type, name, text)
    return html


@register.filter(name='addcss')
def addcss(field, css):
    return field.as_widget(attrs={"class": css})
