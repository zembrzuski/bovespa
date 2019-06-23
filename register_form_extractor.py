import xmltodict
import helpers.date_helper as date_helper


def extract_informmation(all_files):
    # retrieved_zip_file.open(innerzip.filename).read()

    # TODO talvez eu deva extrair esse cara para uma funcao para reutiliza-lo em outros
    # arquivos
    register_form = \
        all_files['original_zip_file'].open(all_files['register_form'].filename).read()

    ae = xmltodict.parse(register_form.decode('utf-8'))

    referencia = date_helper.parse(ae['Documento']['DataReferenciaDocumento'].strip())
    entrega = date_helper.parse(ae['Documento']['DataEntrega'].strip())

    return {
        'codigo_cvm': ae['Documento']['CompanhiaAberta']['CodigoCvm'].strip().replace('-', ''),
        'razao_social': ae['Documento']['CompanhiaAberta']['NomeRazaoSocialCompanhiaAberta'].strip(),
        'data_referencia_documento': referencia,
        'data_entrega': entrega
    }
