import re
from helpers.balanco_date_mapper.conta_definition import conta_definition


def evaluate_indicador(conta, txt):
    return re.search(conta_definition[conta]['regex'], txt, re.IGNORECASE)


def retrieve_a_given_conta(conta, informacoes_financeiras):
    filtered_descricao_conta = list(filter(
        lambda x: evaluate_indicador(conta, x['descricao_conta']),
        informacoes_financeiras))

    filtered_info_financeira = list(filter(
        lambda x: x['codigo_tipo_informacao_financeira'] == conta_definition[conta]['codigo_tipo_informacao_financeira'],
        filtered_descricao_conta))

    if len(filtered_info_financeira) != 1:
        raise Exception('errow. melhore tua regex!')

    return filtered_info_financeira[0]


def retrieve_conta_with_date(conta, informacoes_financeiras, index_to_date_mapper, trimestre):
    valores_conta = retrieve_a_given_conta(conta, informacoes_financeiras)['valores_conta']
    tipo_conta = conta_definition[conta]['tipo_conta']

    conta_with_date = dict()

    for key, value in index_to_date_mapper[tipo_conta][trimestre-1].items():
        conta_with_date[value] = valores_conta[key]

    return conta_with_date
