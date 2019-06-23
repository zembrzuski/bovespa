from xml_extractors import formulario_cadastral_extractor
import helpers.download_helper as downloader_helper
import helpers.zip_helper as zip_helper


def get_inner_zip_information(original_zip_file):
    inner_zip_item = list(filter(lambda file: 'xml' not in file.filename, original_zip_file.filelist))[0]
    inner_zip_bytes = zip_helper.open_file_inside_zip_file(original_zip_file, inner_zip_item.filename)
    inner_zip_file = zip_helper.bytes_to_zipfile(inner_zip_bytes)

    return inner_zip_file


def get_information_from_file(downloaded_file):
    root_zip_file = zip_helper.bytes_to_zipfile(downloaded_file)
    inner_zip_files = get_inner_zip_information(root_zip_file)

    formulario_cadastral = zip_helper.open_file_inside_zip_file(root_zip_file, 'FormularioCadastral.xml')
    informacoes_financeiras = zip_helper.open_file_inside_zip_file(inner_zip_files, 'InfoFinaDFin.xml')

    document_type = get_document_type(root_zip_file)

    return {
        'document_type': document_type,
        'formulario_cadastral': formulario_cadastral,
        'informacoes_financeiras': informacoes_financeiras
    }


def get_document_type(root_zip_file):
    return 'DFP' \
        if len(list(filter(lambda file: 'DFP' in file.filename, root_zip_file.filelist))) > 0 \
        else 'ITR'


def main():
    url_to_download = \
        'https://www.rad.cvm.gov.br/enetconsulta/frmDownloadDocumento.aspx?' \
        'CodigoInstituicao=2&NumeroSequencialDocumento=81551'

    downloaded_file = downloader_helper.download_zip_file_from_bovespa(url_to_download)
    all_files = get_information_from_file(downloaded_file)

    formulario_cadastral_info = formulario_cadastral_extractor.extract_informmation(all_files['formulario_cadastral'])

    print('ae')


if __name__ == '__main__':
    main()
