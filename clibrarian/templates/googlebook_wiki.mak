{{Book
|title=${item.title}${': ' + item.subtitle if item.subtitle != '' else ''}
|authors=${", ".join(item.authors)}
|publisher=${item.publisher}
|date=${item.publishedDate}
|isbn=${item.isbn}
}}
