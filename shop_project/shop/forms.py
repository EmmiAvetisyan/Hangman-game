from django import forms
from .models import Category, Product

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__' 
        labels = {
            "name" : "Name",
        }

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__' 
        labels = {
            "name" : "Your Name",
            "image" : "image",
            "text" : "Text",
            "category" : "Category",
            "stock" : "Stock",
            "price" : "Price"
        } 
