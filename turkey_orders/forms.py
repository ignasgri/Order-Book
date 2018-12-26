from django import forms
from .models import Turkey_Orders
 
class Turkey_Orders_Form(forms.ModelForm):
    class Meta:
        model = Turkey_Orders
        fields = ('name', 'address','phone_number', 'create_date', 'collection_date')
