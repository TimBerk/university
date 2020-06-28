from datetime import datetime

import django_rq

from django.shortcuts import redirect

from django.urls import reverse
from django.views.generic import FormView

from django.contrib import messages

from university.helpers.EmailHelper import EmailHelper

from contacts.forms import EmailForm
from contacts.tasks import send_email_job


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

            letter = EmailHelper(email=email, to_email=from_email, template='emails/contacts.html')
            letter = letter.email_content()

            email_context = {
                'subject': subject,
                'message': message,
                'for_admin': True,
                'user_email': from_email
            }
            email.update({'context': email_context})

            letter_admin = EmailHelper(email=email, to_email=from_email, for_admin=True,
                                       template='emails/contacts.html')
            letter_admin = letter_admin.email_content()

            scheduler = django_rq.get_scheduler('default')
            scheduler.enqueue_at(datetime.utcnow(), func=send_email_job, email=letter)
            scheduler.enqueue_at(datetime.utcnow(), func=send_email_job, email=letter_admin)

            messages.success(self.request, 'Письмо отправлено')
            return redirect(self.get_success_url())
        else:
            messages.warning(self.request, 'Убедитесь, что все поля введены и корректны')

        return super().form_valid(form)
