from datetime import datetime, date
from unittest import TestCase
from nose.plugins.skip import SkipTest

import packagetrack
from packagetrack import Package, UnsupportedShipper


class TestPackageTrack(TestCase):

    def test_identify_ups(self):
        assert Package('1Z9999999999999999').shipper == 'UPS'

    def test_ups_url(self):
        num = '1Z9999999999999999'
        url = Package(num).url()
        assert num in url
        assert url.startswith('http')

    def test_track_ups(self):
        if not packagetrack.config.has_section('UPS'):
            raise SkipTest
        # This is just a random tracking number found on google. To find more,
        # google for something like:
        # ["Tracking Detail" site:wwwapps.ups.com inurl:WebTracking]
        p = Package('1Z58R4770350434926')
        info = p.track()
        assert info.status != ''
        assert isinstance(info.delivery_date, date)
        assert isinstance(info.last_update, datetime)

    def test_identify_fedex(self):
        assert Package('012345678901234').shipper == 'FedEx'

    def test_fedex_url(self):
        num = '012345678901234'
        url = Package(num).url()
        assert num in url
        assert url.startswith('http')

    def test_track_fedex(self):
        p = Package('012345678901234')
        try:
            p.track()
        except NotImplementedError:
            pass
        else:
            raise AssertionError('tracking fedex package should fail')

    def test_identify_usps(self):
        assert Package('91124235').shipper == 'USPS'

    def test_usps_url(self):
        num = '91124235'
        url = Package(num).url()
        assert num in url
        assert url.startswith('http')

    def test_identify_unknown(self):
        assert Package('14324423523').shipper == None

    def test_track_unknown(self):
        try:
            Package('12391241248').track()
        except UnsupportedShipper:
            pass
        else:
            raise AssertionError("tracking package with unknown "
                                 "shipper should fail")
