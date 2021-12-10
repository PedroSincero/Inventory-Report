from datetime import datetime
from collections import Counter


class SimpleReport:
    @classmethod
    def generate(cls, stock):
        old = old_date(stock, "Data de fabricação mais antiga: ")
        validation = validation_date(stock, "Data de validade mais próxima: ")
        company = stock_company(
            stock, "Empresa com maior quantidade de produtos estocados: "
        )
        return f"{old}\n{validation}\n{company}\n"


def old_date(stock, text):
    lowest_date = stock[0]["data_de_fabricacao"]
    for date in stock:
        if lowest_date > date["data_de_fabricacao"]:
            lowest_date = date["data_de_fabricacao"]
    return f"{text}{lowest_date}"


def validation_date(stock, text):
    data_val = stock[0]["data_de_validade"]
    date_now = str(datetime.now().date())
    for date in stock:
        if date["data_de_validade"] > date_now:
            if data_val > date["data_de_validade"]:
                data_val = date["data_de_validade"]
    return f"{text}{data_val}"


def stock_company(stock, text):
    result = []
    for company in stock:
        result.append(company["nome_da_empresa"])
    return f"{text}{max(Counter(result))}"
