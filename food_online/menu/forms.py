from django import forms 
from .models import Category,FoodItem
from accounts.validators import allow_only_images_validator
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ("category_name","description")


class FoodItemForm(forms.ModelForm):
    image=forms.ImageField(widget=forms.FileInput(attrs={'class':'btn btn-info w-100'}),required=False,validators=[allow_only_images_validator])
    class Meta:
        model = FoodItem
        fields = ("category","description","food_title","price","image","is_available")

