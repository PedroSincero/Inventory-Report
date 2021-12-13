from inventory_report.importer.importer import Importer

import xml.etree.ElementTree as ET


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if not path.endswith('.xml'):
            raise ValueError('Arquivo inválido')
        jobs = []
        tree = ET.parse(path)
        root = tree.getroot()
        for record in root:
            result_dict = {}
            for child_record in record:
                result_dict[child_record.tag] = child_record.text
            jobs.append(result_dict)
        return jobs
