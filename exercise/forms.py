from django import forms


class CppForm(forms.Form):
    cpp = forms.CharField(widget=forms.Textarea)
