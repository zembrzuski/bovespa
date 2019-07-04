from helpers.balanco_date_mapper import date_resolver
from helpers import conta_extractor_helper


def conta_currying(info_financeiras, index_to_date_mapper, trimestre):
    def inner(conta):
        return conta_extractor_helper.retrieve_conta_with_date(
            conta, info_financeiras, index_to_date_mapper, trimestre)

    return inner


def convert(raw, id_documento):
    index_to_date_mapper = date_resolver.indices_to_date(raw)

    trimestre = int(raw['formulario_cadastral']['data_documento']['data_referencia_documento'].month / 3)

    conta_wrapper = conta_currying(raw['informacoes_financeiras'], index_to_date_mapper, trimestre)

    return {
        'nome_empresa': raw['formulario_cadastral']['razao_social'],
        'codigo_cvm': raw['formulario_cadastral']['codigo_cvm'],
        'numero_documento_original': id_documento,
        'data_entrega_documento': raw['formulario_cadastral']['data_entrega'],
        'id_documento': id_documento,
        'tipo_documento': raw['document_type'],
        'plano_contas': {
            'patrimonio_liquido': conta_wrapper('patrimonio_liquido'),
            'lucro_liquido': conta_wrapper('lucro_liquido')
        }
    }
