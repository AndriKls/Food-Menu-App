from django import forms
from .models import Item



class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
        labels = {
           "item_name": "Item Name",
            "item_description": "Item Description",
            "item_price": "Item Price",
            "item_image": "Item Image",
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