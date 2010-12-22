class USPSInterface(object):

    def identify(self, tracking_number):
        return (tracking_number.startswith('91') or
                tracking_number.startswith('94'))

    def url(self, tracking_number):
        return ('http://trkcnfrm1.smi.usps.com/PTSInternetWeb/'
                'InterLabelInquiry.do?origTrackNum=%s' % tracking_number)

    def validate(self, tracking_number):
        "Return True if this is a valid USPS tracking number."
        tracking_num = tracking_number[:-1].replace(' ', '')
        odd_total = 0
        even_total = 0
        for ii, digit in enumerate(tracking_num):
            if ii % 2:
                odd_total += int(digit)
            else:
                even_total += int(digit)
        total = odd_total + even_total * 3
        check = ((total - (total % 10) + 10) - total) % 10
        return (check == int(tracking_number[-1:]))
