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


# result = [
#     {
#         "id": 1,
#         "nome_do_produto": "CALENDULA OFFICINALIS FLOWERING TOP",
#         "nome_da_empresa": "Forces of Nature",
#         "data_de_fabricacao": "2020-07-04",
#         "data_de_validade": "2023-02-09",
#         "numero_de_serie": "FR48 2002 7680 97V4 W6FO LEBT 081",
#         "instrucoes_de_armazenamento": "in blandit ultrices enim",
#     },
#     {
#         "id": 2,
#         "nome_do_produto": "sodium ferric gluconate complex",
#         "nome_da_empresa": "sanofi-aventis U.S. LLC",
#         "data_de_fabricacao": "2020-05-31",
#         "data_de_validade": "2023-01-17",
#         "numero_de_serie": "SE95 2662 8860 5529 8299 2861",
#         "instrucoes_de_armazenamento": "duis bibendum morbi",
#     },
#     {
#         "id": 3,
#         "nome_do_produto": "Dexamethasone Sodium Phosphate",
#         "nome_da_empresa": "sanofi-aventis U.S. LLC",
#         "data_de_fabricacao": "2019-09-13",
#         "data_de_validade": "2023-02-13",
#         "numero_de_serie": "BA52 2034 8595 7904 7131",
#         "instrucoes_de_armazenamento": "morbi quis tortor id",
#     },
#     {
#         "id": 4,
#         "nome_do_produto": "Uricum acidum, Benzoicum acidum",
#         "nome_da_empresa": "Newton Laboratories, Inc.",
#         "data_de_fabricacao": "2019-11-08",
#         "data_de_validade": "2019-11-25",
#         "numero_de_serie": "FR38 9203 3060 400T QQ8B HHS0 Q46",
#         "instrucoes_de_armazenamento": "velit eu est congue elementum",
#     },
# ]


def stock_company(stock):
    result = []
    palavras = "Empresa com maior quantidade de produtos estocados"
    for company in stock:
        result.append(company["nome_da_empresa"])
    return f"{palavras}: {max(Counter(result))}"


# print(old_date(result))
# # print(datetime.now().date())
# print(validation_date(result))
# print(stock_company(result))
