import json

from clibrarian.libs.api import AbstractApi
from clibrarian.libs.items import GoogleBook

class GoogleBooksApi(AbstractApi):
    """API for Google Books
       https://developers.google.com/books/docs/v1/reference/
       https://developers.google.com/books/docs/v1/using
    """

    def __init__(self):
        AbstractApi.__init__(self)
        self.baseuri = "https://www.googleapis.com/books/v1"

    def search(self, query, debug=False):
        url = self.build_url(
                resource='volumes',
                parameters='q='+query)

        json = self.get_json(url, debug)

        books = []
        for item in json['items']:
            book = GoogleBook()
            book.from_json(item)
            books.append(book)

        return books

    def get_volumes(self, volumes, debug=False):
        """Obtain search results"""
        url = self.build_url(
                resource='volumes/'+volumes)

        json = self.get_json(url, debug)
        book = GoogleBook()
        book.from_json(json)
        return book
