from inventory_report.reports.simple_report import SimpleReport
import csv

# inventory_report/reports/simple_report.py
# exec("../reports/simple_report.py")
from inventory_report.reports.complete_report import CompleteReport

# ("/home/el/foo2/mylib.py")


class Inventory:
    @classmethod
    def import_data(cls, path, type_report):
        jobs = []
        with open(path) as file:
            jobs_reade = csv.DictReader(file)
            for job in jobs_reade:
                jobs.append(job)
            if type_report == "completo":
                return CompleteReport.generate(jobs)
            if type_report == "simples":
                return SimpleReport.generate(jobs)
