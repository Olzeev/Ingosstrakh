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

    
class EditInfoForm(forms.Form):
    class Meta:
        fields = ["second_name", "name", "last_name", "gender", "age", "weight"]

        widgets = {
            "second_name": forms.TextInput(attrs={
                "class": "edit_info_name",
                "placeholder": "Фамилия", 
                "type": "text", 
                "maxlength": "30"
            }),
            "name": forms.TextInput(attrs={
                "class": "edit_info_name", 
                "placeholder": "Имя", 
                "type": "text", 
                "maxlength": "30"
            }),
            "last_name": forms.TextInput(attrs={
                "class": "edit_info_name", 
                "placeholder": "Отчество", 
                "type": "text", 
                "maxlength": "30"
            }), 
            "gender": forms.Select(), 
            "birth_date": forms.DateInput(attrs={
                "class": "edit_info_birth_date"
            }), 
            "weight": forms.NumberInput(attrs={
                "class": "edit_info_weight", 
                "type": "number", 
                "maxlength": 3
            })
        }


class ReportForm(forms.Form):
    class Meta:
        fields = ["pulse", "preassure1", "preassure2"]

        widgets = {
            "pulse": forms.TextInput(attrs={
                "class": "report_pulse_input", 
                "placeholder": "Пульс", 
                "type": "number"
            }), 
            "preassure1": forms.TextInput(attrs={
                "class": "report_preassure_input", 
                "placeholder": "Верхнее", 
                "type": "number"
            }), 
            "preassure2": forms.TextInput(attrs={
                "class": "report_preassure_input", 
                "placeholder": "Нижнее", 
                "type": "number"
            }), 
        }