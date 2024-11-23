from django import forms
from .models import Item




class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['item_name', 'item_description', 'item_price', 'item_image', 'item_full_description']
        labels = {
            "item_name": "Pakkumise nimi",
            "item_description": "Pakkumise lühikirjeldus",
            "item_price": "Pakkumise Hind",
            "item_image": "Pakkumise Pilt",
            "item_full_description": "Pakkumise täiskirjeldus",
        }
        error_messages = {
            "item_name": {
                "required": "Please enter a valid item name.",
                "max_length": "Item name cannot exceed 200 characters.",
            },
            "item_description": {
                "required": "Please enter a valid item description.",
                "max_length": "Item description cannot exceed 200 characters.",
            },
            "item_price": {
                "required": "Please enter a valid price.",
            },
            "item_image": {
                "required": "Please add an image for the item.",
                "invalid_image": "Please add a valid image URL.",
            },
        }
        widgets = {
            "item_full_description": forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }
        