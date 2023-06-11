from django import forms

class LoginForm(forms.Form):
    class Meta:
        fields = ["email", "password"]

        widgets = {
            "email": forms.TextInput(attrs={
                "class": "sign_in_input", 
                "placeholder": "Эл. почта", 
                "type": "email", 
                "maxlength": "30"
            }), 
            "password": forms.TextInput(attrs={
                "class": "password_input",
                "placeholder": "Пароль",
                "type": "password",
                "maxlength": "30",
                "size": "30"
            })
        }

class SignUpForm(forms.Form):
    class Meta:
        fields = ["email", "password", "password_check"]

        widgets = {
            "email": forms.TextInput(attrs={
                "class": "sign_in_input", 
                "placeholder": "Эл. почта", 
                "type": "email", 
                "maxlength": "30"
            }), 
            "password": forms.TextInput(attrs={
                "class": "password_input",
                "placeholder": "Пароль",
                "type": "password",
                "maxlength": "30"
            }), 
            "password_check": forms.TextInput(attrs={
                "class": "password_input",
                "placeholder": "Пароль",
                "type": "password",
                "maxlength": "30"
            })
        }

    #email = forms.EmailField(label='Email', max_length=30)
    #password = forms.CharField(label='Password', max_length=30)
    #password_check = forms.CharField(label='Password', max_length=30)