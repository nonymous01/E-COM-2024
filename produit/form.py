from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django import forms

class AuthUser(UserCreationForm):

    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("last_name","first_name","username", "email", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Cet email est déjà utilisé.")
        return email
    def clean_username(self):
        username = self.cleaned_data['username']
        return username

    def __init__(self, *args, **kwargs):
        super(AuthUser, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['placeholder'] = 'Nom utilisateur'
        self.fields['last_name'].widget.attrs['placeholder'] = 'prenom'
        self.fields['first_name'].widget.attrs['first_name'] = 'nom'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['password1'].widget.attrs['placeholder'] = 'Entrez votre mot de passe'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirmez votre mot de passe'
        self.fields['username'].help_text = None
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None