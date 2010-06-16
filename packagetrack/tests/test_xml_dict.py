from unittest import TestCase

from packagetrack import xml_dict

test_xml = '''<?xml version="1.0"?>
<foo>
  <bar>
    <baz>what</baz>
    <quux>hello</quux>
  </bar>
  <sup>yeah</sup>
  <goodbye>no</goodbye>
</foo>'''

test_dict = {'foo': {'bar': {'baz': 'what',
                     'quux': 'hello'},
             'sup': 'yeah',
             'goodbye': 'no'}}


class TestXMLDict(TestCase):

    def test_xml_to_dict(self):
        assert xml_dict.xml_to_dict(test_xml) == test_dict

    def test_roundtrip(self):
        assert (xml_dict.xml_to_dict(xml_dict.dict_to_xml(test_dict)) ==
                test_dict)

    def test_attribute(self):
        xml = xml_dict.dict_to_xml(test_dict, {'xml:lang': 'en-US'})
        assert '<foo xml:lang="en-US">' in xml
