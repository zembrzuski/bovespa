import register_form_extractor
import helpers.download_helper as downloader_helper
import helpers.zip_helper as zip_helper


def get_inner_zip_information(original_zip_file):
    inner_zip_item = list(filter(lambda file: 'xml' not in file.filename, original_zip_file.filelist))[0]
    inner_zip_bytes = zip_helper.open_zip_file(original_zip_file, inner_zip_item)

    return zip_helper.bytes_to_zipfile(inner_zip_bytes)


def get_information_from_file(downloaded_file):
    retrieved_zip_file = zip_helper.bytes_to_zipfile(downloaded_file)

    register_form_item = list(filter(
        lambda file: 'FormularioCadastral.xml' == file.filename, retrieved_zip_file.filelist))[0]
    register_form_file = zip_helper.open_zip_file(retrieved_zip_file, register_form_item)

    document_type = 'DFP' \
        if len(list(filter(lambda file: 'DFP' in file.filename, retrieved_zip_file.filelist))) > 0 \
        else 'ITR'



    inner_zip_files = get_inner_zip_information(retrieved_zip_file)

    all_files = {
        'document_type': document_type,
        'register_form': register_form_file
    }

    return all_files


def main():
    url_to_download = \
        'https://www.rad.cvm.gov.br/enetconsulta/frmDownloadDocumento.aspx?' \
        'CodigoInstituicao=2&NumeroSequencialDocumento=81551'

    downloaded_file = downloader_helper.download_zip_file_from_bovespa(url_to_download)
    all_files = get_information_from_file(downloaded_file)

    xoxo = register_form_extractor.extract_informmation(all_files['register_form'])

    print('ae')


if __name__ == '__main__':
    main()
