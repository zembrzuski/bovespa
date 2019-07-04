from helpers import conta_extractor_helper
from helpers.balanco_date_mapper import dfp_resolver
from helpers.balanco_date_mapper import itr_resolver


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

    data_documento = raw['formulario_cadastral']['data_documento']['data_referencia_documento']

    if raw['document_type'] == 'ITR':
        return itr_resolver.indices_to_date_itr(data_documento)

    if raw['document_type'] == 'DFP':
        return dfp_resolver.indices_to_date_dfp(patrimonio_liquido, data_documento)
