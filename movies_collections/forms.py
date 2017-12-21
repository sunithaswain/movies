from django import forms
class SearchingForm(forms.Form):  
    search_text =  forms.CharField(max_length=200)