class USPSInterface(object):

    def identify(self, tracking_number):
        return tracking_number.startswith('91')
