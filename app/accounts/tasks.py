from celery import shared_task
from django.core.mail import send_mail
from django.urls import reverse


@shared_task
def send_contact_us_email(form_data):
    message = f'''
            Email from: {form_data["contact_to_email"]}
            Name: {form_data["full_name"]}

            Message: {form_data["message"]}
            '''
    sender = 'fenderoksp@gmail.com'
    send_mail(
        'Contact Us',
        message,
        sender,
        [sender],
        fail_silently=False,
    )


@shared_task
def send_activate_account_email(username, token):
    link = reverse('activate', args=(username, token))
    message = f"""
        Your activation http://127.0.0.1:8000{link}
    """  # TODO
    sender = 'fenderoksp@gmail.com'  # TODO

    send_mail(
        'Activate Your Account',
        message,
        sender,
        [sender],
        fail_silently=False,
    )


@shared_task
def debug():
    debug_message = ('DEBUG ' * 10)
    return debug_message
