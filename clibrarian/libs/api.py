import json
import httplib
import urllib2

from lxml import etree, objectify

class AbstractApi(object):
    """ Generic API
    """

    def __init__(self):
        self.baseuri = ""
        self.resource = ""
        self.parameters = ""

    def build_url(self, resource=None, parameters=None):
        """Build URL for API access"""
        if resource is not None:
            self.resource = resource
        if parameters is not None:
            self.parameters = parameters

        return "{url}/{resource}?{parameters}".format(
                url=self.baseuri,
                resource=self.resource,
                parameters=self.parameters
            )

    def do_query(self, url, debug=False):
        if debug:
            print(url)
            httplib.HTTPConnection.debuglevel = 1
        req = urllib2.Request(
            url,
            data=None,
        )
        return urllib2.urlopen(req).read()

    def get_json(self, url, debug=False):
        data = self.do_query(url, debug)

        try:
            return json.loads(data)
        except ValueError as e:
            print(data)
            return {}
    
    def get_xml(self, url, debug=False):
        """Convert XML to python object"""
        return objectify.fromstring(
                self.do_query(url, debug)
            )


    def search(self, query, debug=False):
        pass

    def get_volumes(self, volumes, debug=False):
        pass
