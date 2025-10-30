from django import forms

PRODUCT_QUANTITY_CHOICES = [(i , str(i)) for i in range(1,21)]

class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'class': 'quantity-input compact-orange',
            'min': '1',
            'style': 'width: 35px; color:orange; margin:5px;'
        })
    )
    override = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.HiddenInput(attrs={'class': 'override-field'})
    )
    
    