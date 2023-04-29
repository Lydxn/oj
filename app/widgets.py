from django import forms
from django.utils.safestring import mark_safe

from martor.widgets import AdminMartorWidget


class CustomAdminMartorWidget(AdminMartorWidget):
    class Media(AdminMartorWidget.Media):
        css = {
            'all': ('css/martor.js',)
        }


class CodeMirrorWidget(forms.Textarea):
    class Media:
        css = {
            'all': ('dist/css/codemirror.css',)
        }
        js = ('dist/js/codemirror.js',)

    def render(self, name, value, attrs=None, renderer=None):
        attrs = attrs or {}
        attrs['class'] = 'codemirror-widget'

        textarea = super().render(name, value, attrs, renderer)

        return mark_safe(textarea)
