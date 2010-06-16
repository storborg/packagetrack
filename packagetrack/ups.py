import urllib

from .xml_dict import dict_to_xml


class UPSInterface(object):
    url = 'https://wwwcie.ups.com/ups_app/xml/Track'

    def __init__(self, license_number=None, user_id=None, password=None):
        self.license_number = license_number
        self.user_id = user_id
        self.password = password
        self.attrs = {'xml:lang': 'en-US'}

    def identify(self, tracking_number):
        return tracking_number.startswith('1Z')

    def build_access_request(self):
        d = {'AccessRequest': {'AccessLicenseNumber': self.license_number,
                               'UserId': self.user_id,
                               'Password': self.password}}
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
        body = self.build_request(self.tracking_number)
        webf = urllib.urlopen(self.url, body)
        resp = webf.read()
        webf.close()

    def parse_request(self, resp):
        main = resp['TrackResponse']
        response = main['Response']
        status_code = response['ResponseStatusCode']
        status_description = response['ResponseStatusDescription']

        # Parse activity.

        # Parse status.

        
    def track(self, tracking_number):
        "Track a UPS package by number. Returns just a delivery date."
        resp = self.make_request(self, tracking_number)
