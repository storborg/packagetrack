class TrackingInfo(object):
    
    def __init__(self, delivery_date, status, last_update):
        self.delivery_date = delivery_date
        self.status = status
        self.last_update = last_update

    def __repr__(self):
        return ('<TrackingInfo(delivery_date=%r, status=%r, last_update=%r)>' %
                (self.delivery_date, self.status, self.last_update))
