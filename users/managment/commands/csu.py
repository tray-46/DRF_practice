from django.core.management import BaseCommand, CommandError

from dogs.models import User


class Command(BaseCommand):
    help = "create super user"

    def add_arguments(self, parser):
        parser.add_argument("email", required=True, type=str, help="The email address for account")
        parser.add_argument("username", required=True, type=str, help="The username for the new account")
        parser.add_argument("password", required=True, type=str, help="The password for account")

    def handle(self, *args, **kwargs):
        email = kwargs["email"]
        username = kwargs["username"]
        password = kwargs["password"]

        if User.objects.filter(email=email).exists():
            raise CommandError(f"User with {email} already exists")

        try:
            user = User.objects.create(email=email, username=username)
            user.set_password(password)
            user.save()
            self.stdout.write(self.style.SUCCESS(f"Successfully created user {username}"))
        except Exception as e:
            raise CommandError(f"An error occurred: {e}")

