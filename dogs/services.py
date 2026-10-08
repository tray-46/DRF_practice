# import os
# import django
#
# # Replace 'your_project_name' with the folder name containing your settings.py
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
# django.setup()

from datetime import datetime

import stripe
from django.core import mail
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from forex_python.converter import CurrencyRates

from config.settings import STRIPE_API_KEY
from dogs.models import Dog

stripe.api_key = STRIPE_API_KEY


def convert_rub_to_usd(amount):
    c = CurrencyRates()
    rate = c.get_rate("RUB", "USD")
    return int(amount * rate)


def create_stripe_price(amount):
    price = stripe.Price.create(
        currency="usd",
        unit_amount=amount * 100,
        product_data={"name": "Donation"},
    )
    return price


def create_stripe_session(price):
    session = stripe.checkout.Session.create(
        success_url="http://127.0.0.1:8000/",
        line_items=[{"price": price.id, "quantity": 1}],
        mode="payment",
    )
    return session.id, session.url


def send_like_email(dog_id):
    dog = get_object_or_404(Dog, pk=dog_id)

    send_mail(
        subject="Your dog was liked",
        message="Your dog was liked",
        from_email="no-reply@localhost",
        recipient_list=[dog.owner.email],
        fail_silently=False,
    )
    print("mail send")


def send_birthday_email():
    dt_now = datetime.now()
    dogs = Dog.objects.filter(owner__isnull=False, date_born__month=dt_now.month, date_born__day=dt_now.day)

    messages = list()
    for dog in dogs:
        meg = mail.EmailMessage(
            f"Happy birthday, {dog.name}!",
            f"Congrats with you {dog.name} BDay!",
            "no-reply@localhost",
            [dog.owner.email],
        )
        messages.append(meg)

    if messages:
        backend = mail.mailers.default
        backend.send_messages(messages)

# def send_telegram_massage(chat_id, message):
#     params = {
#         "chat_id": chat_id,
#         "text": message,
#     }
#     response = requests.get("https://api.telegram.org/bot{}")
#     print(response.json())


if __name__ == "__main__":
    # print(convert_rub_to_usd(86.40))
    # donation = create_stripe_price(5)
    # print(donation)
    # print(create_stripe_session(donation))
    # send_like_email(1)
    # send_birthday_email()
    # send_telegram_massage(587385268, "Hi")
    pass
