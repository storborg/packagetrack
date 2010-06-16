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


def dict_to_doc(d):
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

    dict_to_nodelist(d.values()[0], doc.documentElement)
    return doc


def doc_to_dict(n):
    first = n.childNodes[0]
    if len(n.childNodes) == 1 and first.nodeName == '#text':
        return first.data
    else:
        return dict((child.nodeName, doc_to_dict(child))
                    for child in n.childNodes)


def dict_to_xml(d):
    return dict_to_doc(d).toxml()


def xml_to_dict(s):
    return doc_to_dict(parseString(s))
