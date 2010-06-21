from datetime import datetime, date
from unittest import TestCase

from packagetrack.data import TrackingInfo


class TestTrackingInfo(TestCase):

    def test_repr(self):
        now = datetime.now()
        today = date.today()
        info = TrackingInfo(delivery_date=today,
                            status='IN TRANSIT',
                            last_update=now)
        s = repr(info)
        assert repr(now) in s
        assert repr(today) in s
        assert 'IN TRANSIT' in s

        
