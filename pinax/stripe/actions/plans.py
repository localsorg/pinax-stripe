import stripe

from .. import models, utils


def sync_plans():
    """
    Synchronizes all plans from the Stripe API
    """
    plans = stripe.Plan.auto_paging_iter()
    for plan in plans:
        sync_plan(plan)


def sync_plan(plan, event=None):
    """
    Synchronizes a plan from the Stripe API

    Args:
        plan: data from Stripe API representing a plan
        event: the event associated with the plan
    """

    product = models.Product.objects.get(stripe_id=plan['product'])

    defaults = {
        'amount': utils.convert_amount_for_db(plan['amount'], plan['currency']),
        'currency': plan['currency'] or '',
        'interval': plan['interval'],
        'interval_count': plan['interval_count'],
        'product': product,
        'trial_period_days': plan['trial_period_days'],
        'metadata': plan['metadata']
    }

    obj, created = models.Plan.objects.get_or_create(
        stripe_id=plan['id'],
        defaults=defaults
    )
    utils.update_with_defaults(obj, defaults, created)
