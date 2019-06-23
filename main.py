import register_form_extractor
import helpers.download_helper as downloader_helper
import helpers.zip_helper as zip_helper


def get_information_from_file(downloaded_file):
    retrieved_zip_file = zip_helper.bytes_to_zipfile(downloaded_file)

    register_form = list(filter(
        lambda file: 'FormularioCadastral.xml' == file.filename, retrieved_zip_file.filelist))[0]

    document_type = 'DFP' \
        if len(list(filter(lambda file: 'DFP' in file.filename, retrieved_zip_file.filelist))) > 0 \
        else 'ITR'

    inner_zip_file = list(filter(lambda file: 'xml' not in file.filename, retrieved_zip_file.filelist))[0]

    all_files = {
        'original_zip_file': retrieved_zip_file,
        'document_type': document_type,
        'register_form': register_form
    }

    return all_files


def main():
    url_to_download = \
        'https://www.rad.cvm.gov.br/enetconsulta/frmDownloadDocumento.aspx?' \
        'CodigoInstituicao=2&NumeroSequencialDocumento=81551'

    downloaded_file = downloader_helper.download_zip_file_from_bovespa(url_to_download)
    all_files = get_information_from_file(downloaded_file)

    xoxo = register_form_extractor.extract_informmation(all_files)

    print('ae')


if __name__ == '__main__':
    main()
