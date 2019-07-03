from helpers import date_helper


def balanco_mapper(patrimonio_liquido, data_documento):
    mapper = {
        0: data_documento,
        1: date_helper.parse('{}-12-31T00:00:00'.format(data_documento.year - 1))
    }

    if patrimonio_liquido['valores_conta'][2] != 0:
        mapper[2] = date_helper.parse('{}-12-31T00:00:00'.format(data_documento.year - 2))

    return mapper


def indices_to_date_dfp(patrimonio_liquido, data_documento):
    return {
        'balanco': balanco_mapper(patrimonio_liquido, data_documento)
    }
