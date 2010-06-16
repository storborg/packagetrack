==================================================================================
packagetrack - Track UPS packages
==================================================================================

:Authors:
    Scott Torborg (storborg)
:Version: 0.1

This library provides UPS tracking tools.

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
>>> package = Package('1Z 999 999 99 9999 999 9')

>>> package.identify_shipper()
'UPS'
>>> package.track()

License
=======

Packagetrack is released under the GNU General Public License (GPL). See the
LICENSE file for full text of the license.


.. # vim: syntax=rst expandtab tabstop=4 shiftwidth=4 shiftround
