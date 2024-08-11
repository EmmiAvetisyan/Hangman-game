from django import forms

from .models import Book, Address, Author, Country

class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        filds = "__all__"
        labels = {
            "name" : "Your Name",
            "code" : "Your Code"
        }

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        filds = "__all__"
        labels = {
            "street" : "Your street",
            "postal_code" : "Your Postal Code",
            "city" : "Your City"
        }
        
class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        filds = "__all__"
        labels = {
            "first_name" : "Your First Name",
            "last_name" : "Your Last Name",
            "address" : "Your Address"
            }
        
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        filds = "__all__"
        labels = {
            "title" : "Title",
            "rating" : "Rating",
            "author" : "Author",
            "is_bestseller" : "Is Bestseller"
        }