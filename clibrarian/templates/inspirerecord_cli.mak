Date: ${item.publishedDate}
Title: ${item.title}
Authors (${item.number_of_authors}):
	${"\n\t".join(item.authors)}
Summary:
	${item.summary}
Pages: ${item.pagination}
Citation: ${item.number_of_citations}
Collections:
% if type(item.primary_report_number) is list:
	${"\n\t".join(item.primary_report_number)}
% else:
	${item.primary_report_number}
% endif
DOI:
% if type(item.doi) is list:
	${"\n\t".join(item.doi)}
% else:
	${item.doi}
% endif
URL: http://inspirehep.net/record/${item.id}
