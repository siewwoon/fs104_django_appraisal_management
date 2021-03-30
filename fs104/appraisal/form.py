from django import forms
from appraisal.models import Appraisal


class EmpForm(forms.ModelForm):
    class Meta:
        model = Appraisal
        fields ="__all__"