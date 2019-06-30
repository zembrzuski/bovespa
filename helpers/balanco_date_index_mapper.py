from helpers import conta_extractor_helper
from helpers import date_helper

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


def __do_itr_stupid_validation(patrimonio_liquido):
    valores_conta = patrimonio_liquido['valores_conta']

    if valores_conta[0] != 0.:
        raise Exception("nao previ o caso para contas de itr cujo primeiro valor nao eh zero")

    if len(list(filter(lambda x: x != 0., valores_conta))) > 2:
        raise Exception("nao previ o caso para contas de itr que possuem mais do que dois valores")


def __indices_to_date_itr(patrimonio_liquido, data_documento):
    __do_itr_stupid_validation(patrimonio_liquido)

    return {
        1: data_documento,
        2: date_helper.parse('{}-12-31T00:00:00'.format(data_documento.year-1))
    }


def __do_dfp_stupid_validation(patrimonio_liquido):
    valores_conta = patrimonio_liquido['valores_conta']

    if valores_conta[0] == 0 or valores_conta[1] == 0:
        raise Exception('Só previ caso em que patrimonios liquidos de dfp sao preenchidos nas posicoes 1 e 2')

    if valores_conta[3] != 0 or valores_conta[4] != 0:
        raise Exception('Só previ caso em que patrimonios liquidos de dfp sao até as posicoes 1 e 2')


def __indices_to_date_dfp(patrimonio_liquido, data_documento):
    __do_dfp_stupid_validation(patrimonio_liquido)

    mapper = {
        0: data_documento,
        1: date_helper.parse('{}-12-31T00:00:00'.format(data_documento.year - 1))
    }

    if patrimonio_liquido['valores_conta'][2] != 0:
        mapper[2] = date_helper.parse('{}-12-31T00:00:00'.format(data_documento.year - 2))

    return mapper


def indices_to_date(raw):
    patrimonio_liquido = conta_extractor_helper.retrieve_a_given_conta(
        'patrimonio_liquido', raw['informacoes_financeiras'])

    data_documento = raw['formulario_cadastral']['data_documento']['data_referencia_documento']

    if raw['document_type'] == 'ITR':
        return __indices_to_date_itr(patrimonio_liquido, data_documento)

    if raw['document_type'] == 'DFP':
        return __indices_to_date_dfp(patrimonio_liquido, data_documento)
