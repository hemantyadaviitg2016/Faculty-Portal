from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ("username", "first_name","last_name", "password1", "password2")
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)
        self.fields["username"].label = "Webmail"
        self.fields["first_name"].label = "Firstname"
        self.fields["last_name"].label = "Lastname"
        self.fields["password1"].help_text = ""
        self.fields["username"].help_text = "please exclude @iitg.ernet.in or @iitg.ac.in"
