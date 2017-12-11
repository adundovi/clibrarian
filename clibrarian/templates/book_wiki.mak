{{Book
|title=${book.title}${': ' + book.subtitle if book.subtitle != '' else ''}
|authors=${", ".join(book.authors)}
|publisher=${book.publisher}
|date=${book.publishedDate}
|isbn=${book.isbn}
}}
