from celery import shared_task
from time import sleep
from django.core.mail import send_mail, EmailMultiAlternatives, send_mass_mail, EmailMessage
from django_celery_beat.models import PeriodicTask, IntervalSchedule

@shared_task
def user_reg_email(username, email):
    send_mail(
        "Welcome to Facebook Clone!",
        f"Hy {username}, Connect with your friends and communities with Facebook Clone Project.",
        "vijaychoudhary@thoughtwin.com",
        [email],
        fail_silently=False
    )
    return 'sent'


@shared_task
def birthday_wishes(key):
    
    

# Create Schedule Every Day at 10 AM
schedule, created = IntervalSchedule.objects.get_or_create(
    every=1,
    period=IntervalSchedule.DAYS,
)

# Schedule the periodic task programmatically
PeriodicTask.objects.get_or_create(
    name='Birthday Wish',
    task='users.tasks.birthday_wishes',
    interval=schedule,
    args=json.dumps(['Happy Birthday']),
)