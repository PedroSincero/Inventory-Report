from .simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, stock):
        simple_report = SimpleReport.generate(stock)
        all_stock = all_stock_company_reports(stock)
        return (
            f"{simple_report}\nProdutos estocados por empresa: \n{all_stock}"
        )


def all_stock_company_reports(stock):
    empresas = []
    result = ""
    for company in stock:
        empresas.append(company["nome_da_empresa"])
    cont = Counter(empresas)
    for k, v in cont.items():
        result += f"- {k}: {v}\n"

    return result
