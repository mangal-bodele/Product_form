from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

        widgets = {
            'product_name' : forms.TextInput(attrs={'class': 'form-control'}),
            'product_price' : forms.NumberInput(attrs={'class': 'form-control'}),
            'product_quantity' : forms.NumberInput(attrs={'class': 'form-control'}),
            'delivery_address' : forms.Textarea(attrs={'rows':5, 'class': 'form-control'}),
            'mode': forms.Select(attrs={'class': 'form-control'})
            }