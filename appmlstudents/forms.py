from django import forms

class GradeForm(forms.Form):
    math = forms.FloatField(label="Math")
    english = forms.FloatField(label="English")
    science = forms.FloatField(label="Science")