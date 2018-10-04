import stripe

from .. import models, utils


def sync_products():
    """
    Synchronizes all products from the Stripe API
    """
    products = stripe.Product.auto_paging_iter()
    for product in products:
        sync_product(product)


def sync_product(product, event=None):
    """
    Synchronizes a product from the Stripe API

    Args:
        product: data from Stripe API representing a product
        event: the event associated with the product
    """

    defaults = {
        'name': product['name'],
        'statement_descriptor': product['statement_descriptor'] or '',
        'metadata': product['metadata']
    }

    obj, created = models.Product.objects.get_or_create(
        stripe_id=product['id'],
        defaults=defaults
    )
    utils.update_with_defaults(obj, defaults, created)
