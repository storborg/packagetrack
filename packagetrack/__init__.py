__version__ = '0.1'


def identify_tracking_num(num):
    """
    This could be better. See more info here:
        http://answers.google.com/answers/threadview/id/207899.html
    """
    if num.startswith('1Z'):
        return 'UPS'
    elif len(num) == 15:
        return 'FedEx'
    elif num.startswith('91'):
        return 'USPS'
    else:
        return None
