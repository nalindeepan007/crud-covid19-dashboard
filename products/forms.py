from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    title             =   forms.CharField(widget=forms.TextInput(attrs={"placeholder":"your title "}))
    description       =   forms.CharField(required=False, widget=forms.Textarea(attrs={
        "class": "new-class-name two",
        "placeholder": "Write description here ",
        "id": "my-id-for-text-area",
        "rows": 10,
        "cols": 50,
    }))
    price             =   forms.DecimalField(initial=5.00)
    summary = forms.CharField(required= False, widget=forms.Textarea(attrs={
        "id": "my-id-for-text-area",
        "class": "new-class-name three",
        "rows": 10,
        "cols": 50,

    }))


    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price',
            'summary'

        ]


class RawProductionForm(forms.Form):
    title             =   forms.CharField(widget=forms.TextInput(attrs={"placeholder":"your title "}))
    description       =   forms.CharField(required=False, widget=forms.Textarea(attrs={
        "class": "new-class-name two",
        "placeholder": "Write description here ",
        "id": "my-id-for-text-area",
        "rows": 10,
        "cols": 50,
    }))
    price             =   forms.DecimalField(initial=5.00)
    summary = forms.CharField(required= False, widget=forms.Textarea(attrs={
        "id": "my-id-for-text-area",
        "class": "new-class-name three",
        "rows": 10,
        "cols": 50,

    }))
