from helpers import regex_helper


def __convert_conta_dfp(conta, data_referencia):
    print('oi')
    return True


def __convert_conta_itr(conta, data_referencia):
    raise Exception('not implemented yet')


def __convert_a_given_conta(indicador, raw):
    filtered = list(filter(
        lambda x: regex_helper.evaluate_indicador(indicador, x['descricao_conta']),
        raw['informacoes_financeiras']))

    if len(filtered) != 1:
        raise Exception('errow')

    conta = filtered[0]

    if raw['document_type'] == 'DFP':
        return __convert_conta_dfp(conta, raw['formulario_cadastral']['data_referencia_documento'])
    elif raw['document_type'] == 'ITR':
        return __convert_conta_itr(conta, raw['formulario_cadastral']['data_referencia_documento'])
    else:
        raise Exception('the world is over')


def convert(raw, id_documento):
    patrimonio_liquido = __convert_a_given_conta('patrimonio_liquido', raw)


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
