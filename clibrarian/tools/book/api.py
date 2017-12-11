import json
import httplib
import urllib2

from clibrarian.libs.items import Book

class GoogleBooksApi(object):
    """API for Google Books
       https://developers.google.com/books/docs/v1/reference/
       https://developers.google.com/books/docs/v1/using
    """

    def __init__(self):
        self.baseuri = "https://www.googleapis.com/books/v1"

    def build_url(self, resource=None, parameters=None):
        """Build URL for API access"""
        if resource is not None:
            self.resource = resource
        if parameters is not None:
            self.parameters = parameters

        return "{url}/{resource}{parameters}".format(
            url=self.baseuri,
            resource=self.resource,
            parameters=self.parameters)

    def do_query(self, url, debug=False):
        if debug:
            print(url)
            httplib.HTTPConnection.debuglevel = 1

        req = urllib2.Request(
            url,
            data=None,
        )
        raw_json = urllib2.urlopen(req).read()
        return json.loads(raw_json)

    def search(self, query, debug=False):
        url = self.build_url(
                resource='volumes',
                parameters='?q='+query)

        json = self.do_query(url, debug)

        books = []
        for item in json['items']:
            book = self.json2book(item)
            books.append(book)

        return books

    def get_volumes(self, volumes, debug=False):
        """Obtain search results"""
        url = self.build_url(
                resource='volumes',
                parameters='/'+volumes)

        json = self.do_query(url, debug)
        book = self.json2book(json)
        return book

    def json2book(self, json):

        book = Book()
        book.googleId = json['id']
        book.googleLink = json['selfLink']
        book.title = json['volumeInfo']['title']
        if 'subtitle' in json['volumeInfo']:
            book.subtitle = json['volumeInfo']['subtitle']
        if 'authors' in json['volumeInfo']:
            book.authors = json['volumeInfo']['authors']
        if 'publisher' in json['volumeInfo']:
            book.publisher = json['volumeInfo']['publisher']
        if 'publishedDate' in json['volumeInfo']:
            book.publishedDate = json['volumeInfo']['publishedDate']
        if 'description' in json['volumeInfo']:
            book.description = json['volumeInfo']['description']
        for identifiers in json['volumeInfo']['industryIdentifiers']:
            if identifiers['type'] == "ISBN_13":
                book.isbn = identifiers['identifier']
            elif identifiers['type'] == "ISBN_10":
                book.isbn = identifiers['identifier']
        if 'pageCount' in json['volumeInfo']:
            book.pageCount = json['volumeInfo']['pageCount']
        if 'categories' in json['volumeInfo']:
            book.categories = json['volumeInfo']['categories']
        if 'averageRating' in json['volumeInfo']:
            book.averageRating = json['volumeInfo']['averageRating']
        if 'ratingsCount' in json['volumeInfo']:
            book.ratingsCount = json['volumeInfo']['ratingsCount']

        return book
    
