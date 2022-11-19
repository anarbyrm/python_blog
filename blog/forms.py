from django import forms

from .models import Contact


class ContactForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['full_name'].required = True
        self.fields['email'].required = True
        self.fields['subject'].required = True
        self.fields['content'].required = True

    class Meta:
        model = Contact
        exclude = ('sent_at', )
        widgets = {
            'full_name': forms.TextInput(attrs={
                'placeholder': 'Ad Soyad',
                'data-validation-required-message': "Ad və soyadınızı yazın.",
                'class': "form-control",
                'type': "text",
                'id': "name"
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Email',
                'data-validation-required-message': "Email ünvanınızı yazın.",
                'class': "form-control",
                'type': "email",
                'id': "email"
            }),
            'subject': forms.TextInput(attrs={
                'placeholder': 'Mövzu',
                'data-validation-required-message': "Mövzunu qeyd edin.",
                'class': "form-control",
                'type': "text",
                'id': "subject"
            }),
            'content': forms.Textarea(attrs={
                'placeholder': 'Mesajınız...',
                'data-validation-required-message': "Mesaj bölməsi boş ola bilməz.",
                'class': "form-control",
                'row': 8,
                'id': "message"
            }),
        }



