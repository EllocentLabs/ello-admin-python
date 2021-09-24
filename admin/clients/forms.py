from admin.clients.models import Clients
from django import forms


class ClientForm(forms.ModelForm):
    class Meta:
        model = Clients
        exclude = ['emailStatus', 'status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = forms.PasswordInput()
        for key, value in self.fields.items():
            self.fields[key].widget.attrs.update({
                'class': 'form-control',
                "placeholder": f"Enter {value.label}"
            })
        self.fields['username'].widget = forms.HiddenInput()
        self.fields['password'].widget.attrs.update(
            {'data-parsley-minlength': '8', })
        self.fields['personPhone'].widget.attrs.update(
            {'type': 'tel', })
    field_order = ['businessName','businessAddress','businessPhone','personName','personEmail','personPhone','username' ,'plan', 'password']

class ClientUpdate(forms.ModelForm):
    class Meta:
        model = Clients
        exclude = ['password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, value in self.fields.items():
            if key != 'emailStatus' and key != 'status':
                self.fields[key].widget.attrs.update({
                    'class': 'form-control',
                    "placeholder": f"Enter {value.label}"
                })
