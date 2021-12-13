from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if not path.endswith('.json'):
            raise ValueError('Arquivo inválido')
        jobs = []
        with open(path) as file:
            jobs_reade = json.load(file)
            for job in jobs_reade:
                jobs.append(job)
        return jobs
