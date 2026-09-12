import stripe

from config.settings import STRIPE_API_KEY
from forex_python.converter import CurrencyRates


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


if __name__ == "__main__":
    print(convert_rub_to_usd(86.40))
    donation = create_stripe_price(5)
    print(donation)
    print(create_stripe_session(donation))
