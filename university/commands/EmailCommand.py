from university.settings import ADMIN_EMAIL, ROBOT_EMAIL

from django.core.mail import send_mail

from django.template.loader import render_to_string
from django.utils.html import strip_tags


class EmailCommand:
    template = "emails/base.html"
    from_email = ROBOT_EMAIL
    admin_email = ADMIN_EMAIL

    def __init__(self, email, to_email, for_admin=False):
        self.to_email = to_email
        self.subject = email.get('subject', '')
        self.context = email.get('context', '')
        self.for_admin = for_admin

    def make_email_body(self, context):
        return render_to_string(self.template, context)

    def send(self):
        html_message = self.make_email_body(self.context)
        plain_message = strip_tags(html_message)
        email_to = [self.to_email] if not self.for_admin else [self.admin_email]

        send_mail(
            self.subject,
            plain_message,
            self.from_email,
            email_to,
            html_message=html_message
        )
