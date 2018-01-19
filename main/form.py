from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField()
    algo = forms.ChoiceField(choices=[(x, x) for x in range(1, 32)])