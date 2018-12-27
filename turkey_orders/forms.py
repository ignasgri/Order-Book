from django import forms
from .models import Turkey_Orders
 
class Turkey_Orders_Form(forms.ModelForm):
    class Meta:
        model = Turkey_Orders
        fields = ('name', 'address','phone_number', 'turkey', 't_type'
        , 'weight', 'collection_date', 'staff_initials', 'comments')
