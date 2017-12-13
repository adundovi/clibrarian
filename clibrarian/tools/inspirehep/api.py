import json

from clibrarian.libs.api import AbstractApi
from clibrarian.libs.items import InspireRecord

class InspireHEPApi(AbstractApi):
    """API for INSPIRE-HEP
       http://inspirehep.net/info/hep/api
       https://github.com/inspirehep/invenio/blob/prod/modules/bibfield/etc/atlantis.cfg
    """

    def __init__(self):
        self.baseuri = "http://inspirehep.net"
        self.tags = [
            'recid',
            'number_of_citations',
            'authors',
            'title',
            'abstract',
            'prepublication',
            'physical_description',
            'number_of_authors',
            'primary_report_number',
            'doi'
                ]

    def search(self, query, debug=False):
        url = self.build_url(
                resource='search',
                parameters="&".join([
                    'p='+query,
                    'of=recjson',
                    'rg=10',
                    'ot='+",".join(self.tags),
                    'so=d'
                    ])
                )

        json = self.get_json(url, debug)

        records = []
        for item in json:
            record = InspireRecord()
            record.from_json(item)
            records.append(record)

        return records

    def get_record(self, query, debug=False):
        url = self.build_url(
                resource='record/'+query,
                parameters="&".join([
                    'of=recjson',
                    'ot='+",".join(self.tags),
                    ])
                )

        json = self.get_json(url, debug)
       
        record = InspireRecord()
        record.from_json(json[0])

        return record

