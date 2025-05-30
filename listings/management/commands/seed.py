from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from listings.models import Listing, Booking, Review
from faker import Faker
import random
from datetime import timedelta, date

fake = Faker()

class Command(BaseCommand):
    help = 'Seed the database with sample listings, bookings, and reviews.'

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding data...")

        users = list(User.objects.all())
        if not users:
            for _ in range(5):
                users.append(User.objects.create_user(
                    username=fake.user_name(),
                    email=fake.email(),
                    password='password123'
                ))

        listings = []
        for _ in range(10):
            listing = Listing.objects.create(
                title=fake.sentence(),
                description=fake.paragraph(),
                price_per_night=round(random.uniform(50, 300), 2),
                location=fake.city()
            )
            listings.append(listing)

        for _ in range(20):
            Booking.objects.create(
                listing=random.choice(listings),
                user=random.choice(users),
                start_date=date.today(),
                end_date=date.today() + timedelta(days=random.randint(1, 10))
            )

        for _ in range(10):
            Review.objects.create(
                listing=random.choice(listings),
                user=random.choice(users),
                rating=random.randint(1, 5),
                comment=fake.sentence()
            )

        self.stdout.write(self.style.SUCCESS("Successfully seeded the database."))
