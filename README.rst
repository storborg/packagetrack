==================================================================================
packagetrack - Track UPS packages
==================================================================================

:Authors:
    Scott Torborg (storborg)
:Version: 0.1

This library tracks packages.

*Note* Use at your own risk!

Installation
============

Simple as::

    $ easy_install packagetrack

Or if you prefer, download the source and then::

    $ python setup.py build
    $ python setup.py install

Example
=======

>>> from packagetrack import Package
>>> package = Package('1Z9999999999999999')
# Identify packages (UPS, FedEx, and USPS)
>>> package.shipper
'UPS'
# Track packages (UPS only, requires API access)
>>> info = package.track()
>>> print info.status
IN TRANSIT TO
>>> print info.delivery_date
2010-06-25 00:00:00
>>> print info.last_update
2010-06-19 00:54:00
# Get tracking URLs (UPS, FedEx, and USPS)
>>> print package.url()
http://wwwapps.ups.com/WebTracking/processInputRequest?TypeOfInquiryNumber=T&InquiryNumber1=1Z9999999999999999


UPS API Configuration
=====================

To enable UPS package tracking, get an account and an API license number on the
UPS website, then make a file at ~/.packagetrack that looks like::

    [UPS]
    license_number = XXXXXXXXXXXXXXXX
    user_id = XXXX
    password = XXXX

License
=======

Packagetrack is released under the GNU General Public License (GPL). See the
LICENSE file for full text of the license.


.. # vim: syntax=rst expandtab tabstop=4 shiftwidth=4 shiftround
