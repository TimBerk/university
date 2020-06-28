from django.core.mail import send_mail
from django_rq import job


@job
def send_email_job(email):
    print('Start email')
    send_mail(
        email['subject'],
        email['plain_message'],
        email['from_email'],
        email['email_to'],
        html_message=email['html_message']
    )
    print('Finish email')
