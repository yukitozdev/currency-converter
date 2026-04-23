usd_rate = 5.15
eur_rate = 6.08

def brl_to_usd(amount):
    return amount / usd_rate

def brl_to_eur(amount):
    return amount / eur_rate

def usd_to_brl(amount):
    return amount * usd_rate

def eur_to_brl(amount):
    return amount * eur_rate