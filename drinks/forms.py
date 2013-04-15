from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from drinks.models import Profile
from django.db import transaction


class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).count():
            raise forms.ValidationError(u'Email addresses must be unique.')
        return email 
    
    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        
        if commit:
            with transaction.commit_on_success():
                user.save()
                profile = Profile(user=user)
                profile.save()
        else:
            raise NotImplementedError("Can not create user with profile without commit")
        return user