from django import forms

from app.models import Language, Submission
from app.widgets import CodeMirrorWidget


class SubmissionForm(forms.ModelForm):
    source = forms.CharField(max_length=65536, widget=CodeMirrorWidget, strip=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['language'].queryset = Language.objects.all().order_by('name')
        self.fields['language'].empty_label = None
        self.fields['language'].widget.attrs.update({'class': 'submit-language'})

    class Meta:
        model = Submission
        fields = ('language', 'source')
