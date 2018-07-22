from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import validate_email
from .models import Profile
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput


class PlaceholderAuthForm(AuthenticationForm):
    username = forms.CharField(
        label="사용자명",
        widget=forms.TextInput(
            attrs={'class':'validate','placeholder': 'Email'}))
    password = forms.CharField(
        label="비밀번호",
        widget=forms.PasswordInput(
            attrs={'placeholder':'Password'}))

class SignupForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '이메일'}))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': '비밀번호'}))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': '비밀번호확인'}))
    clinicname = forms.CharField(label='병원명')
    
    ROLE_CHOICES = (
        ('W', '원장'),
        ('M', '마케팅담당자'),
        ('S', '병원관계자'),
    )
    role = forms.ChoiceField(label='담당업무', 
                widget=forms.RadioSelect,
                choices=ROLE_CHOICES)

    # class Meta(UserCreationForm.Meta):
    #     fields = UserCreationForm.Meta.fields + ('email',)

    # def clean_username(self):
    #     value = self.cleaned_data.get('username')
    #     if value:
    #         validate_email(value)
    #         return value

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].validators = [validate_email]
        self.fields['username'].help_text = "이메일주소를 입력하세요."
        self.fields['username'].label = '아이디(이메일주소)'

    def save(self):
        user = super().save(commit=False)
        user.email = self.cleaned_data.get('username')
        user.save()
        profile = Profile.objects.create(user=user, role=self.cleaned_data['role'], clinicname=self.cleaned_data['clinicname'])
        return user

    

