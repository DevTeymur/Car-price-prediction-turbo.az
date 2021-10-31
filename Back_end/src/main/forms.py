from django import forms
from . models import Contact

class ContactForm(forms.ModelForm):
    name=forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control rounded-0 border-dark border-2',
        'placeholder': 'Your Name',
    }))
    email=forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control rounded-0 border-dark border-2',
        'placeholder': 'Your Email',
    }))
    message=forms.CharField(widget=forms.Textarea(attrs={      #No text field inside forms
        'class': 'form-control rounded-0 border-dark border-2',
        'placeholder': 'Your Message',
        'rows': 7,
    }))  

    class Meta:
        model=Contact
        fields=['name', 'email', 'message']


