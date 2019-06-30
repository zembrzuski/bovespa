from helpers import regex_helper


def __retrieve_a_given_conta(indicador, raw):
    filtered = list(filter(
        lambda x: regex_helper.evaluate_indicador(indicador, x['descricao_conta']),
        raw['informacoes_financeiras']))

    if len(filtered) != 1:
        raise Exception('errow')

    return filtered[0]


def __indices_to_date_dfp(valores_conta, data_referencia_documento):
    indices_to_date_mapper = dict()

    valores_conta_importantes = list(filter(
        lambda x: x != 0, valores_conta))

    for i in range(0, len(valores_conta_importantes)):
        new_date = data_referencia_documento.replace(year=data_referencia_documento.year - i)
        indices_to_date_mapper[i] = new_date

    return indices_to_date_mapper


def get_number_of_days_in_month(month):
    if month == 3:
        return 31
    if month == 6:
        return 30
    if month == 9:
        return 30

    raise Exception('errow')


def __indices_to_date_itr(valores_conta, data_referencia_documento):
    indices_to_date_mapper = dict()

    valores_conta_importantes = list(filter(
        lambda x: x != 0, valores_conta))

    for i in range(0, len(valores_conta_importantes)):
        new_date = data_referencia_documento.replace(month=data_referencia_documento.month - 3*i)
        new_date = new_date.replace(day=get_number_of_days_in_month(new_date.month))
        indices_to_date_mapper[i] = new_date

    return indices_to_date_mapper


def __indices_to_date(raw):
    patrimonio_liquido = __retrieve_a_given_conta('patrimonio_liquido', raw)

    if raw['document_type'] == 'DFP':
        return __indices_to_date_dfp(
            patrimonio_liquido['valores_conta'], raw['formulario_cadastral']['data_referencia_documento'])
    elif raw['document_type'] == 'ITR':
        return __indices_to_date_itr(
            patrimonio_liquido['valores_conta'], raw['formulario_cadastral']['data_referencia_documento'])
    else:
        raise Exception('the world is over')


def convert(raw, id_documento):
    patrimonio_liquido = __indices_to_date(raw)

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
