import xmltodict
import helpers.date_helper as date_helper


def extract_informmation(register_form):
    ae = xmltodict.parse(register_form.decode('utf-8'))

    referencia = date_helper.parse(ae['Documento']['DataReferenciaDocumento'].strip())
    entrega = date_helper.parse(ae['Documento']['DataEntrega'].strip())

    return {
        'codigo_cvm': ae['Documento']['CompanhiaAberta']['CodigoCvm'].strip().replace('-', ''),
        'razao_social': ae['Documento']['CompanhiaAberta']['NomeRazaoSocialCompanhiaAberta'].strip(),
        'data_referencia_documento': referencia,
        'data_entrega': entrega
    }
