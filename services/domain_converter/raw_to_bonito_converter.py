from helpers import balanco_date_index_mapper
from helpers import conta_extractor_helper


def get_conta_wrapper(info_financeiras, index_to_date_mapper):
    def inner_function(conta):
        return conta_extractor_helper.retrieve_conta_with_date(
            conta, info_financeiras, index_to_date_mapper)

    return inner_function


def convert(raw, id_documento):
    index_to_date_mapper = balanco_date_index_mapper.indices_to_date(raw)

    conta_extractor_helper.retrieve_conta_with_date(
        'patrimonio_liquido', raw['informacoes_financeiras'], index_to_date_mapper)

    get_conta = get_conta_wrapper(raw['informacoes_financeiras'], index_to_date_mapper)

    return {
        'nome_empresa': raw['formulario_cadastral']['razao_social'],
        'codigo_cvm': raw['formulario_cadastral']['codigo_cvm'],
        'numero_documento_original': id_documento,
        'data_entrega_documento': raw['formulario_cadastral']['data_entrega'],
        'plano_contas': {
            'patrimonio_liquido': get_conta('patrimonio_liquido'),
            'ativo_total': get_conta('ativo_total'),
            'receita_liquida': get_conta('receita_liquida')
        }
    }
