from helpers import date_helper


def demonstrativo_mapper_primeiro_tri(data_documento):
    one_year_before = date_helper.parse('{}-{}-{}T00:00:00'.format(
        data_documento.year - 1, data_documento.month, data_documento.day))

    return {
        3: data_documento,
        5: one_year_before
    }


def demonstrativo_mapper(data_documento):
    one_year_before = date_helper.parse('{}-{}-{}T00:00:00'.format(
        data_documento.year - 1, data_documento.month, data_documento.day))

    return {
        1: data_documento,
        4: one_year_before
    }


def balanco_mapper(patrimonio_liquido, data_documento):
    mapper = {
        1: data_documento,
        2: date_helper.parse('{}-12-31T00:00:00'.format(data_documento.year - 1))
    }

    return mapper


def indices_to_date_itr(patrimonio_liquido, data_documento):
    return {
        'balanco': [
            balanco_mapper(patrimonio_liquido, data_documento),  # primeiro tri
            balanco_mapper(patrimonio_liquido, data_documento),  # segundo tri
            balanco_mapper(patrimonio_liquido, data_documento),  # terceiro tri
            balanco_mapper(patrimonio_liquido, data_documento),  # quarto tri
        ],
        'demonstrativo': [
            demonstrativo_mapper_primeiro_tri(data_documento),  # 1o tri
            demonstrativo_mapper(data_documento),  # 2o tri
            demonstrativo_mapper(data_documento),  # 3o tri
            demonstrativo_mapper(data_documento),  # 4o tri
        ]
    }
