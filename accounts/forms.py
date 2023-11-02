from django.forms import Form, CharField, PasswordInput, TextInput


class LoginForm(Form):
    username = CharField(label='Username', widget=TextInput(attrs={
        'class': 'form-control',
        'id': "username",
        'placeholder': 'Username',
    }))

    password = CharField(label='Password', widget=TextInput(attrs={
        'class': 'form-control',
        'id': 'password',
        'placeholder': 'Password',
    }))
