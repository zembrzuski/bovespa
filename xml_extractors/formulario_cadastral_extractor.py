import xmltodict
import helpers.date_helper as date_helper


def extract_information(register_form):
    the_dict = xmltodict.parse(register_form.decode('utf-8'))

    referencia = date_helper.parse(the_dict['Documento']['DataReferenciaDocumento'].strip())
    entrega = date_helper.parse(the_dict['Documento']['DataEntrega'].strip())

    return {
        'codigo_cvm': the_dict['Documento']['CompanhiaAberta']['CodigoCvm'].strip().replace('-', ''),
        'razao_social': the_dict['Documento']['CompanhiaAberta']['NomeRazaoSocialCompanhiaAberta'].strip(),
        'data_referencia_documento': referencia,
        'data_entrega': entrega
    }
