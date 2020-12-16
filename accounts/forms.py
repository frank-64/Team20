from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.db import transaction
from .models import User, Customer, Helper


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_customer = True
        user.save()

        # Can assign account number etc here
        customer = Customer.objects.create(user=user)
        customer.account_num = 12345678
        customer.sort_code = "09-87-65"
        customer.save()
        return user


class UserInputQrCodeForm(forms.Form):
    code = forms.IntegerField(max_value=999999)


