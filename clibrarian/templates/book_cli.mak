Title: ${book.title}
%if book.subtitle != '':
	${book.subtitle}
%endif
Authors:
	${"\n\t".join(book.authors)}
ISBN: ${book.isbn}
GoogleID: ${book.googleId}
GoogleLink: ${book.googleLink}
