Title: ${item.title}
%if item.subtitle != '':
	${item.subtitle}
%endif
Authors:
	${"\n\t".join(item.authors)}
Publisher: ${item.publisher}
Date of publishing: ${item.publishedDate}
ISBN: ${item.isbn}
Google ID: ${item.id}
GoogleLink: ${item.googleLink}
