"""
Helpers functions to convert nested dicts/lists to and from XML.

For example, this XML:

    <foo>
      <bar>
        <baz>what</baz>
        <quux>hello</quux>
      </bar>
      <sup>yeah</sup>
      <goodbye>no</goodbye>
    </foo>

Will be transformed to and from this dict:

    {'foo': {'bar': {'baz': 'what',
                     'quux': 'hello'},
             'sup': 'yeah',
             'goodbye': 'no'}}
"""

from xml.dom.minidom import getDOMImplementation, parseString


def dict_to_doc(d, attrs=None):
    assert len(d) == 1
    impl = getDOMImplementation()
    doc = impl.createDocument(None, d.keys()[0], None)

    def dict_to_nodelist(d, parent):
        for key, child in d.iteritems():
            new = doc.createElement(key)
            parent.appendChild(new)
            if type(child) == dict:
                dict_to_nodelist(child, new)
            else:
                new.appendChild(doc.createTextNode(child))

    if attrs:
        for key, val in attrs.iteritems():
            doc.documentElement.setAttribute(key, val)

    dict_to_nodelist(d.values()[0], doc.documentElement)
    return doc


def doc_to_dict(n):
    first = n.childNodes[0]
    if len(n.childNodes) == 1 and first.nodeName == '#text':
        return first.data
    else:
        return dict((child.nodeName, doc_to_dict(child))
                    for child in n.childNodes
                    if (child.nodeName != '#text')
                    or (child.data.strip() != ''))


def dict_to_xml(d, attrs=None):
    return dict_to_doc(d, attrs).toxml()


def xml_to_dict(s):
    return doc_to_dict(parseString(s))
