from unittest import TestCase

from packagetrack import Package


class TestPackageTrack(TestCase):

    def test_identify_ups(self):
        assert Package('1Z9999999999999999').shipper == 'UPS'

    def test_identify_fedex(self):
        assert Package('012345678901234').shipper == 'FedEx'

    def test_identify_usps(self):
        assert Package('91124235').shipper == 'USPS'

    def test_identify_unknown(self):
        assert Package('143244235235').shipper == None
