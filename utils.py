import math

from settings import settings


def cny_to_usd(cny_amount):
    usd_amount = round(cny_amount / settings.USD_CNY, 2)
    return usd_amount


def round_price(usd_amount):
    if usd_amount < 25:
        left = int(usd_amount)
        right = usd_amount % 1
        if right <= 0.25:
            usd_amount = left + 0.25
        elif right <= 0.50:
            usd_amount = left + 0.50
        else:
            usd_amount = left + 0.95
        return usd_amount

    else:
        return math.ceil(usd_amount)
