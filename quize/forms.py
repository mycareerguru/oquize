from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password1 = forms.CharField(
        widget = forms.PasswordInput()
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput()
    )
    
    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2:
                return password2
            
        raise forms.ValidationError("Password do not match")
                
                
    def clean_username(self):
        username = self.cleaned_data['username']
        
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        
        raise forms.ValidationError("User already exists")
            

class QuestionForm(forms.Form):
    text = forms.CharField()
    opt1 = forms.CharField()
    opt2 = forms.CharField()
    opt3 = forms.CharField()
    opt4 = forms.CharField()
    ans = forms.CharField()
    tags = forms.CharField(required=False)
    
