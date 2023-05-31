from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import *
from crispy_forms.bootstrap import *
from crispy_forms.layout import Layout, Submit, Reset
from .models import ScamReport, ReportVote


class ScamReportForm(forms.ModelForm):
    class Meta:
        model = ScamReport
        fields = ['your_full_name', 'your_email', 'url', 'report_email', 'report_phone',
                  'category', 'description', 'evidence', 'severity_level',
                  'location_country', 'location_city']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Submit'))


class ScamReportUpdateForm(forms.ModelForm):
    class Meta:
        model = ScamReport
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Submit'))


class ReportVoteForm(forms.ModelForm):
    class Meta:
        model = ReportVote
        fields = ('is_upvote',)