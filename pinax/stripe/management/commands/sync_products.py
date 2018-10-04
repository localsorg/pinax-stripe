from django.core.management.base import BaseCommand

from ...actions import products


class Command(BaseCommand):

    help = "Make sure your Stripe account has the products"

    def handle(self, *args, **options):
        products.sync_products()
