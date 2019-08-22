from django import forms
from django.conf import settings
from course.core.mail import send_mail_template


class ContactEad(forms.Form):

    name = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail')
    message = forms.CharField(label='Mensagem', widget=forms.Textarea)

    def send_email(self, ead):
        subject = 'Contato sobre o curso %s ' % ead.name
        context = {
            'name': self.cleaned_data['name'],
            'email': self.cleaned_data['email'],
            'message': self.cleaned_data['message'],
        }

        send_mail_template(subject, 'ead/contact_email.html', context, [settings.CONTACT_EMAIL],
                           settings.DEFAULT_FROM_EMAIL)