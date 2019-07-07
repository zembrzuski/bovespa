import re
from helpers.balanco_date_mapper.conta_definition import conta_definition


def evaluate_indicador(conta, info_financeira):
    for predicate in conta_definition[conta]['predicate']:
        tipo_info_financeira = \
            info_financeira['codigo_tipo_informacao_financeira'] == predicate['codigo_tipo_informacao_financeira']

        evaluated_regex = re.search(predicate['regex'], info_financeira['descricao_conta'], re.IGNORECASE)

        if tipo_info_financeira and evaluated_regex:
            return evaluated_regex

    return None


def retrieve_a_given_conta(conta, informacoes_financeiras):
    filtered_descricao_conta = list(filter(
        lambda x: evaluate_indicador(conta, x), informacoes_financeiras))

    if len(filtered_descricao_conta) != 1:
        raise Exception('errow. melhore tua regex!')

    return filtered_descricao_conta[0]


def retrieve_conta_with_date(conta, informacoes_financeiras, index_to_date_mapper, trimestre):
    valores_conta = retrieve_a_given_conta(conta, informacoes_financeiras)['valores_conta']
    tipo_conta = conta_definition[conta]['tipo_conta']

    conta_with_date = dict()

    for key, value in index_to_date_mapper[tipo_conta][trimestre-1].items():
        conta_with_date[value] = valores_conta[key]

    return conta_with_date
