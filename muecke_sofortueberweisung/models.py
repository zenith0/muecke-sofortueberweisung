# django imports
from django.conf import settings

# muecke imports
from muecke.cart.utils import get_cart
from muecke.plugins import PaymentMethodProcessor
from muecke.plugins import PM_ORDER_IMMEDIATELY


class SofortUeberweisungPaymentMethodProcessor(PaymentMethodProcessor):
    """
    Provides payment processment with sofortueberweisung.de.
    """
    def process(self):
        return {
            "accepted": True,
            "next_url": "https://www.sofortueberweisung.de/payment/start?user_id=%s&project_id=%s&reason_1=Bestellnummer %s&amount=%s&currency=EUR" % \
                (settings.SOFORTUEBERWEISUNG_USERID, settings.SOFORTUEBERWEISUNG_PROJECT_ID, self.order.number, self.order.price)
        }

    def get_pay_link(self):
        return "https://www.sofortueberweisung.de/payment/start?user_id=%s&project_id=%s&reason_1=Bestellnummer %s&amount=%s&currency=EUR" % \
                (settings.SOFORTUEBERWEISUNG_USERID, settings.SOFORTUEBERWEISUNG_PROJECT_ID, self.order.number, self.order.price)

    def get_create_order_time(self):
        return PM_ORDER_IMMEDIATELY
