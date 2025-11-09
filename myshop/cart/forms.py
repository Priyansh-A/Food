from django import forms

class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(
        min_value=1,
        initial=1,
        widget=forms.NumberInput(attrs={
            'class': 'quantity-input compact-orange',
            'min': '1',
            'max': '20',
            'value': '1',
            'style': 'width: 60px; text-align: center; color: orange; margin: 5px 5px;'
        })
    )
    override = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.HiddenInput(attrs={'class': 'override-field'})
    )