from helpers import regex_helper


def __to_map(valoes_conta):
    mapped = {
        0: valoes_conta[0]
    }

    for i in range(1, len(valoes_conta)):
        if valoes_conta[i] > 0:
            mapped[i] = valoes_conta[i]

    filtered = dict()

    for i in range(len(mapped)):
        if mapped[i] != 0:
            filtered[i] = mapped[i]

    return filtered


def __retrieve_a_given_conta(indicador, raw):
    filtered = list(filter(
        lambda x: regex_helper.evaluate_indicador(indicador, x['descricao_conta']),
        raw['informacoes_financeiras']))

    if len(filtered) != 1:
        raise Exception('errow. melhore tua regex!')

    return filtered[0]


def indices_to_date(raw):
    patrimonio_liquido = __retrieve_a_given_conta('patrimonio_liquido', raw)
    valores_conta_mapped = __to_map(patrimonio_liquido['valores_conta'])

    data_documento = raw['formulario_cadastral']['data_documento']['data_referencia_documento']

    indices_to_date_mapper = dict()

    for i in range(0, len(valores_conta_mapped)):
        new_date = data_documento.replace(year=data_documento.year - i)
        indices_to_date_mapper[list(valores_conta_mapped.keys())[i]] = new_date

    return indices_to_date_mapper
