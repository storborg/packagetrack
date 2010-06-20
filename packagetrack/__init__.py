from .ups import UPSInterface
from .fedex import FedexInterface
from .usps import USPSInterface


__version__ = '0.1'

_interfaces = {}

def register_interface(shipper, interface):
    global _interfaces
    _interfaces[shipper] = interface


def get_interface(shipper):
        if shipper in _interfaces:
            return _interfaces[shipper]
        else:
            raise UnsupportedShipper


def init(ups_license_number, ups_user_id, ups_password):
    register_interface('UPS', UPSInterface(license_number=ups_license_number,
                                           user_id=ups_user_id,
                                           password=ups_password))
    register_interface('FedEx', FedexInterface())
    register_interface('USPS', USPSInterface())


class UnsupportedShipper(Exception):
    pass


class Package(object):

    def __init__(self, tracking_number):
        self.tracking_number = tracking_number
        self.shipper = None
        for shipper, iface in _interfaces.iteritems():
            if iface.identify(self.tracking_number):
                self.shipper = shipper
                break
    
    def track(self):
        return get_interface(self.shipper).track(self.tracking_number)

    def url(self):
        return get_interface(self.shipper).url(self.tracking_number)
