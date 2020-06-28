from django.conf import settings

from django.template.loader import render_to_string
from django.utils.html import strip_tags


class EmailHelper:
    from_email = settings.ROBOT_EMAIL
    admin_email = settings.ADMIN_EMAIL

    def __init__(self, email, to_email, for_admin=False, template='emails/base.html'):
        self.email_to = [to_email] if not for_admin else [self.admin_email]
        self.subject = email.get('subject', '')
        self.context = email.get('context', '')
        self.for_admin = for_admin
        self.template = template
        self.html_message = html_message = self.make_email_body(self.context)
        self.plain_message = strip_tags(html_message)

    def make_email_body(self, context):
        return render_to_string(self.template, context)

    def email_content(self):
        return {
            'subject':self.subject,
            'plain_message':self.plain_message,
            'from_email':self.from_email,
            'email_to':self.email_to,
            'html_message':self.html_message
        }
