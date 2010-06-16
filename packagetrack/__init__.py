__version__ = '0.1'


class Package(object):

    def __init__(self, tracking_number):
        self.tracking_number = tracking_number
        if self.tracking_number.startswith('1Z'):
            self.shipper = 'UPS'
        elif len(self.tracking_number) == 15:
            self.shipper = 'FedEx'
        elif self.tracking_number.startswith('91'):
            self.shipper = 'USPS'
        else:
            self.shipper = None
