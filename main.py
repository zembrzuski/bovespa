import requests
import zipfile
import io as io
import register_form_extractor

def bytes_to_zipfile(the_bytes):
    zip_data = io.BytesIO()
    zip_data.write(the_bytes)

    return zipfile.ZipFile(zip_data)


def download_zip_file_from_bovespa():
    url_to_download = \
        'https://www.rad.cvm.gov.br/enetconsulta/frmDownloadDocumento.aspx?' \
        'CodigoInstituicao=2&NumeroSequencialDocumento=81551'

    retrieved_zip_file = bytes_to_zipfile(requests.get(url_to_download, verify=False).content)

    # TODO talvez eu deva extrair esse cara para uma funcao separada para reutiliza-la
    # em outros arquivos
    register_form = list(filter(
        lambda file: 'FormularioCadastral.xml' == file.filename, retrieved_zip_file.filelist))[0]

    all_files = {
        'original_zip_file': retrieved_zip_file,
        'register_form': register_form
    }

    return all_files


def main():
    all_files = download_zip_file_from_bovespa()

    # TODO guardar se eh dfp or itf
    xoxo = register_form_extractor.extract_informmation(all_files)

    print('ae')


if __name__ == '__main__':
    main()
