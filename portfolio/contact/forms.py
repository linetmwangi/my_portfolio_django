from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'message']

        name = forms.CharField(max_length=100, required=True)
        email = forms.EmailField(required=True)
        phone = forms.CharField(max_length=15, required=False)  # Optional phone number
        message = forms.CharField()

    def clean_message(self):
        message = self.cleaned_data.get('message')
        if len(message) > 100:
            raise forms.ValidationError("Message must be at least 100 characters.")
        return message
