from django import forms 

class todoform(forms.Form):
    text = forms.CharField(max_length=40, 
        widget=forms.TextInput(
            attrs={'class' : 'form-control', 'placeholder' : 'Enter todo', 'aria-label' : 'Todo', 'aria-describedby' : 'add-btn'}))