from helpers import balanco_date_index_mapper


def convert(raw, id_documento):
    index_to_date_mapper = balanco_date_index_mapper.indices_to_date(raw)

    print('ae')
    return {
        'nome_empresa': raw['formulario_cadastral']['razao_social'],
        'codigo_cvm': raw['formulario_cadastral']['codigo_cvm'],
        'numero_documento_original': id_documento,
        'data': None,
        'data_entrega_documento': raw['formulario_cadastral']['data_entrega'],
        'plano_contas': {
            'patrimonio_liquido': None
        }
    }
