from helpers import conta_extractor_helper


def __to_map(valores_conta):
    mapped = {
        0: valores_conta[0]
    }

    for i in range(1, len(valores_conta)):
        if valores_conta[i] > 0:
            mapped[i] = valores_conta[i]

    filtered = dict()

    for i in range(len(mapped)):
        if mapped[i] != 0:
            filtered[i] = mapped[i]

    return filtered


def indices_to_date(raw):
    patrimonio_liquido = conta_extractor_helper.retrieve_a_given_conta(
        'patrimonio_liquido', raw['informacoes_financeiras'])

    valores_conta_mapped = __to_map(patrimonio_liquido['valores_conta'])

    data_documento = raw['formulario_cadastral']['data_documento']['data_referencia_documento']

    indices_to_date_mapper = dict()

    for i in range(0, len(valores_conta_mapped)):
        new_date = data_documento.replace(year=data_documento.year - i)
        indices_to_date_mapper[list(valores_conta_mapped.keys())[i]] = new_date

    return indices_to_date_mapper
