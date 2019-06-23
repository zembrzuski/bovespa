import helpers.zip_helper as zip_helper


def get_document_type(root_zip_file):
    # TODO isso aqui está um pouquinho ruim. Deveria pegar a info se é
    # DFP ou ITR lendo o conteúdo do arquivo e não com uma lógica de nome de arquivo.
    return 'DFP' \
        if len(list(filter(lambda file: 'DFP' in file.filename, root_zip_file.filelist))) > 0 \
        else 'ITR'


def get_inner_zip_information(original_zip_file):
    inner_zip_item = list(filter(lambda file: 'xml' not in file.filename, original_zip_file.filelist))[0]
    inner_zip_bytes = zip_helper.open_file_inside_zip_file(original_zip_file, inner_zip_item.filename)
    inner_zip_file = zip_helper.bytes_to_zipfile(inner_zip_bytes)

    return inner_zip_file


def unzip(downloaded_file):
    root_zip_file = zip_helper.bytes_to_zipfile(downloaded_file)
    inner_zip_files = get_inner_zip_information(root_zip_file)

    formulario_cadastral = zip_helper.open_file_inside_zip_file(root_zip_file, 'FormularioCadastral.xml')
    informacoes_financeiras = zip_helper.open_file_inside_zip_file(inner_zip_files, 'InfoFinaDFin.xml')
    composicao_capital_social = zip_helper.open_file_inside_zip_file(inner_zip_files, 'ComposicaoCapitalSocialDemonstracaoFinanceiraNegocios.xml')

    document_type = get_document_type(root_zip_file)

    return {
        'document_type': document_type,
        'formulario_cadastral': formulario_cadastral,
        'informacoes_financeiras': informacoes_financeiras,
        'composicao_capital_social': composicao_capital_social
    }
