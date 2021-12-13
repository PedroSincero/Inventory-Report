from inventory_report.reports.simple_report import SimpleReport
import json
import csv
import xml.etree.ElementTree as ET
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def import_data(cls, path, type_report):
        jobs = []
        type = {'completo': CompleteReport, 'simples': SimpleReport}
        with open(path) as file:
            if path.endswith(".csv"):
                jobs_reade = csv.DictReader(file)
            if path.endswith(".json"):
                jobs_reade = json.load(file)
            if path.endswith(".xml"):
                jobs_reade = read_xml(path)
            for job in jobs_reade:
                jobs.append(job)
            return type[type_report].generate(jobs)


def read_xml(path):
    tree = ET.parse(path)
    root = tree.getroot()
    jobs_reade = []
    for record in root:
        result_dict = {}
        for child_record in record:
            result_dict[child_record.tag] = child_record.text
        jobs_reade.append(result_dict)
    return jobs_reade


# Agradecimentos A
# Lucas Martins, Ederson Rodrigues, Gabriel Essenio - Turma 10 - Tribo B
