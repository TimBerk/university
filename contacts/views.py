from django.shortcuts import render, redirect

from django.urls import reverse
from django.views.generic import FormView

from django.contrib import messages
from django.core.mail import BadHeaderError

from university.commands.EmailCommand import EmailCommand

from contacts.forms import EmailForm


class EmailView(FormView):
    form_class = EmailForm
    template_name = 'contacts/email.html'

    def get_success_url(self):
        return reverse('courses:index')

    def form_valid(self, form):
        clean_data = form.cleaned_data
        subject = clean_data.get('subject', '')
        message = clean_data.get('text', '')
        from_email = clean_data.get('email', '')

        if subject and message and from_email:
            email = {
                'subject': subject,
            }
            email_context = {
                'subject': subject,
                'message': message,
                'for_admin': False
            }
            email.update({'context': email_context})

            letter = EmailCommand(email=email, to_email=from_email)
            letter.template = 'emails/contacts.html'

            email_context = {
                'subject': subject,
                'message': message,
                'for_admin': True,
                'user_email': from_email
            }
            email.update({'context': email_context})
            letter_admin = EmailCommand(email=email, to_email=from_email, for_admin=True)
            letter_admin.template = 'emails/contacts.html'
            try:
                letter.send()
                letter_admin.send()
                messages.success(self.request, 'Письмо отправлено')
                return redirect(self.get_success_url())
            except BadHeaderError:
                messages.error(self.request, 'Обнаружен неверный заголовок.')
                return redirect(reverse('contacts:index'))
        else:
            messages.warning(self.request, 'Убедитесь, что все поля введены и корректны')
