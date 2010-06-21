import urllib
from datetime import datetime, date, time

import packagetrack
from .xml_dict import dict_to_xml, xml_to_dict
from .data import TrackingInfo


class UPSInterface(object):
    url = 'https://wwwcie.ups.com/ups.app/xml/Track'

    def __init__(self):
        self.attrs = {'xml:lang': 'en-US'}

    def identify(self, tracking_number):
        return tracking_number.startswith('1Z')

    def build_access_request(self):
        d = {'AccessRequest':
             {'AccessLicenseNumber': packagetrack.UPS_LICENSE_NUMBER,
              'UserId': packagetrack.UPS_USER_ID,
              'Password': packagetrack.UPS_PASSWORD}}
        return dict_to_xml(d, self.attrs)

    def build_track_request(self, tracking_number):
        req = {'TransactionReference': {'RequestAction': 'Track'}}
        d = {'TrackRequest': {'Request': req,
                              'TrackingNumber': tracking_number}}
        return dict_to_xml(d)

    def build_request(self, tracking_number):
        return (self.build_access_request() +
                self.build_track_request(tracking_number))

    def send_request(self, tracking_number):
        body = self.build_request(tracking_number)
        webf = urllib.urlopen(self.url, body)
        resp = webf.read()
        webf.close()
        return resp

    def parse_response(self, raw):
        root = xml_to_dict(raw)['TrackResponse']
        response = root['Response']
        status_code = response['ResponseStatusCode']
        status_description = response['ResponseStatusDescription']
        # Check status code?

        # Parse delivery date, status, and last update.
        est_delivery_date = datetime.strptime(
            root['Shipment']['ScheduledDeliveryDate'],
            "%Y%m%d")

        package = root['Shipment']['Package']
        activity = package['Activity']
        last_update_date = datetime.strptime(activity['Date'], "%Y%m%d").date()
        last_update_time = datetime.strptime(activity['Time'], "%H%M%S").time()
        last_update = datetime.combine(last_update_date, last_update_time)
        status = activity['Status']['StatusType']['Description']

        return TrackingInfo(last_update=last_update,
                            delivery_date=est_delivery_date,
                            status=status)
        
    def track(self, tracking_number):
        "Track a UPS package by number. Returns just a delivery date."
        resp = self.send_request(tracking_number)
        return self.parse_response(resp)
