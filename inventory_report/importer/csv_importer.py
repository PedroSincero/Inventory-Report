from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if not path.endswith('.csv'):
            raise ValueError('Arquivo inválido')
        jobs = []
        with open(path) as file:
            jobs_reade = csv.DictReader(file)
            for job in jobs_reade:
                jobs.append(job)
        return jobs
