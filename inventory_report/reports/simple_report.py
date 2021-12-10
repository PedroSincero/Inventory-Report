from datetime import datetime
from collections import Counter


class SimpleReport:
    @classmethod
    def generate(cls, stock):
        old = old_date(stock)
        validation = validation_date(stock)
        company = stock_company(stock)
        return f"{old}\n{validation}\n{company}\n"


def old_date(date):
    menor_data = date[0]["data_de_fabricacao"]
    for data in date:
        if menor_data > data["data_de_fabricacao"]:
            menor_data = data["data_de_fabricacao"]
    return f"Data de fabricação mais antiga: {menor_data}"


def validation_date(date):
    data_val = date[0]["data_de_validade"]
    data_atual = str(datetime.now().date())
    for data in date:
        if data["data_de_validade"] > data_atual:
            if data_val > data["data_de_validade"]:
                data_val = data["data_de_validade"]
    return f"Data de validade mais próxima: {data_val}"


def stock_company(stock):
    result = []
    palavras = "Empresa com maior quantidade de produtos estocados"
    for company in stock:
        result.append(company["nome_da_empresa"])
    return f"{palavras}: {max(Counter(result))}"
