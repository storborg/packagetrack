from .ups import UPSInterface


__version__ = '0.1'

_interfaces = {}

def register_interface(shipper, interface_class):
    global _interfaces
    _interfaces[shipper] = interface_class


register_interface('UPS', UPSInterface)


class UnsupportedShipper(Exception):
    pass


class TrackingInfo(object):
    pass


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
    
    def _interface(self):
        if self.shipper in _interfaces:
            return _interfaces[self.shipper]()
            iface.track(self.tracking_number)
        else:
            raise UnsupportedShipper

    def track(self):
        return self._interface().track(self.tracking_number)

    def url(self):
        return self._interface().url(self.tracking_number)
