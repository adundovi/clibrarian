Title: ${book.title}
%if book.subtitle != '':
	${book.subtitle}
%endif
Authors:
	${"\n\t".join(book.authors)}
Publisher: ${book.publisher}
Date of publishing: ${book.publishedDate}
ISBN: ${book.isbn}
Google ID: ${book.googleId}
GoogleLink: ${book.googleLink}
