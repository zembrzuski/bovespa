import re

regexes = {
    'patrimonio_liquido': '^patr(\.)?(im[oô]nio)? l[ií]q(\.)?(uido)?$'
}


def evaluate_indicador(indicador, txt):
    return re.search(regexes[indicador], txt, re.IGNORECASE)


def retrieve_a_given_conta(indicador, raw):
    filtered = list(filter(
        lambda x: evaluate_indicador(indicador, x['descricao_conta']),
        raw['informacoes_financeiras']))

    if len(filtered) != 1:
        raise Exception('errow. melhore tua regex!')

    return filtered[0]
