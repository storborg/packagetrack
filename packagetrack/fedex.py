class FedexInterface(object):

    def identify(self, tracking_number):
        return len(tracking_number) == 15
