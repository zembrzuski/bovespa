from helpers import conta_extractor_helper
from helpers.balanco_date_mapper import dfp_resolver
from helpers.balanco_date_mapper import itr_resolver


def indices_to_date(raw):
    patrimonio_liquido = conta_extractor_helper.retrieve_a_given_conta(
        'patrimonio_liquido', raw['informacoes_financeiras'])

    data_documento = raw['formulario_cadastral']['data_documento']['data_referencia_documento']

    if raw['document_type'] == 'ITR':
        return itr_resolver.indices_to_date_itr(data_documento)

    if raw['document_type'] == 'DFP':
        return dfp_resolver.indices_to_date_dfp(patrimonio_liquido, data_documento)
