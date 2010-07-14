class FedexInterface(object):

    def identify(self, tracking_number):
        return len(tracking_number) in (12, 15)

    def track(self, tracking_number):
        raise NotImplementedError

    def url(self, tracking_number):
        return ('http://www.fedex.com/Tracking?tracknumbers=%s'
                % tracking_number)
