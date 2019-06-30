import re

regexes = {
    'patrimonio_liquido': '^patr(\.)?(im[oô]nio)? l[ií]q(\.)?(uido)?$',
    'ativo_total': '^ativo total$'
}


def evaluate_indicador(conta, txt):
    return re.search(regexes[conta], txt, re.IGNORECASE)


def retrieve_a_given_conta(conta, informacoes_financeiras):
    filtered = list(filter(
        lambda x: evaluate_indicador(conta, x['descricao_conta']),
        informacoes_financeiras))

    if len(filtered) != 1:
        raise Exception('errow. melhore tua regex!')

    return filtered[0]


def retrieve_conta_with_date(conta, informacoes_financeiras, index_to_date_mapper):
    valores_conta = retrieve_a_given_conta(conta, informacoes_financeiras)['valores_conta']

    conta_with_date = dict()

    for key, value in index_to_date_mapper.items():
        conta_with_date[value] = valores_conta[key]

    return conta_with_date
