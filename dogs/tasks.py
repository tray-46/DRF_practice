from datetime import datetime

from celery import shared_task

from dogs.services import send_like_email, send_birthday_email


@shared_task
def dog_likes(dog_id):
    send_like_email(dog_id)


@shared_task
def dog_birthday():
    send_birthday_email()