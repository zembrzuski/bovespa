from xml_extractors import formulario_cadastral_extractor
import helpers.download_helper as downloader_helper
import helpers.bovespa_unzipper as bovespa_unzipper


def main():
    url_to_download = \
        'https://www.rad.cvm.gov.br/enetconsulta/frmDownloadDocumento.aspx?' \
        'CodigoInstituicao=2&NumeroSequencialDocumento=81551'

    downloaded_file = downloader_helper.download_zip_file_from_bovespa(url_to_download)
    all_files = bovespa_unzipper.unzip(downloaded_file)

    formulario_cadastral_info = formulario_cadastral_extractor.extract_informmation(all_files['formulario_cadastral'])

    print('ae')


if __name__ == '__main__':
    main()
