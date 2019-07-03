import re

conta_filter = {
    'patrimonio_liquido': {
        'regex': '^patr(\.)?(im[oô]nio)? l[ií]q(\.)?(uido)?$',
        'codigo_tipo_informacao_financeira': 1,
        'tipo_informacao': 'balanco_patrimonial'

    },
    'lucro_liquido': {
        'regex': '^lucro l.quido consolidado',
        'codigo_tipo_informacao_financeira': 2,
        'tipo_informacao': 'demonstracao_resultado'
    }
}


def evaluate_indicador(conta, txt):
    return re.search(conta_filter[conta]['regex'], txt, re.IGNORECASE)


def retrieve_a_given_conta(conta, informacoes_financeiras):
    filtered_descricao_conta = list(filter(
        lambda x: evaluate_indicador(conta, x['descricao_conta']),
        informacoes_financeiras))

    filtered_info_financeira = list(filter(
        lambda x: x['codigo_tipo_informacao_financeira'] == conta_filter[conta]['codigo_tipo_informacao_financeira'],
        filtered_descricao_conta))

    if len(filtered_info_financeira) != 1:
        raise Exception('errow. melhore tua regex!')

    return filtered_info_financeira[0]


def convert_date_for_balanco_patrimonial(valores_conta, index_to_date_mapper):
    conta_with_date = dict()

    for key, value in index_to_date_mapper.items():
        conta_with_date[value] = valores_conta[key]

    return conta_with_date


def convert_date_for_demonstracao_resultado(valores_conta, index_to_date_mapper):
    print('oi')
    pass


def retrieve_conta_with_date(conta, informacoes_financeiras, index_to_date_mapper):
    valores_conta = retrieve_a_given_conta(conta, informacoes_financeiras)['valores_conta']

    if conta_filter[conta]['tipo_informacao'] == 'balanco_patrimonial':
        return convert_date_for_balanco_patrimonial(valores_conta, index_to_date_mapper)

    if conta_filter[conta]['tipo_informacao'] == 'demonstracao_resultado':
        return convert_date_for_demonstracao_resultado(valores_conta, index_to_date_mapper)


    print('AE')

