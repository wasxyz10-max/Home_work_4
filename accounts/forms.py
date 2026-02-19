from django import forms
from django.contrib.auth.models import User
from .models import Resume
from captcha.fields import CaptchaField

class RegisterForm(forms.ModelForm):
    username = forms.CharField(label="Логин")
    password = forms.CharField(widget=forms.PasswordInput, label="Пароль")
    captcha = CaptchaField(label="Введите текст с картинки")

    class Meta:
        model = Resume
        fields = [
            'full_name', 'age', 'phone', 'email', 'city',
            'education', 'experience', 'skills',
            'desired_position', 'salary_expectation', 'about'
        ]

    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
        )
        user.is_active = True 
        user.save()


        resume = super().save(commit=False)
        resume.user = user
        if commit:
            resume.save()

        return user